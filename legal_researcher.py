import autogen
from config import llm_config

stock_analyst = autogen.AssistantAgent(
    name="Stock_Analyst",
    llm_config=llm_config,
    system_message="""You are a professional Financial Data Extractor.

    YOUR TOOL:
    1. get_stock_price(ticker): Use this tool to get the current stock price for a given ticker symbol.

    YOUR PROCESS:
    - If the user asks for a stock price -> Call the 'get_stock_price' tool immediately.
    - After calling the tool, **WAIT** for the execution result from the User Proxy.
    - Once the tool returns the price, state the final price clearly.
    - CRITICAL: After providing the final price, you **MUST** respond with "TERMINATE" and nothing else.
    """
)