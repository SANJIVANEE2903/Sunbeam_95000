# Implement the chunking examples discussed in the provided PDF document.
# basic_fixed_chunking.py
from langchain_text_splitters import CharacterTextSplitter

raw_text = """
LangChain is a framework for building applications with LLMs. 
It provides tools for text splitting, embeddings, chains, agents, 
and more. This example demonstrates character-based chunking.
"""

splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10)
docs = splitter.create_documents([raw_text])

for i, doc in enumerate(docs, 1):
    print(f"Chunk {i}:\n{doc}\n")


