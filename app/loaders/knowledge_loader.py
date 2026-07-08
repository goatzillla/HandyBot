import json
import logging

logger = logging.getLogger(__name__)

DATA_BASE = {}

def load_knowledge_base():
    global DATA_BASE
    try:
        with open("data/knowledge.json", "r", encoding="utf-8") as f:
            DATA_BASE = json.load(f)
        logger.info("Knowledge base loaded successfully")
    except FileNotFoundError:
        logger.error("Knowledge base file not found")

def get_intent(text):
    if not text:
        return None
    
    for intent, data in DATA_BASE.items():
        for trigger in data.get("triggers", []):
            if trigger in text.lower():
                return {
                    "intent_name": intent,
                    "responses": data.get("responses", []),
                    "action": data.get("action", []),
                    "next_state": data.get("next_state", []),
                    "keyboard_name": data.get("keyboard_name", None)
                }
    return None