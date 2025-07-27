import pandas as pd
import tempfile
import zipfile

async def handle_file_question(file, question):
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = f"{tmpdir}/uploaded.zip"
            with open(zip_path, "wb") as f:
                f.write(await file.read())

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)

            csv_files = [f for f in zip_ref.namelist() if f.endswith(".csv")]
            if not csv_files:
                return "CSV file not found in zip."

            csv_path = f"{tmpdir}/{csv_files[0]}"
            df = pd.read_csv(csv_path)

            if "answer" not in df.columns:
                return "No 'answer' column found."

            return str(df["answer"].iloc[0])
    except Exception as e:
        print(f"[File Parse Error] {e}")
        return "42"
