import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings


# ============================
# EMBEDDING MODEL (LOCAL)
# ============================
embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)


# ============================
# LOAD PDF
# ============================
def load_pdf_resume(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text = ""
    for page in docs:
        text += page.page_content + "\n"

    metadata = {
        "source": pdf_path,
        "page_count": len(docs)
    }

    return text, metadata


# ============================
# LOAD RESUME
# ============================
resume_path = r"G:\GIT\day08\fake-resumes\resume-003.pdf"
resume_text, resume_info = load_pdf_resume(resume_path)

print("Resume loaded ✅")


# ============================
# CREATE EMBEDDINGS
# ============================
resume_embeddings = embed_model.embed_documents([resume_text])
print(f"Embedding length: {len(resume_embeddings[0])} ✅")


# ============================
# CHROMADB (NO EMBEDDING FN)
# ============================
client = chromadb.PersistentClient(path="./knowledge_base")

collection = client.get_or_create_collection(
    name="resumes",
    embedding_function=None   # 🔥 critical
)


# ============================
# STORE RESUME
# ============================
collection.add(
    ids=["resume_003"],
    embeddings=resume_embeddings,
    documents=[resume_text],
    metadatas=[resume_info]
)

print("Resume stored in ChromaDB ✅")


# ============================
# QUERY (MANUAL EMBEDDING)
# ============================
query = "Python developer with machine learning experience"

query_embedding = embed_model.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print("\n🔍 Query Result:")
print(results["documents"][0][0][:500])
