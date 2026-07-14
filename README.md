# A2UI Financial Assistant

An AI-powered financial advisory assistant built using a multi-agent architecture, FastAPI, React, and TypeScript. Instead of returning plain text, the assistant generates structured **A2UI JSON**, which is rendered dynamically into interactive React components.

The application demonstrates how Large Language Models can drive user interfaces through declarative UI generation while maintaining conversation context, validating outputs, handling streaming responses, and gracefully recovering from malformed responses.

---

# Features

- Multi-Agent Architecture
- Real LLM Integration (Google Gemini)
- Dynamic A2UI JSON Rendering
- Recursive React Renderer
- Conversation Memory
- Streaming Responses using Server-Sent Events (SSE)
- Validator + Retry Pipeline
- Graceful Fallback UI
- Controlled Form Components
- Fully Typed Backend (Pydantic)
- Fully Typed Frontend (TypeScript)

---

# Architecture

```

                    User

                      │

                      ▼

             React + TypeScript

                      │

              Server Sent Events

                      │

                      ▼

                FastAPI Backend

                      │

                      ▼

          Financial Assistant Service

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

Intent Agent     Research Agent    UI Generator Agent

      │                               │

      └───────────────┬───────────────┘

                      ▼

             Validator Agent

                      │

          ┌───────────┴────────────┐

          ▼                        ▼

     Valid UI                 Retry Generation

                                   │

                              Retry Failed

                                   │

                                   ▼

                             Fallback UI

                                   │

                                   ▼

                           React Renderer

```

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Google Gemini API
- Server Sent Events (SSE)

## Frontend

- React
- TypeScript
- CSS

## AI

- Google Gemini
- Prompt Engineering
- Multi-Agent Architecture
- A2UI JSON Rendering

---

# Folder Structure

```

backend/

│

├── agents/

│ ├── intent_agent.py

│ ├── research_agent.py

│ ├── ui_generator_agent.py

│ └── validator_agent.py

│

├── prompts/

│

├── services/

│ ├── conversation_manager.py

│ ├── financial_assistant_service.py

│ └── llm_service.py

│

├── models/

│

└── utils/

frontend/

│

├── components/

├── api/

├── styles/

├── types/

└── App.tsx

```

---

# Multi-Agent Pipeline

The assistant follows a specialised multi-agent architecture where each agent has a single responsibility.

## 1. Intent Agent

Responsible for identifying the user's intent.

Example:

```

Compare RELIANCE and TCS

```

↓

```

COMPARE

```

or

```

Help me rebalance my portfolio

```

↓

```

ALLOCATE

```

---

## 2. Research Agent

Based on the detected intent, this agent prepares a structured research plan for the UI generation agent.

Instead of directly generating UI, it creates contextual information describing what should be presented.

---

## 3. UI Generator Agent

Generates A2UI-compliant JSON using the research plan and conversation context.

The output is parsed into structured JSON and rendered dynamically by the frontend.

---

## 4. Validator Agent

Every generated UI is validated before reaching the frontend.

Validation includes checking:

- Supported component types
- Parent-child hierarchy
- Root container
- Recursive component validation

If validation fails:

1. Retry UI generation once
2. If retry fails, return a fallback UI

---

# Conversation Memory

The application maintains conversation history using a dedicated `ConversationManager`.

Every interaction stores:

- User messages
- Assistant responses

This enables the assistant to understand follow-up questions and generate personalised interfaces across multiple turns.

Example:

```

User:

Compare RELIANCE and TCS

↓

User:

I want to invest ₹50,000

```

The assistant can use previous conversation context while generating the recommendation.

---

# Streaming

The backend streams progress updates using **Server-Sent Events (SSE)**.

Pipeline:

```

Detecting Intent

↓

Planning Research

↓

Generating UI

↓

Validating UI

↓

Render Response

```

The frontend displays live progress updates while waiting for the final UI response, making the interaction feel responsive and AI-driven.

---

# Dynamic A2UI Renderer

The frontend recursively renders UI components from AI-generated JSON.

Supported components:

- Container
- Card
- Text
- Form
- Text Field
- Button
- Badge
- Data Table
- Chart

Each component is independently reusable and supports nested composition.

---

# Demo Flows

## 1. Company Comparison

```

Compare RELIANCE and TCS

```

↓

Comparison Card

↓

Dynamic Data Table

---

## 2. Portfolio Rebalancing

```

Help me rebalance my portfolio

```

↓

Dynamic Form

↓

Collect investment preferences

---

## 3. Investment Recommendation

User submits:

- Amount
- Risk
- Investment Horizon

↓

Recommendation Card

↓

Badge

↓

Allocation Summary

↓

Chart

---

# Running the Project

## Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash
```

---

# Engineering Decisions

- Chose a multi-agent architecture instead of a single prompt to separate responsibilities and improve maintainability.
- Used conversation memory to support multi-turn interactions and personalised recommendations.
- Implemented recursive validation to prevent malformed A2UI JSON from reaching the frontend.
- Added a retry mechanism before falling back to a default UI for improved robustness.
- Used recursive React rendering to support arbitrary nested UI structures generated by the LLM.
- Implemented streaming with Server-Sent Events to improve perceived responsiveness.

---

# Challenges & Fixes

## Challenge

LLM occasionally returned malformed JSON.

### Solution

Added a validator with retry and fallback UI.

---

## Challenge

Maintaining conversation context across multiple requests.

### Solution

Implemented a dedicated Conversation Manager that stores user and assistant messages.

---

## Challenge

Rendering arbitrary nested UI structures.

### Solution

Built a recursive React renderer capable of rendering nested A2UI components.

---

# Future Improvements

- Tool calling for real-time financial data
- Token usage monitoring
- Model fallback across multiple providers
- Real chart rendering using Recharts
- Persistent conversation storage using Redis or PostgreSQL
- User authentication and saved conversations

---

# Screenshots

Add screenshots demonstrating:

- Company Comparison
- Portfolio Form
- Recommendation Card
- Streaming Progress
