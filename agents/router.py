from system.state_manager import load_state

class RouterAgent:
    def _init_(self):
        print("[Router] Initialized router")
    def route(self):
        state = load_state()
        status = state.get("status",None)
        if status is None:
            return "planner"
        if status == "planned":
            return "code"
        
        return "planner"