import json
import subprocess
from agents.base_agent import BaseAgent
from system.state_manager import load_state, save_state


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("planner")

    def call_llama(self, prompt: str) -> str:
        """Call LLaMA via Ollama and return raw output."""
        result = subprocess.run(
            ["C:\\Users\\derri\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "llama3.1"],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()

    def run(self):
        print("[PlannerAgent] Generating project plan...")

        # Ask user for the high-level goal
        user_goal = input("Describe the project you want to build: ")

        # Prompt for the LLM
        prompt = f"""
You are an expert software architect AI.

The user wants to build the following project:

\"\"\"{user_goal}\"\"\"

Your job:
1. Break the project into clear, discrete engineering steps.
2. Return ONLY VALID JSON with this structure:

{{
  "project_name": "",
  "steps": [
    "step 1",
    "step 2",
    "step 3"
  ]
}}

NO explanation. NO extra text. ONLY VALID JSON.
"""

        # Call LLaMA
        raw_output = self.call_llama(prompt)

        # Try parsing JSON. If invalid, ask LLaMA to fix it.
        try:
            plan = json.loads(raw_output)
        except Exception:
            print("[PlannerAgent] Invalid JSON. Requesting correction...")
            corrected = self.call_llama(f"Fix this into VALID JSON ONLY:\n{raw_output}")
            plan = json.loads(corrected)

        # Show the generated plan
        print("\n--- PLAN GENERATED ---")
        print(json.dumps(plan, indent=4))

        # Save into project state
        state = load_state()
        state["project_name"] = plan.get("project_name", "")
        state["plan"] = plan
        state["status"] = "planned"
        save_state(state)

        return state
