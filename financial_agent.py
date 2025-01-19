from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import openai
load_dotenv()

openai.api_key=os.getenv("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")
os.environ["GROQ_API_KEY"] = "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"

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

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)