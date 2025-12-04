#reading and writing to the project_state.json file
import json
def load_state():
    with open("system/project_state_.json","r") as file:
        t = file.read().strip()
        if (len(t)==0):
            return {}
        else:
            state_dict = json.loads (t)
            return state_dict

def save_state(state_dict):
    json_s = json.dumps(state_dict,indent=4)
    with open("system/project_state_.json","w") as f:
        f.write(json_s)
    


    
