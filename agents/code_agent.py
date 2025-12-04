from agents.base_agent import BaseAgent

class CodeAgent(BaseAgent):
    def __init__(self):
        super().__init__("code")

    def run(self):
        print("[CodeAgent] Running code agent...")
        print("Reached code stage (empty for now). Stopping loop.")
        return {}
