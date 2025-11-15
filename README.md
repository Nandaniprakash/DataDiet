DataDiet: AI-Powered Personalized Nutrition Agent

Project Overview

DataDiet is a health-tech AI agent designed to provide highly personalized nutrition guidance and structured meal plans based on individual calorie goals and dietary restrictions. This project demonstrates a modern, production-ready AI architecture using Google's core generative AI and cloud tools.

Core Problem Solved

The project solves the challenge of generating structured, data-driven content from a conversational query. Instead of just answering with a paragraph, the agent uses its intelligence (Gemini) to execute a custom function to produce a machine-readable, week-long meal chart tailored precisely to the user's needs (e.g., 2000 calories, vegan, low-carb).

Technology Stack

This project is built around the three core requirements of the hackathon:

Component

Technology

Role in Project

Agent Core

Agent Development Kit (ADK) / Python

The framework that orchestrates the workflow, handles session management, and directs the LLM when to use its tools.

Intelligence

Gemini 2.5 Flash

The Large Language Model (LLM) serving as the agent's brain for reasoning, natural language understanding, and powerful JSON Structured Output.

Infrastructure

Google Cloud / Vertex AI

Used for local authentication (via ADC) and configured for future deployment as a scalable API on Cloud Run.

Development

Gemini CLI / ADK CLI

Command-line interfaces used for scaffolding the project, running the local development server, and debugging the agent's execution trace.

Architectural Flow: Tool-Calling Pattern

DataDiet operates using the advanced "Tool-Calling" pattern, where the LLM is instructed to call a specific Python function (generate_meal_plan) when a user's intent is clear.

User Input: User asks a complex question ("Give me a 2000 calorie plan, high protein").

LLM Reasoning (agent.py): The Gemini model identifies the intent (MealPlan) and extracts the required parameters (2000, high-protein).

Tool Call: The ADK framework pauses the LLM and calls the Python function generate_meal_plan.

Structured Generation (tools.py): The Python function calls the Gemini API again, but this time, it enforces a strict JSON Schema to ensure the 7-day meal plan is returned in a predictable format.

Final Response: The ADK presents the clean, structured JSON output back to the user.

Project Structure

The final working structure of the Python project:

datadiet-final-project/
├── .venv/                      # Python Virtual Environment
├── .env                        # Stores GOOGLE_API_KEY for local testing
├── data_diet_agent/            # The ADK Agent Module (Python Package)
│   ├── _init_.py             # Imports root_agent for module loading
│   ├── agent.py                # Defines the DataDiet agent (Persona, Instructions, Tools)
│   └── tools.py                # Contains the custom Python function (MealPlannerTool)
└── README.md                   # This file


How to Run the Agent (Local Testing)

Follow these steps to run the agent locally and verify the functionality using the ADK Dev UI.

Prerequisites

Python 3.9+ installed.

VS Code installed.

A Gemini API Key.

Google Cloud CLI installed (needed for secure authentication).

Execution Steps

Activate Environment: Navigate to the root directory and activate the virtual environment:

.\.venv\Scripts\Activate.ps1  # Windows PowerShell


Ensure Authentication (CRITICAL): Run the following command to set the Application Default Credentials (ADC), which is the most reliable authentication method for the ADK.

# This command requires the gcloud CLI to be in your system PATH and will open a browser for login.
gcloud auth application-default login


Start the ADK Web Server: Run the agent on a safe port.

adk web --port 8001


Access the UI: While the server is running, open your web browser and navigate to the correct URL:

http://localhost:8001/dev-ui/?app=data_diet_agent


Test Query

Input the following query to trigger the custom tool and validate the project's core logic:

"I need a 2000 calorie plan for a week. I want a high-protein, low-carb diet."

Future Development

This project is ready for immediate deployment and scaling:

Deployment to Cloud Run: The next step is containerizing the project (using a Dockerfile) and deploying it to Google Cloud Run to provide a public, scalable API endpoint.

Frontend App: Develop a dedicated mobile (Android/iOS) or web frontend that calls the deployed API to display the structured meal plan data in a visually appealing dashboard.

Advanced Personalization: Integrate Google Cloud Firestore to store user history and allergies, allowing the agent to provide ongoing, personalized coaching and track dietary adherence over time.
