#2. Character Text Splitter (Fixed-size chunks)
# This basic splitter divides text based on a fixed number of characters, regardless of sentence or paragraph structure.
#  It is simpler but may break sentences in awkward places. 

from langchain_text_splitters import CharacterTextSplitter

text = "The quick brown fox jumps over the lazy dog. The dog is very lazy indeed."

splitter = CharacterTextSplitter(
    separator=".", # You can specify a separator, e.g., split by sentence ending
    chunk_size=20,
    chunk_overlap=0,
    length_function=len
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}\n")
