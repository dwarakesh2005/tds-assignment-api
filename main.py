from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from utils.llm_handler import handle_llm_question
from utils.file_parser import handle_file_question

app = FastAPI()

@app.post("/api/")
async def solve_question(question: str = Form(...), file: UploadFile = File(None)):
    try:
        if file:
            return {"answer": await handle_file_question(file, question)}
        else:
            return {"answer": await handle_llm_question(question)}
    except Exception as e:
        return JSONResponse(content={"answer": f"Error: {str(e)}"}, status_code=500)
