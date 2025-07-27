import os, zipfile, pandas as pd
from io import BytesIO

async def handle_file_question(file, question: str) -> str:
    contents = await file.read()

    if file.filename.endswith('.zip'):
        with zipfile.ZipFile(BytesIO(contents), 'r') as zip_ref:
            for name in zip_ref.namelist():
                if name.endswith('.csv'):
                    df = pd.read_csv(zip_ref.open(name))
                    if "answer" in df.columns:
                        return str(df["answer"].iloc[0])
        return "Could not find answer column in ZIP"
    
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(contents))
        if "answer" in df.columns:
            return str(df["answer"].iloc[0])
        return "No 'answer' column found."

    elif file.filename.endswith('.txt'):
        return contents.decode()

    return "Unsupported file type"
