from agents.base_agent import BaseAgent

class TestAgent(BaseAgent):
    def __init__(self):
        super().__init__("test")

    def run(self):
        print("[TestAgent] Running test agent...")
        return {}
