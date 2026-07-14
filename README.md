# A2UI Financial Assistant

An AI-powered financial advisory assistant that uses a multi-agent architecture to generate dynamic A2UI JSON, which is rendered as interactive React components.

The project demonstrates how LLMs can decide the appropriate user interface based on user intent instead of returning plain text responses.

---

# 🚀 Tech Stack

## Backend

- Python
- FastAPI
- OpenRouter
- OpenAI Python SDK
- Pydantic

## Frontend

- React
- TypeScript
- Tailwind CSS

---

# 🏗️ Architecture

```
User
   │
   ▼
Intent Agent
   │
   ▼
Research Agent
   │
   ▼
UI Generator Agent
   │
   ▼
A2UI JSON
   │
   ▼
React Renderer
```

---

# 🤖 Multi-Agent Pipeline

### Intent Agent

Responsible for understanding the user's request.

Example:

```
Compare Apple and Microsoft
```

↓

```
COMPARE
```

---

### Research Agent

Determines what information is required to answer the request.

Example:

```
Collect

- Company Overview
- Revenue
- Market Capitalization
- Net Profit
- P/E Ratio
- Earnings Growth
```

---

### UI Generator Agent

Uses the user query, detected intent, and research plan to generate structured A2UI JSON.

Example Output:

- Comparison Cards
- Forms
- Data Tables
- Recommendation Cards

---

# 🎨 Supported A2UI Components

- Container
- Card
- Text
- Form
- TextField
- Button
- DataTable
- Badge
- Chart

---

# ✨ Features

- Multi-Agent AI Pipeline
- Real OpenRouter LLM Integration
- Dynamic Intent Classification
- Dynamic Research Planning
- AI Generated A2UI JSON
- Structured JSON Validation
- Modular Agent Architecture
- Clean Prompt Engineering

---

# 🚧 Current Status

## ✅ Completed

- FastAPI Backend
- OpenRouter Integration
- Intent Agent
- Research Agent
- UI Generator Agent
- Financial Assistant Service
- Structured A2UI JSON Generation

## 🚀 In Progress

- React A2UI Renderer
- Recursive Component Rendering
- Conversation Memory
- Streaming Responses

## 📅 Planned

- Validator + Retry Agent
- Redis Conversation Memory
- Tool Calling
- Portfolio Recommendation Engine
- Stock Data Integration

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   │   ├── intent_agent.py
│   │   ├── research_agent.py
│   │   └── ui_generator_agent.py
│   │
│   ├── models/
│   ├── services/
│   ├── main.py
│   └── ...
│
└── requirements.txt
```

---

# 📌 Example Flow

User:

```
Compare Apple and Microsoft
```

↓

Intent Agent

```
COMPARE
```

↓

Research Agent

```
Company Overview
Revenue
Market Capitalization
PE Ratio
...
```

↓

UI Generator

```json
{
  "type": "container",
  "children": [
    {
      "type": "card",
      "title": "Apple vs Microsoft"
    }
  ]
}
```

↓

React renders the UI dynamically.

---

# 🎯 Project Goal

Instead of returning plain text, the AI generates structured A2UI JSON describing the interface. The frontend interprets this JSON and renders a fully interactive user experience.

---

# 📝 Future Improvements

- Conversation Memory
- Streaming Responses
- Validator + Retry Loop
- Tool Calling
- Live Financial Data Integration
- Model Fallback
- Token Usage Tracking