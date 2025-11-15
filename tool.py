import json
from google.adk.tools import FunctionTool
# FIX: Correct import location for ToolContext
from google.adk.agents import ToolContext 
from google.genai import Client, types
# FIX: Correct import location for structured JSON config
from google.genai.types import GenerateContentConfig 

# Initialize the Gemini client 
client = Client()

# -----------------------------------------------------------
# 1. Structured Output Schema for Meal Plan
# -----------------------------------------------------------
MEAL_PLAN_SCHEMA = types.Schema(
    type=types.Type.ARRAY,
    description="A 7-day meal plan where each day includes a calorie summary and three main meals.",
    items=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "day": types.Schema(type=types.Type.STRING, description="The day of the week, e.g., Monday."),
            "target_calories": types.Schema(type=types.Type.INTEGER, description="The requested daily calorie target."),
            "total_estimated_calories": types.Schema(type=types.Type.INTEGER, description="The sum of calories for breakfast, lunch, and dinner."),
            "meals": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "type": types.Schema(type=types.Type.STRING, description="Meal type: Breakfast, Lunch, or Dinner."),
                        "name": types.Schema(type=types.Type.STRING, description="Name of the dish, e.g., 'High-Protein Scramble'."),
                        "calories": types.Schema(type=types.Type.INTEGER, description="Estimated calorie count for this meal."),
                        "main_ingredients": types.Schema(type=types.Type.STRING, description="List of main ingredients, e.g., '2 eggs, 50g spinach, 1 slice whole wheat bread'."),
                    },
                ),
            ),
        },
    ),
)


# -----------------------------------------------------------
# 2. Function Tool Definition
# -----------------------------------------------------------
def generate_meal_plan(calorie_goal: int, dietary_prefs: str) -> str:
    """
    Generates a structured, 7-day meal plan that strictly adheres to the provided
    daily calorie goal and dietary preferences using the Gemini model's JSON mode.

    Args:
        calorie_goal: The target daily calorie intake (e.g., 1800).
        dietary_prefs: Specific dietary constraints (e.g., 'vegetarian, no nuts, high protein').

    Returns:
        A JSON string containing the full 7-day meal chart.
    """
    system_instruction = (
        f"You are an expert nutritionist and meal prep chef. Your task is to generate a comprehensive 7-day meal plan. "
        f"The plan MUST strictly target {calorie_goal} calories per day. "
        f"You MUST adhere to the following dietary constraints: '{dietary_prefs}'. "
        "Each meal must include an estimated calorie count. Respond ONLY in the requested JSON schema."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Content(role="user", parts=[types.Part.from_text(
                    f"Create a 7-day meal plan based on a {calorie_goal} calorie target and these constraints: {dietary_prefs}.")]
                )
            ],
            config=GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MEAL_PLAN_SCHEMA,
                system_instruction=system_instruction
            )
        )
        return response.text
    except Exception as e:
        return json.dumps({"error": f"Failed to generate meal plan. Gemini API error: {e}"})

# Wrap the Python function as an ADK FunctionTool
MealPlannerTool = FunctionTool(func=generate_meal_plan)