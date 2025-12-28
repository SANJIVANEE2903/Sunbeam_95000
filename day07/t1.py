# 1. Basic Fixed-Size Chunking
from langchain_text_splitters import CharacterTextSplitter

text = """
LangChain is a framework designed to simplify the creation of applications using large language models (LLMs).
It provides a standard interface for chains, integrations with many tools, and end-to-end chains for common applications.

Document chunking is a critical step in RAG pipelines.
Choosing the right chunking strategy can significantly impact retrieval performance.
Experimenting with chunk size and overlap is often necessary to find the optimal balance for your specific data and use case.
"""

# Initialize RecursiveCharacterTextSplitter
# chunk_size is measured by number of characters by default
text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20, # Overlap helps maintain context across chunks
    length_function=len,
)

# Split the text into chunks
chunks = text_splitter.split_text(text)

# Print the resulting chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}\n")

