from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company_name: str) -> str:
    """
    Get the stock symbol (ticker) for a given company name.
    
    This function maps the top 10 tech company names to their stock exchange symbols.
    Use this when users mention company names and you need to find their stock symbols.
    
    Args:
        company_name (str): The name of the company (e.g., "Tesla", "Microsoft", "Apple").
    
    Returns:
        str: The stock symbol for the company, or an error message if not found.
    
    Examples:
        - "Tesla" -> "TSLA"
        - "Microsoft" -> "MSFT"
        - "Apple" -> "AAPL"
        - "Nvidia" -> "NVDA"
        - "Meta" -> "META"
    """
    # Top 10 Tech Companies mapping
    company_symbols = {
        "apple": "AAPL",
        "microsoft": "MSFT",
        "google": "GOOGL",
        "alphabet": "GOOGL",
        "amazon": "AMZN",
        "nvidia": "NVDA",
        "nvida": "NVDA",  # Common misspelling
        "meta": "META",
        "facebook": "META",
        "tesla": "TSLA",
        "netflix": "NFLX",
        "oracle": "ORCL",
        "adobe": "ADBE",
    }
    
    # Normalize input: lowercase and strip whitespace
    normalized_name = company_name.lower().strip()
    
    # Direct lookup
    if normalized_name in company_symbols:
        return company_symbols[normalized_name]
    
    # Partial match for compound names
    for key, symbol in company_symbols.items():
        if key in normalized_name or normalized_name in key:
            return symbol
    
    # If not found, return error message
    return f"Stock symbol not found for '{company_name}'. This tool only supports the top 10 tech companies: Apple, Microsoft, Google, Amazon, Nvidia, Meta, Tesla, Netflix, Oracle, and Adobe."

model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct", max_tokens=5048)
tools = [YFinanceTools(), get_company_symbol]

agent = Agent(
    model=model,
    tools=tools,
    # tool_call_limit=5, 
    instructions=[
        "You are a helpful assistant that can help with finance related questions.", 
        "You are provided with tools, so use them.", 
        "Use tabular format for statistical data.",
        "Provide concise and accurate response. "
    ],
    stream_intermediate_steps=True,
    markdown=True,
    debug_mode=False
)

agent.print_response("Compare both TSLA and NVDA stocks and give me Price, analysis and recommendation for investment.", stream=True)