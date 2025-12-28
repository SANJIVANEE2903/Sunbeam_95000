from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import pandas as pd

# Load API key from .env
load_dotenv()

# Initialize Groq LLM (use a supported model)
llm = init_chat_model(
    model="llama-3.1-8b-instant",  # ✅ supported
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize conversation with system prompt
conversation = [
    {"role": "system", "content": "You are a SQLite expert developer with 10 years of experience."}
]

# Load CSV into pandas DataFrame
csv_file = input("Enter path of a CSV file: ").strip()
df = pd.read_csv(csv_file)
print("CSV schema: ")
print(df.dtypes)
print("\nCSV columns:", df.columns.tolist())

while True:
    # Ask user for a query-related question
    user_input = input("\nAsk anything about this CSV? ").strip()
    if user_input.lower() == "exit":
        break
    if not user_input:
        continue

    # Step 1: Generate SQL query using LLM
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

    # Step 2: Execute the SQL query on the DataFrame using pandas
    try:
        # Use pandasql for SQL execution on pandas
        import pandasql as ps
        query_result = ps.sqldf(sql_query, locals())
        print("\nQuery Result:")
        print(query_result)
    except Exception as e:
        query_result = None
        print("\nError executing SQL:", e)

    # Step 3: Ask LLM to explain the result in English
    if query_result is not None:
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
