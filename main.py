from dotenv import load_dotenv
load_dotenv()
from src.extractor import extract_text
from src.chunker import chunk_text
from src.embedder import build_vectors
from src.retriever import retrieve
from src.responder import ask

load_dotenv()

text = extract_text("data/file.pdf")
chunks = chunk_text(text)
vectorizer, vectors = build_vectors(chunks)

while True:
    question = input("\nYou: ")
    if question.lower() == "quit":
        break
    results = retrieve(question, chunks, vectorizer, vectors)
    print("\nBot:", ask(question, results))