"""
=========================================================
RESUME CHUNKING + EMBEDDINGS + CHROMADB
(Custom chunker for LangChain v1.2.1)
=========================================================
"""

# =====================================================
# STEP 1: IMPORTS
# =====================================================
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings

# =====================================================
# STEP 2: EMBEDDING MODEL (LOCAL)
# =====================================================
embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)

# =====================================================
# STEP 3: LOAD PDF RESUME
# =====================================================
def load_pdf_resume(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    full_text = ""
    for page in docs:
        full_text += page.page_content + "\n"
    return full_text

resume_path = r"G:\GIT\day08\fake-resumes\resume-003.pdf"
resume_text = load_pdf_resume(resume_path)
print("Resume loaded ✅")
print(resume_text[:300], "...")  # preview first 300 characters

# =====================================================
# STEP 4: CUSTOM CHUNKING FUNCTION
# =====================================================
def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits text into chunks with specified size and overlap.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# Create chunks
chunks_to_store = chunk_text(resume_text, chunk_size=800, overlap=100)
print(f"Chunks created: {len(chunks_to_store)}")

# =====================================================
# STEP 5: CREATE EMBEDDINGS FOR CHUNKS
# =====================================================
chunk_embeddings = embed_model.embed_documents(chunks_to_store)
print("Chunk embeddings created ✅")

# =====================================================
# STEP 6: CHROMADB SETUP
# =====================================================
client = chromadb.PersistentClient(path="./knowledge_base")

collection = client.get_or_create_collection(
    name="resume_chunks",
    embedding_function=None
)

# =====================================================
# STEP 7: STORE CHUNKS IN CHROMADB
# =====================================================
ids = [f"resume_003_chunk_{i}" for i in range(len(chunks_to_store))]
metadatas = [{"chunk_index": i, "source": resume_path} for i in range(len(chunks_to_store))]

collection.add(
    ids=ids,
    embeddings=chunk_embeddings,
    documents=chunks_to_store,
    metadatas=metadatas
)

print("Chunks stored in ChromaDB ✅")

# =====================================================
# STEP 8: QUERY OVER CHUNKS
# =====================================================
query = "SQL and data visualization experience"
query_embedding = embed_model.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# =====================================================
# STEP 9: DISPLAY RESULTS
# =====================================================
print("\n🔍 Top Matching Chunks:\n")
for i, doc in enumerate(results["documents"][0]):
    print(f"--- Match {i+1} ---")
    print(doc[:300])  # preview first 300 characters
    print()
