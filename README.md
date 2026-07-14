# A2UI Financial Assistant

An AI-powered financial assistant that uses multiple AI agents to understand user requests and dynamically generate user interfaces using the A2UI specification.

---

## 🚀 Tech Stack

### Backend
- Python 3.14
- FastAPI
- OpenRouter
- Google Gemini
- Pydantic

### Frontend *(Upcoming)*
- React
- TypeScript
- Tailwind CSS

---

## 🏗️ Architecture

```
User
   │
   ▼
FastAPI
   │
   ▼
Intent Agent
   │
   ▼
LLM Service
   │
   ▼
OpenRouter
   │
   ▼
Gemini
```

---

## ✨ Features

### ✅ Completed

- FastAPI backend
- REST API endpoints
- OpenRouter LLM integration
- Gemini model support
- Prompt-based AI architecture
- Intent Classification Agent
- Pydantic response validation
- Modular LLM Service

### 🚧 In Progress

- Research Agent
- Conversation Memory
- A2UI JSON Generator
- React Renderer
- Streaming Responses

### 📅 Planned

- Financial Research Agent
- Dynamic UI Generation
- Conversation Persistence
- Token Usage Monitoring
- Investment Assistant Workflows

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── requirements.txt
└── .env.example
```

---

## 📈 Development Progress

- ✅ Project Setup
- ✅ FastAPI Configuration
- ✅ Chat API
- ✅ OpenRouter Integration
- ✅ Intent Agent
- ⏳ Research Agent
- ⏳ Conversation Manager
- ⏳ A2UI Generator
- ⏳ React Frontend

---

## 🎯 Goal

Build an AI-powered financial assistant that understands user intent, performs financial reasoning using specialized AI agents, and dynamically renders user interfaces using the A2UI specification.

---

## 👨‍💻 Current Status

**Milestone 5 Completed ✅**

The project can now:

- Accept user requests
- Classify user intent using an AI Agent
- Validate responses with Pydantic
- Use a shared LLM Service for AI communication

The next milestone is implementing the **Research Agent**, which will analyze the user's request and gather the required financial context before generating the UI.