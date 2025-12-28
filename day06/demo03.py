from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import re

@tool
def calculator(expression: str):
    """
    Solves numeric arithmetic expressions only.
    Supports +, -, *, /, and parentheses.
    Variables like x, y are NOT supported.
    """
    try:
        # Reject variables explicitly
        if re.search(r"[a-zA-Z]", expression):
            return "Error: Only numeric expressions are supported."

        result = eval(expression, {"__builtins__": {}})
        return str(result)

    except Exception:
        return "Error: Invalid arithmetic expression."


# create model (LM Studio – OpenAI compatible)
llm = init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="non-needed"
)

# create agent
agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="""
You are a helpful assistant.
Use the calculator tool ONLY for numeric arithmetic.
If variables like x are present, say algebra is not supported.
Answer briefly.
"""
)

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = agent.invoke({
            "messages": [{"role": "user", "content": user_input}]
        })

        print("AI:", result["messages"][-1].content)

    except KeyboardInterrupt:
        print("\nExited.")
        break
