from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

model = Groq(id="openai/gpt-oss-20b")
agent = Agent(
    model=model, 
    instructions="You are a helpful assistant. Provide Concise and If required Provide Tabular for statistical data", 
    markdown=True, 
    debug_mode=False
)

agent.print_response("Tell me about Allied Bank Limited?", stream=True)