import openai

# AI Proxy credentials (hardcoded — for development only)
openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDE5MTVAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.acO3-kXAgc-Q7TWfcThE2JLAsU81PDdvS6iIBfu7ELo"
openai.api_base = "https://aiproxy.sanand.workers.dev/openai"

async def handle_llm_question(question: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[LLM Error] {e}")
        return "42"  # fallback default
