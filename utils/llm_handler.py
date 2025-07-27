import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def handle_llm_question(question: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content.strip()
    except:
        return "42"  # Fallback default for now
