# 5. Code-Aware Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample Python source code
code_text = """
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
"""

# Create a code-aware splitter for Python
code_splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=1000,
    chunk_overlap=100
)

# Split code into documents
docs = code_splitter.create_documents([code_text])

# Display results
for i, doc in enumerate(docs):
    print(f"Chunk {i + 1}:")
    print(doc.page_content)
    print("-" * 20)
