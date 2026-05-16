# PDF RAG Chatbot

A conversational chatbot that answers questions about your PDF documents using Retrieval-Augmented Generation (RAG).

## How It Works

1. **Extract** — reads text from your PDF using PyMuPDF
2. **Chunk** — splits the text into 500-word overlapping pieces
3. **Embed** — converts chunks into TF-IDF vectors stored in memory
4. **Retrieve** — finds the top 3 most relevant chunks for your question
5. **Answer** — sends only those chunks to the LLM to generate a grounded answer

## Project Structure

```
pdf-rag-chatbot/
├── main.py              # Terminal chat loop
├── app.py               # Streamlit web UI
├── .env                 # API keys (never commit this)
├── requirements.txt     # Dependencies
├── src/
│   ├── extractor.py     # Step 1: Extract text from PDF
│   ├── chunker.py       # Step 2: Split text into chunks
│   ├── embedder.py      # Step 3: Build TF-IDF vectors
│   ├── retriever.py     # Step 4: Find relevant chunks
│   └── responder.py     # Step 5: Call LLM API
└── data/
    └── your_file.pdf    # Put your PDFs here (for terminal version)
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root folder:

```
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Get a free API key at [openrouter.ai](https://openrouter.ai)

### 4. Add your PDF

Place your PDF file inside the `data/` folder (for terminal version), or use the file uploader in the Streamlit UI.

## Usage

### Terminal version

```bash
python main.py
```

```
You: what is this document about?
Bot: This document is about...

You: quit
```

### Web UI version

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser, upload a PDF, and start chatting.

## Requirements

```
pymupdf
scikit-learn
numpy
python-dotenv
streamlit
openai
```

Install all at once:

```bash
pip install -r requirements.txt
```

## Configuration

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | Your OpenRouter API key |

## Model

This project uses `mistralai/mistral-7b-instruct` via OpenRouter. You can swap it for any other model by changing one line in `src/responder.py`:

```python
model="mistralai/mistral-7b-instruct"  # change this
```

Free models available on OpenRouter: [openrouter.ai/models?q=free](https://openrouter.ai/models?q=free)

## Limitations

- Vectors are stored in memory — reprocesses the PDF on every restart
- TF-IDF search is keyword-based, not semantic
- Best suited for PDFs under 50 pages

## Next Steps

- Swap TF-IDF for real embeddings (e.g. ChromaDB + sentence-transformers)
- Add persistent vector storage so PDFs are not reprocessed every time
- Support multiple PDFs at once

## License

MIT
