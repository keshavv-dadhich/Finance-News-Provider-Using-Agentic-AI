# Financial AI Agent

A powerful AI-powered financial analysis tool that combines web search capabilities with real-time stock market data analysis using Phidata and Groq's LLM models.

## Features

- Real-time stock market data analysis
- Web search integration for comprehensive research
- Interactive playground interface
- Multi-agent architecture for complex queries
- Stock fundamentals and analyst recommendations
- Company news and information tracking

## Prerequisites

- Python 3.8+
- API keys for:
  - Phidata
  - Groq
  - OpenAI (optional)

## Installation

1. Clone the repository and navigate to the project directory

2. Install required dependencies:
```bash
pip install phidata python-dotenv yfinance packaging duckduckgo-search fastapi uvicorn groq openai
```

3. Create a `.env` file in the project root and add your API keys:
```env
PHI_API_KEY="your-phi-api-key"
GROQ_API_KEY="your-groq-api-key"
OPENAI_API_KEY="your-openai-api-key"
```

## Project Structure

The project consists of two main agents:

1. **Web Search Agent**
   - Powered by Groq's llama-3.2-90b-vision-preview model
   - Utilizes DuckDuckGo for web searches
   - Provides sourced information from across the web

2. **Finance Agent**
   - Uses Groq's llama-3.2-90b-vision-preview model
   - Integrates with YFinance for real-time market data
   - Features include:
     - Stock price tracking
     - Analyst recommendations
     - Company information
     - Latest news
     - Stock fundamentals

## Usage

### Running the Playground

```python
from phi.playground import Playground, serve_playground_app

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
```

### Using the Multi-AI Agent

```python
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Example query
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
```

## Agent Configuration

### Web Search Agent
```python
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)
```

### Finance Agent
```python
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        company_news=True,
        stock_fundamentals=True
    )],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)
```

## Tools and Integrations

- **YFinance Tools**: Access to real-time market data and financial information
- **DuckDuckGo**: Web search capabilities for comprehensive research
- **Groq LLM Models**: Advanced language processing and analysis
- **Phidata Framework**: Agent orchestration and management
- **FastAPI**: Web interface for the playground

## Development

The project uses FastAPI for the playground interface and supports hot reloading during development. The agents can be modified and extended by adding new tools or changing the model configurations.

## Security Notes

- Keep your API keys secure and never commit them to version control
- Use environment variables for sensitive information
- Regularly rotate API keys following security best practices

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]
