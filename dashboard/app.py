from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
from fluvio import Fluvio, Offset
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../models')))
from models.groq_moderator import moderate_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'streamguardian123'
socketio = SocketIO(app, cors_allowed_origins="*")

#counters
stats = {
    'total': 0,
    'clean': 0,
    'toxic': 0,
    'last_toxic': None,
    'toxic_per_minute': 0,
    'messages': [],
    'toxic_trend': []
}

def consume_messages():
    fluvio = Fluvio.connect()
    consumer = fluvio.partition_consumer("chat-room", 0)
    
    print("Dashboard consumer started...")
    
    try:
        last_request_time = 0
        min_interval = 2.1
        last_minute_check = time.time()
        toxic_count_minute = 0

        for record in consumer.stream(offset=Offset.from_beginning(0)):
            current_time = time.time()
            elapsed = current_time - last_request_time
            
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            
            last_request_time = time.time()
            
            message = record.value_string()
            verdict = moderate_message(message).lower()
            
            #stats
            stats['total'] += 1
            if verdict == 'toxic':
                stats['toxic'] += 1
                toxic_count_minute += 1
                message_type = '⚠️ FLAGGED'
                stats['last_toxic'] = message
            else:
                stats['clean'] += 1
                message_type = 'OK'
            
            #Track toxic messages every 30 seconds 
            if current_time - last_minute_check >= 30:
                stats['toxic_per_minute'] = toxic_count_minute
                stats['toxic_trend'].append(toxic_count_minute)
                if len(stats['toxic_trend']) > 10:  
                    stats['toxic_trend'].pop(0)
                toxic_count_minute = 0
                last_minute_check = current_time
            
            message_data = {
                'text': message,
                'type': message_type,
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'verdict': verdict
            }
            
            stats['messages'].append(message_data)
            socketio.emit('update', {
                'stats': stats,
                'newMessage': message_data
            })
            
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
        consume_messages()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=consume_messages, daemon=True).start()
    socketio.run(app, debug=True, port=5000)