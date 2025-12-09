📈 Stock Price Agent (ML EXAM)

This Stock Price AI Agent designed to fetch real-time stock prices using the yfinance API and a cloud-hosted Mistral LLM through the AutoGen agentic framework.

Instead of manually searching financial sites or relying on hallucinated LLM guesses, the agent uses a clean tool-calling architecture to ensure every answer is grounded in real data.

🚀 Features

✔ Real Stock Prices pulled directly from Yahoo Finance (via yfinance)
✔ Cloud-based LLM (Mistral Nemo) ensures reliable tool-calling
✔ Strict Non-Hallucination Architecture — LLM is forced to use tools
✔ Modern Agent Design: AutoGen ConversableAgent + user proxy
✔ Clear, Extendable Code Structure using a modular src/ layout
✔ CLI support → run the agent with a simple terminal command

🛠️ Architecture

Two-agent architecture:

🧠 Stock_Analyst (LLM Agent)

Cloud-based Mistral LLM

Receives the user’s request

Must call the tool get_stock_price

Never guesses or fabricates stock prices

🔧 User_Proxy

Executes tools

Handles errors, validations

Sends tool results back to the LLM to generate the final answer

🛠️ Tool: get_stock_price

Implemented in tools/extract.py, using yfinance:

Fetches real-time stock data

Extracts regularMarketPrice

Returns the price in a clean format

Provides safe fallback errors when a ticker is invalid

🌐 Workflow Overview

User → Stock_Analyst → get_stock_price → yfinance → Stock_Analyst → User

### Option 1: Using pip


1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create .env file:
    ```bash
    MISTRAL_API_KEY=your_key_here
   ```


###  Running the Generator

```bash

# Using python directly
python main.py
```