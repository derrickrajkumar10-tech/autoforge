class BaseAgent:
    def __init__(self,name:str):
        self.name = name
    def run(self):
        raise NotImplementedError("run() must be implemented by agent subclasses")