
# markdown_chunking
from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Header 1
Introduction to LangChain

## Header 2
Text splitting techniques

### Header 3
Character-based, token-based, markdown-aware
"""

headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
docs = splitter.split_text(markdown_text)

for i, doc in enumerate(docs, 1):
    print(f"Chunk {i}:\n{doc}\n")
