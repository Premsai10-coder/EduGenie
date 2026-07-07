import os
import google.generativeai as genai
from google.api_core import exceptions  # Imported to catch specific API errors

from dotenv import load_dotenv

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ----------------------------------------
# FastAPI App
# ----------------------------------------

app = FastAPI()

# ----------------------------------------
# Gemini API Configuration
# ----------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------------------
# Static Files & Templates
# ----------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# ----------------------------------------
# Chat History
# ----------------------------------------

history = []

# ----------------------------------------
# Home Page
# ----------------------------------------

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

# ----------------------------------------
# Ask EduGenie
# ----------------------------------------

@app.post("/ask")
def ask(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    prompt = f"""
You are EduGenie, an AI-powered Learning Assistant.

Task:
{task}

Instructions:
1. Explain in simple English.
2. Use proper headings.
3. Use bullet points.
4. Give one real-world example.
5. End with a short summary.

Student Question:
{question}
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            answer = response.text
        else:
            answer = "⚠️ No text response received from Gemini. The content might have been flagged or blocked."

    except exceptions.ResourceExhausted as e:
        print("Gemini Error: Rate limit or quota exceeded.", e)
        answer = """
⚠️ **Rate Limit Exceeded (Quota Blocked)**

EduGenie is resting for a moment! The free tier rate limit has been reached. 

**What to do:**
• Please wait 30–60 seconds and try submitting again.
• If you are the developer, check your [Google AI Studio Console](https://aistudio.google.com/) to see if your daily free tier tokens are fully exhausted.
"""

    except exceptions.InvalidArgument as e:
        print("Gemini Error: Invalid API key or configuration.", e)
        answer = "⚠️ **Configuration Error:** The API key provided seems invalid. Please check your `.env` file."

    except Exception as e:
        print("Gemini Error:", e)
        answer = f"""
⚠️ Unable to generate a response.

**Reason:**
{str(e)}

**Possible causes:**
• API quota fully exhausted
• Temporary internet connection issue
• Service disruption

Please try again in a few moments.
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

# ----------------------------------------
# Clear Chat
# ----------------------------------------

@app.get("/clear")
def clear():

    history.clear()

    return RedirectResponse(url="/", status_code=303)