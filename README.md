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

# Epic 3 - Build Web Interface

## Objective

Develop a responsive and user-friendly web interface for EduGenie using HTML, CSS, JavaScript, and Jinja2 templates.

## Features Completed

- Responsive HTML interface
- Welcome section for EduGenie
- Question Answering interface
- Concept Explanation interface
- Quiz Generation interface
- Text Summarization interface
- Learning Path interface
- Task selection dropdown
- User input form
- AI response display
- Chat history
- Dark Mode
- Clear Chat
- Copy Answer
- Download Notes
- Loading animation

## Technologies Used

- HTML5
- CSS3
- JavaScript
- FastAPI
- Jinja2 Templates

# Epic 3 - Live Integration

## Objective

Integrate the frontend interface with the FastAPI backend to enable real-time communication with Google Gemini AI.

## Features Completed

- Connected HTML forms with FastAPI
- POST request handling
- User input processing
- Google Gemini AI integration
- Dynamic response rendering
- Chat history management
- Error handling
- Jinja2 template rendering
- Static file support

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

# Epic 4 - Local Deployment and Functional Testing

## Objective

Deploy the EduGenie Learning Assistant in a local development environment and perform functional testing to verify that all AI-powered educational modules work correctly through the FastAPI backend.

---

## Run Locally

### Objective

Execute the EduGenie application using FastAPI and Uvicorn to enable local development, testing, and real-time interaction.

### Features Completed

- Configured FastAPI application for local execution
- Started the application using Uvicorn
- Enabled automatic server reload using the `--reload` option
- Successfully launched the local development server
- Verified frontend and backend connectivity
- Tested the application through a web browser
- Confirmed successful communication with the Google Gemini API

### Command Used

```bash
uvicorn app.main:app --reload
```

### Local Server URL

```
http://127.0.0.1:8000
```

---

## Functional Testing

### Objective

Verify that all educational modules perform correctly and produce accurate AI-generated responses under normal user interactions.

### Functional Tests Performed

- Question Answering
- Concept Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path
- Dark Mode
- Clear Chat
- Copy Answer
- Download Notes
- Chat History

### Test Results

| Module | Status |
|---------|--------|
| Question Answering | ✅ Passed |
| Concept Explanation | ✅ Passed |
| Quiz Generation | ✅ Passed |
| Text Summarization | ✅ Passed |
| Learning Path | ✅ Passed |
| Dark Mode | ✅ Passed |
| Copy Answer | ✅ Passed |
| Download Notes | ✅ Passed |
| Clear Chat | ✅ Passed |
| Chat History | ✅ Passed |

### Outcome

The EduGenie Learning Assistant was successfully executed in the local development environment. All frontend components communicated seamlessly with the FastAPI backend, and Google Gemini AI generated responses for each educational module. Functional testing confirmed that every feature operated correctly, providing a smooth and interactive learning experience.

# Conclusion

EduGenie is an AI-powered learning assistant developed to enhance the educational experience using Google Gemini AI. The project successfully integrates FastAPI, HTML, CSS, JavaScript, and Jinja2 templates to provide an interactive web application for students and self-learners.

The application offers intelligent educational features including Question Answering, Concept Explanation, Quiz Generation, Text Summarization, and Personalized Learning Recommendations. The frontend and backend were successfully integrated, allowing users to interact with the AI in real time through a clean and responsive interface.

The project was successfully tested in a local development environment using Uvicorn and FastAPI. Functional testing confirmed that all modules worked correctly and generated accurate AI-powered responses.

Overall, EduGenie demonstrates the practical application of Generative AI in education by providing personalized, interactive, and efficient learning support. The modular architecture also makes the project scalable and easy to maintain for future enhancements.