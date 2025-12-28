# Recursive Character Chunking

from langchain_text_splitters import RecursiveCharacterTextSplitter

raw_text = """
LangChain handles paragraphs, sentences, and word boundaries.
Recursive splitter preserves semantic meaning better.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50, chunk_overlap=10, separators=["\n\n", "\n", " ", ""]
)
docs = splitter.create_documents([raw_text])

for i, doc in enumerate(docs, 1):
    print(f"Chunk {i}:\n{doc}\n")
