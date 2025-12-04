from agents.base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("evaluator")

    def run(self):
        print("[EvaluatorAgent] Running evaluator agent...")
        return {}
