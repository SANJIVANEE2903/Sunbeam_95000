"""
=========================================================
STEP-BY-STEP RESUME EMBEDDING & SEARCH USING CHROMADB
=========================================================

WHAT THIS SCRIPT DOES:
1. Loads a PDF resume
2. Extracts text
3. Generates embeddings using LOCAL embedding server
4. Stores data in ChromaDB (persistent)
5. Queries resume using semantic search

IMPORTANT:
- We DISABLE Chroma's internal embedding model
- We MANUALLY generate embeddings
=========================================================
"""

# =========================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# =========================================================
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings


# =========================================================
# STEP 2: INITIALIZE EMBEDDING MODEL (LOCAL SERVER)
# =========================================================
# This connects to your local OpenAI-compatible embedding server
embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)


# =========================================================
# STEP 3: FUNCTION TO LOAD PDF RESUME
# =========================================================
def load_pdf_resume(pdf_path):
    """
    Loads a PDF resume and combines all page text into one string
    """
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    resume_text = ""
    for page in docs:
        resume_text += page.page_content + "\n"

    metadata = {
        "source": pdf_path,
        "page_count": len(docs)
    }

    return resume_text, metadata


# =========================================================
# STEP 4: LOAD RESUME FILE
# =========================================================
resume_path = r"G:\GIT\day08\fake-resumes\resume-003.pdf"

resume_text, resume_info = load_pdf_resume(resume_path)

print("Resume loaded ✅")
print(resume_info)
print(resume_text[:300])  # preview


# =========================================================
# STEP 5: CREATE EMBEDDING FOR RESUME
# =========================================================
# IMPORTANT:
# embed_documents() expects a LIST of documents
resume_embeddings = embed_model.embed_documents([resume_text])

print(f"Embedding length: {len(resume_embeddings[0])} ✅")


# =========================================================
# STEP 6: INITIALIZE CHROMADB (PERSISTENT STORAGE)
# =========================================================
client = chromadb.PersistentClient(path="./knowledge_base")

# VERY IMPORTANT:
# embedding_function=None
# -> prevents Chroma from downloading its own model
collection = client.get_or_create_collection(
    name="resumes",
    embedding_function=None
)


# =========================================================
# STEP 7: ADD RESUME TO CHROMADB
# =========================================================
"""
RULE:
- ids, embeddings, documents, metadatas
  MUST HAVE SAME LENGTH
"""

collection.add(
    ids=["resume_003"],                  # unique identifier
    embeddings=resume_embeddings,         # list of vectors
    documents=[resume_text],              # original resume text
    metadatas=[resume_info]               # extra information
)

print("Resume stored in ChromaDB ✅")


# =========================================================
# STEP 8: QUERY THE RESUME (SEMANTIC SEARCH)
# =========================================================
query = "Python developer with machine learning experience"

# IMPORTANT:
# We MANUALLY embed the query
query_embedding = embed_model.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)


# =========================================================
# STEP 9: DISPLAY RESULTS
# =========================================================
print("\n🔍 Query Result:")
print(results["documents"][0][0][:500])
