Enterprise RAG Assistant
A Retrieval-Augmented Generation (RAG) application that answers questions from PDF documents using semantic search and Gemini.

Features
PDF document ingestion
Text chunking
Sentence embeddings using Sentence Transformers
FAISS vector database
Semantic search
Gemini-powered answer generation
Interactive question answering
Tech Stack
Python
PyPDF
Sentence Transformers
FAISS
Gemini API
Requests
Architecture
Document PDF ↓ Text Extraction ↓ Chunking ↓ Embeddings ↓ FAISS Vector Store ↓ Semantic Search ↓ Retrieved Context ↓ Gemini ↓ Final Answer

Project Structure
enterprise-rag-assistant/
│
├── app.py
├── config.py
├── data/
├── requirements.txt
├── README.md
└── .gitignore
Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Run
python app.py
Example Question
What is OneFS?
Future Enhancements
Support multiple PDFs
Flask API
Web UI
Metadata filtering
Source citation support