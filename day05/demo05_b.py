from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import pandas as pd
import pandasql as ps  # For executing SQL on pandas DataFrame
import ssl
import certifi

# -------------------------------
# SSL fix for Windows
# -------------------------------
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

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
# Conversation initialization
# -------------------------------
conversation = [
    {"role": "system", "content": "You are a SQLite expert developer with 10 years of experience."}
]

# -------------------------------
# Load CSV
# -------------------------------
# Load CSV
data = pd.read_csv("G:/GIT/iit-b-01/emp_hdr.csv")
print("\nCSV schema:")
print(data.dtypes)
print("\nCSV columns:", data.columns.tolist())


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
        Table Schema: {data.dtypes}
        Question: {user_input}
        Instruction:
            Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'.
    """

    result = llm.invoke(llm_input)
    sql_query = result.content.strip()
    print("\nGenerated SQL query:")
    print(sql_query)

    # ---------------------------
    # Step 2: Execute SQL on pandas DataFrame using pandasql
    # ---------------------------
    try:
        query_result = ps.sqldf(sql_query, locals())
        print("\nQuery Result:")
        print(query_result)
    except Exception as e:
        query_result = None
        print("\nError executing SQL:", e)

    # ---------------------------
    # Step 3: Ask LLM to explain the result in English
    # ---------------------------
    if query_result is not None and not query_result.empty:
        explain_input = f"""
            Table Name: data
            Query Result:
            {query_result}
            Instruction:
                Explain the above result in clear English.
                Keep explanation concise.
        """
        explain_result = llm.invoke(explain_input)
        print("\nLLM Explanation of Result:")
        print(explain_result.content)
