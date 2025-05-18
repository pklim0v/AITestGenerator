import anthropic
from config import Config

client = anthropic.Anthropic(api_key=Config.CLAUDE_API_KEY)

