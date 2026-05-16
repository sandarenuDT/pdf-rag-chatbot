from dotenv import load_dotenv
load_dotenv()

import os
from src.extractor import extract_text
from src.chunker import chunk_text
from src.embedder import build_vectors
from src.retriever import retrieve
from src.responder import ask

print("\n📄 PDF RAG Chatbot")
print("------------------")

# Ask user for PDF path
while True:
    pdf_path = input("\nEnter path to your PDF file: ").strip()
    
    if not pdf_path:
        print("Please enter a path.")
        continue
    
    # Remove surrounding quotes if user dragged and dropped file
    pdf_path = pdf_path.strip('"').strip("'")
    
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue
    
    if not pdf_path.lower().endswith(".pdf"):
        print("Please provide a .pdf file.")
        continue
    
    break

# Process the PDF
print(f"\nReading {os.path.basename(pdf_path)}...")
text = extract_text(pdf_path)
print("Chunking text...")
chunks = chunk_text(text)
print("Building vectors...")
vectorizer, vectors = build_vectors(chunks)
print(f"✅ Ready! {len(chunks)} chunks indexed.")
print("\nType your questions below. Type 'quit' to exit or 'new' to load a different PDF.\n")

# Chat loop
while True:
    question = input("You: ").strip()

    if not question:
        continue

    if question.lower() == "quit":
        print("Goodbye!")
        break

    if question.lower() == "new":
        # Restart the whole script
        import subprocess, sys
        subprocess.run([sys.executable] + sys.argv)
        break

    results = retrieve(question, chunks, vectorizer, vectors)
    print("\nBot:", ask(question, results), "\n")