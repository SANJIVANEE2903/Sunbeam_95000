# 3. Markdown Header Text Splitter (Structure-aware chunking)
# For structured documents like Markdown files,
#  this splitter preserves the hierarchy of headers and appends relevant header metadata to each chunk,
#  improving contextual relevance during retrieval. 
from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Chapter 1: Introduction
Welcome to the first chapter of the guide. This section covers the basics.

## Section 1.1: Setup
Instructions for setting up the environment are provided here.
Make sure to install Python 3.10 or later.

# Chapter 2: Advanced Topics
This chapter dives into more complex subjects.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

# Initialize the MarkdownHeaderTextSplitter
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False # Keep headers in the chunk content
)

# Split the text and create LangChain Document objects
docs = markdown_splitter.create_documents([markdown_text])

# Print the resulting documents (each document is a chunk with metadata)
for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}\n")

