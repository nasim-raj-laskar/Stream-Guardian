from fluvio import Fluvio
import asyncio, random, time
from datetime import datetime

chat_samples = [
    "You're amazing!",
    "This is so cool 🔥",
    "I need help!",
    "Such a peaceful stream 💖",
    "Great job everyone!",
    "This community is awesome",
    "Thanks for the help!",
    "Let's play together sometime!",
    "I appreciate your content",
    "I hate this game",
    "Get lost you noob",
    "Why are you so bad at this?",
    "You should uninstall",
    "Worst stream ever",
    "You're trash",
    "KYS",
    "Nobody likes you",
    "Your content is garbage",
    "You're the worst player I've seen",
    "Uninstall and never come back"
]

async def produce():
    fluvio =Fluvio.connect()
    producer =fluvio.topic_producer("chat-room")

    while True:
        msg = random.choice(chat_samples)
        producer.send_string(msg)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sent: {msg}")
        time.sleep(3)

asyncio.run(produce())