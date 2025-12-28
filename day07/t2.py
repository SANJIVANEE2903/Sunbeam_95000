#1. Recursive Character Text Splitter (Recommended for generic text) 
#This splitter attempts to split text using a defined list of separators in order (by default ["\\n\\n", "\\n", " ", ""]).
#  This ensures that larger structural breaks are attempted first, falling back to smaller breaks if the chunk size is still exceeded

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample text to split
raw_text = """
LangChain is a framework for developing applications powered by language models.
It enables applications that are context-aware and reasoning-based.

Text splitting is an important step when working with long documents.
RecursiveCharacterTextSplitter helps break text into manageable chunks
while preserving semantic meaning as much as possible.
"""

# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

# Split text into documents
docs = text_splitter.create_documents([raw_text])

# Print results
for i, doc in enumerate(docs):
    print(f"Chunk {i+1}:")
    print(doc.page_content)
    print("-" * 40)
