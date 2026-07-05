# 🎓 EduGenie

EduGenie is an AI-powered learning assistant built using FastAPI and Google Gemini API.

## Features
- 🤖 AI Question Answering
- 📚 Concept Explanation
- 📝 Quiz Generation
- 📄 Summarization
- 🛤 Learning Path Suggestions
- 🌙 Dark Mode
- 📋 Copy Answer
- ⬇ Download Notes
- 🗑 Clear Chat

## Technologies Used
- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript

## Installation

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

## Author

**Bora Prem Sai**



## Epic 1 - Model Selection and Architecture

### Objective
Set up the EduGenie AI learning assistant using FastAPI and Google Gemini.

### Features Completed
- FastAPI project setup
- Google Gemini API integration
- Question & Answer module
- Learning Path module
- Quiz module
- Summary module
- HTML Templates
- Static files support
- Environment variable configuration using .env

### Technologies Used
- Python
- FastAPI
- Google Gemini API
- Jinja2
- HTML/CSS

# Epic 2 - Module Implementation

## Objective

Implement the core AI learning modules of EduGenie to provide different learning services using Google Gemini AI.

## Modules Implemented

- Question Answering Module
- Concept Explanation Module
- Quiz Generation Module
- Summarization Module
- Learning Path Module

## Features Completed

- Created separate Python modules for each learning task.
- Integrated all modules with Google Gemini AI.
- Improved code organization using modular architecture.
- Connected frontend with backend modules.
- Implemented AI response generation for each selected task.
- Added exception handling for API errors.

## Technologies Used

- Python
- Google Gemini API
- FastAPI

# Backend API with FastAPI

## Objective

Develop a FastAPI backend to process user requests, communicate with Google Gemini AI, and manage chat interactions.

## Backend Features Completed

- FastAPI application setup
- Google Gemini API integration
- POST API endpoint for processing user questions
- GET API endpoint for homepage
- Dynamic Jinja2 template rendering
- Static files configuration
- Chat history management
- Clear Chat endpoint
- Environment variable support using `.env`
- Exception handling for API errors

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Load EduGenie homepage |
| POST | `/ask` | Process user questions |
| GET | `/clear` | Clear chat history |

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- Jinja2 Templates
- HTML
- CSS
- JavaScript
- python-dotenv