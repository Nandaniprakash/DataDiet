from google.adk.agents import Agent
from google.adk.tools import google_search
# Import your custom tool from the tools.py file
from .tools import MealPlannerTool

# Define your root ADK agent (The variable the ADK looks for!)
root_agent = Agent(
    model="gemini-2.5-flash",
    name="DataDiet", 
    description="A personalized AI assistant that provides data-driven nutrition guidance and meal charts.",
    instruction=(
        "You are **DataDiet**, an AI designed to help users with data-driven nutrition and meal planning. "
        "1. For general health questions, use the 'google_search' tool to find reliable, up-to-date information. "
        "2. **IMPORTANT**: If the user asks for a meal plan, a diet chart, or calorie-based nutrition advice, "
        "you MUST use the 'generate_meal_plan' tool. Extract the required calorie goal and any dietary preferences."
        "3. Always start your response with a clear disclaimer: 'Disclaimer: I am DataDiet, an AI, and this information is for educational purposes only. Consult a healthcare professional before making diet changes.'"
    ),
    # Equip the agent with both capabilities
    tools=[google_search, MealPlannerTool],
)