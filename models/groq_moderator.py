from groq import Groq
from dotenv import load_dotenv
import os
import time
import random

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

TOXIC_KEYWORDS = [
    'hate', 'stupid', 'idiot', 'noob', 'kill', 'trash', 
    'worthless', 'ugly', 'fat', 'die', 'kys', 'retard',
    'suck', 'worst', 'disgusting', 'awful', 'terrible'
]

def is_potentially_toxic(message: str) -> bool:
    lower_msg = message.lower()
    return any(keyword in lower_msg for keyword in TOXIC_KEYWORDS)

def moderate_message(message: str) -> str:
    if is_potentially_toxic(message):
        return 'toxic'
    
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": """You are a toxic content moderator. Analyze the following message and determine if it contains:
                                1. Hate speech or discrimination
                                2. Severe toxicity
                                3. Threats or violent language
                                4. Sexual content
                                5. Harassment or bullying
                                6. Excessive profanity

                                Respond ONLY with the single word 'toxic' or 'clean' based on your analysis."""
                },
                {
                    "role": "user", 
                    "content": f"Message to analyze: \"{message}\"\n\nYour response (toxic/clean):"
                }
            ],
            model="llama3-8b-8192",
            temperature=0.1, 
            max_tokens=1
        )
        
        result = response.choices[0].message.content.strip().lower()
        return result if result in ['toxic', 'clean'] else 'clean'
    except Exception as e:
        print(f"Groq API error: {e}")
        return 'toxic' if is_potentially_toxic(message) else 'clean'