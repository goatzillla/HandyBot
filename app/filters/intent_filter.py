from aiogram.filters import BaseFilter
from aiogram.types import Message

from loaders.knowledge_loader import get_intent

class IntentFilter(BaseFilter):
    async def __call__(self, message):
        if not message.text:
            return None
        
        intent_data = get_intent(message.text)

        if intent_data:
            return intent_data
        
        return False