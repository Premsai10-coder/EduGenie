import google.generativeai as genai

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# -----------------------------
# FastAPI App
# -----------------------------

app = FastAPI()

# -----------------------------
# Gemini API Configuration
# -----------------------------

genai.configure(api_key="AQ.Ab8RN6KG7aO-zjcbs6FLIpKHKoKbM2TJOlwYaRnWt_dibV4LhA")

model = genai.GenerativeModel("gemini-2.0-flash")

# -----------------------------
# Static & Templates
# -----------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# -----------------------------
# Chat History
# -----------------------------

history = []

# -----------------------------
# Home Page
# -----------------------------

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

# -----------------------------
# Ask EduGenie
# -----------------------------

from fastapi import Form

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
6. Keep the answer neat.
7. Don't use difficult words.

Student Question:

{question}
"""

        response = model.generate_content(prompt)

        answer = response.text

    except Exception:

        answer = """
⚠️ Gemini API quota exceeded or AI service is unavailable.

Please try again after some time.

If the problem continues, use another API key.
"""

    # Save Chat

    history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "task": task,
            "question": question,
            "answer": answer,
            "history": history
        }
    )

# -----------------------------
# Clear Chat
# -----------------------------

from fastapi.responses import RedirectResponse

@app.get("/clear")
def clear():
    history.clear()
    return RedirectResponse(url="/", status_code=303)