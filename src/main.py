# Web Server - FastAPI

# Example in main.py
from fastapi import FastAPI
from src.agents.research_agent import get_research_agent

app = FastAPI()

@app.post("/chat")
async def chat(query: str):
    agent_executor = get_research_agent()
    return await agent_executor.ainvoke({"input": query})