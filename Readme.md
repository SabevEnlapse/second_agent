NovaTech AI Agent – Tool-Calling Lab (Velocity GPT)
Overview

This project implements a production-style AI agent that can:

Answer product pricing and feature questions from a product catalog

Decide when to call a backend tool (getOrderStatus)

Combine tool results with product knowledge into a final response

Operate using a Velocity-hosted GPT model via an OpenAI-compatible API

The agent follows a deterministic JSON protocol to demonstrate how real-world AI agents reason, choose tools, and generate responses.

Project Structure
second_agent/
│
├── agent.py          # Main agent loop and LLM interaction
├── tools.py          # Custom backend tool (order status)
├── products.json     # Product catalog (pricing & plans)
├── prompt.txt        # System instructions for the agent
├── .env              # Environment variables (API key, model, etc.)
├── README.md         # This file
└── __pycache__/      # Python cache (auto-generated)

Requirements

Python 3.9+ (recommended 3.10+)

Internet access to https://chat.velocity.online

Valid Velocity API key

Python Packages

Install dependencies:

pip install requests python-dotenv

Environment Configuration

Create a file named .env in the project root:

VELOCITY_API_KEY=sk-xxxxxxxxxxxxxxxx
VELOCITY_BASE_URL=https://chat.velocity.online/api
VELOCITY_MODEL=openai.openai/gpt-5.1
VELOCITY_TEMPERATURE=0.2
VELOCITY_TIMEOUT=60


⚠️ Never commit .env files with real API keys to version control.

How the Agent Works
1. System Initialization

Loads system instructions from prompt.txt

Loads product data from products.json

Injects both into the conversation context

2. User Input

User types a question (pricing, order status, or both)

3. Model Decision

The model must respond in JSON:

Tool request

{
  "action": "tool",
  "tool": "getOrderStatus",
  "order_id": "12345"
}


Direct response

{
  "action": "response",
  "message": "The Pro plan costs $1299 per month."
}

4. Tool Execution (if needed)

getOrderStatus(order_id) is executed locally

Tool result is injected back into the conversation

5. Final Answer

The model produces a user-facing response combining all information

Running the Agent

From the project directory:

python agent.py


You should see:

NovaTech Agent (Production-Style Lab)
Type 'exit' to quit

Example Test Questions
Product-only
What's the price of the Pro model?

Tool-only
What's the status of order #12345?

Mixed (Product + Tool)
What's the price of the Pro model, and what's the status of order #12345?

Comparison
Compare the Basic and Pro plans

Example Output
Agent: The NovaTech Pro plan costs $1,299 per month. 
Your order #12345 has been shipped via DHL and is expected to arrive on 2025-03-18.

Tool: getOrderStatus

Located in tools.py.

Purpose

Simulates a real order management system (OMS).

Example Return
{
  "order_id": "12345",
  "status": "Shipped",
  "carrier": "DHL",
  "tracking_number": "DHL-88439201",
  "estimated_delivery": "2025-03-18"
}

Design Principles Demonstrated

✅ Deterministic JSON-based agent decisions

✅ Explicit tool calling (no hallucinated data)

✅ Clear separation of concerns (LLM vs tools)

✅ Realistic enterprise prompt engineering

✅ Exam-ready debugging and reasoning flow

Common Issues & Fixes
AttributeError: NoneType has no attribute 'rstrip'

➡️ Missing environment variable
✔️ Ensure .env is loaded and variables are set

FileNotFoundError: prompt.txt

➡️ File name mismatch
✔️ Ensure file is named exactly prompt.txt

HTTP 405 / 404

➡️ Wrong endpoint
✔️ Use https://chat.velocity.online/api/chat/completions

Learning Outcomes (Exam Alignment)

This lab demonstrates:

Agent instruction design

Tool orchestration

Multi-step reasoning

Debugging agent runs

Production-style AI workflows

Next Improvements (Optional)

Add multiple tools

Persist conversation history

Add logging of agent decisions

Convert to Assistants / Threads architecture

Add automated test cases

License

Educational / internal use only.