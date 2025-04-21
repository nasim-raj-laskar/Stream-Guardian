from fluvio import Fluvio, Offset
import time
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))

from models.groq_moderator import moderate_message

def consume():
    fluvio = Fluvio.connect()
    consumer = fluvio.partition_consumer("chat-room", 0)

    print("Listening for messages...")

    try:
        last_request_time = 0
        min_interval = 2.1  

        for record in consumer.stream(offset=Offset.from_beginning(0)):
            current_time = time.time()
            elapsed = current_time - last_request_time
            
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            
            last_request_time = time.time()
            
            message = record.value_string()
            verdict = moderate_message(message)

            debug_info = f"[{datetime.now().strftime('%H:%M:%S')}] "
            if verdict == "toxic":
                debug_info += f"[⚠️ FLAGGED] {message}"
            else:
                debug_info += f"[OK] {message}"
            
            print(debug_info)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    consume()