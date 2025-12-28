from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import pandas as pd

# -------------------------------
# Load API key from .env
# -------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# -------------------------------
# Initialize LLM
# -------------------------------
llm = init_chat_model(
    model="llama-3.1-8b-instant",  # Supported model
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

# -------------------------------
# Initialize conversation with system prompt
# -------------------------------
conversation = [
    {"role": "system", "content": "You are a SQLite expert developer with 10 years of experience."}
]

# -------------------------------
# Load CSV
# -------------------------------
csv_file = input("Enter path of a CSV file: ").strip()
df = pd.read_csv(csv_file)
print("\nCSV schema:")
print(df.dtypes)
print("\nCSV columns:", df.columns.tolist())

# -------------------------------
# Main loop: Ask questions about CSV
# -------------------------------
while True:
    user_input = input("\nAsk anything about this CSV? ").strip()
    if user_input.lower() == "exit":
        break
    if not user_input:
        continue

    # ---------------------------
    # Step 1: Generate SQL query using LLM
    # ---------------------------
    llm_input = f"""
        Table Name: data
        Table Schema: {df.dtypes}
        Question: {user_input}
        Instruction:
            Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'.
    """
    sql_result = llm.invoke(llm_input)
    sql_query = sql_result.content.strip()
    print("\nGenerated SQL query:")
    print(sql_query)