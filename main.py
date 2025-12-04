from agents.planner import PlannerAgent
from agents.router import RouterAgent
from agents.code_agent import CodeAgent

def main():
    print("=== AutoForge Initializing ===")

    router = RouterAgent()

    while True:
        next_agent = router.route()
        print(f"[Router] Next agent: {next_agent}")

        if next_agent == "planner":
            agent = PlannerAgent()
        elif next_agent == "code":
            agent = CodeAgent()
        else:
            print("No valid agent. Stopping.")
            break

        state = agent.run()

        if next_agent == "code":
            print("Reached code stage (empty for now). Stopping loop.")
            break

if __name__ == "__main__":
    main()
