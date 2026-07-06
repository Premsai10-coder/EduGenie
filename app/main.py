import os
import google.generativeai as genai

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Static & Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Chat History
history = []

# ---------------- Home ----------------

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "history": history
        }
    )

# ---------------- Ask ----------------

@app.post("/ask")
def ask(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    try:

        prompt = f"""
You are EduGenie, an AI Learning Assistant.

Learning Task:
{task}

Rules:
1. Explain in simple English.
2. Use headings.
3. Use bullet points.
4. Give one real-life example.
5. End with a short summary.

Student Question:

{question}
"""

        response = model.generate_content(prompt)

        answer = response.text

    except Exception as e:

        print(e)

        answer = """
⚠️ Gemini API quota exceeded.

Please try again later or use a new Gemini API key.
"""

    history.append({
        "question": question,
        "answer": answer
    })

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "history": history
        }
    )

# ---------------- Clear ----------------

@app.get("/clear")
def clear():

    history.clear()

    return RedirectResponse("/", status_code=303)
