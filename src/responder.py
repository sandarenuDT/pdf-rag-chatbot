import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask(question, context_chunks):
    context = "\n\n---\n\n".join(context_chunks)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=(
            "You are a helpful assistant. "
            "Answer questions using ONLY the context provided. "
            "If the answer is not in the context, say 'I could not find that in the document'."
        ),
        messages=[{
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }]
    )
    return response.content[0].text