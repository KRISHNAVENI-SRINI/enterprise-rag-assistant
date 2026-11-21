from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

from config import GEMINI_API_KEY

# Read PDF
pdf_path = "data/sample.pdf"  # replace with your PDF name

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

# Create chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("Number of chunks:", len(chunks))

# Create embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedding_model.encode(chunks)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

print("FAISS Index Created Successfully!")
print("Vectors stored:", index.ntotal)

# Question
query = input("Ask a question: ")

# Search
query_embedding = embedding_model.encode([query])

distances, indices = index.search(
    np.array(query_embedding).astype("float32"),
    k=3
)

print("\nTop Matching Chunks:\n")

context = ""

for idx in indices[0]:
    print("-------------------")
    print(chunks[idx])
    context += chunks[idx] + "\n\n"

# RAG Prompt
prompt = f"""
Answer the question using ONLY the provided context.

If the answer is not found in the context, reply:
"The information is not available in the provided document."

Do not make up information.

Context:
{context}

Question:
{query}
"""

# Gemini API Call
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={GEMINI_API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

result = response.json()

print("\n========================")
print("FINAL ANSWER")
print("========================\n")

try:
    answer = result["candidates"][0]["content"]["parts"][0]["text"]
    print(answer)
except Exception:
    print(result)