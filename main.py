import os
import autogen
from agents.user_proxy import user_proxy
from agents.legal_researcher import stock_analyst
from tools.extract import get_stock_price

TARGET_TICKER = "META"
TASK_PROMPT = f"What is the current stock price for {TARGET_TICKER}?"


# Register the Tool with AutoGen
autogen.agentchat.register_function(
    get_stock_price,
    caller=stock_analyst,
    executor=user_proxy,
    name="get_stock_price",
    description="Fetch the current stock price for a given ticker symbol (e.g., META, GOOGL)."
)

if __name__ == "__main__":
    if not os.path.exists("coding"):
        os.makedirs("coding")

    print(f"Starting Stock Analyst...\nTask: {TASK_PROMPT}\n" + "=" * 40)

    # Check if API key was loaded (optional but good practice)
    from config import llm_config
    if not llm_config['config_list'][0].get('api_key'):
        print("FATAL ERROR: MISTRAL_API_KEY is missing. Please check your .env file.")
        exit(1)

    # Initiate the conversation
    user_proxy.initiate_chat(
        stock_analyst,
        message=TASK_PROMPT
    )