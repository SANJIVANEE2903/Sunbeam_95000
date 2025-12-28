
# Sample text
text = [
    """
    A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs, which enable computers to perform a wide range of tasks.
    """
]

print("3. Token-Based Chunking (offline-friendly)")

# Use CharacterTextSplitter from langchain_text_splitters
from langchain_text_splitters import CharacterTextSplitter

# Approximate token-based splitting
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)

# Create documents
docs = text_splitter.create_documents(text)

# Print each chunk
for i, doc in enumerate(docs, 1):
    print(f"--- Chunk {i} ---")
    print(doc.page_content)
    print()
