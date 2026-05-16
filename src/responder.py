import os
from openai import OpenAI

def ask(question, context_chunks):
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    context = "\n\n---\n\n".join(context_chunks)

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer using ONLY the context provided. If the answer is not in the context, say 'I could not find that in the document'."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content