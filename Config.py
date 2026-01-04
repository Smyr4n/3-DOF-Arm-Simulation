import json

def Read_Config(dir):
    """
    Reads the given Config.json file and returns its DH parameters.
    """

    try:
        with open(dir, 'r') as file:
            data = json.load(file)
        
        d = data["d"]
        a = data["a"]
        alpha = data["alpha"]
    
    except Exception as E:
        print(f"ERROR: {E}")
        d = [0, 1, 1]
        a = [0, 2, 2]
        alpha = [1.57, 0, 0]

    return d, a, alpha