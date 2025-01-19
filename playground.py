from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import openai
from phi.model.openai import OpenAIChat

import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api=os.getenv("phi-twxBwAatqYBLDIXOZwLThP40XB5KqAKAa4r4vQ11mJw")


web_search_agent=Agent(
    name="Web Search Agnet",
    role="Search the web for the information",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)


finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True,stock_fundamentals=True),],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,



)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__ =="__main__":
    serve_playground_app("playground:app",reload=True)