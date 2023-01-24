import yaml

def validate_keys(data):
    required_keys = ["First Name", "Last Name", "Gender", "Tags"]
    missing_keys = []
    for key in required_keys:
        if key not in data.keys():
            missing_keys.append(key)
    if len(missing_keys) > 0:
        print("The following keys are missing: ", missing_keys)
    else:
        print("All required keys are present.")
        
def validate_values(data):
    missing_values = {}
    for key, value in data.items():
        if not value:
            missing_values[key] = "Value is missing"
    if len(missing_values) > 0:
        print("The following values are missing: ", missing_values)
    else:
        print("All values are present.")
        
with open("data.yaml", 'r') as x:
    data = yaml.safe_load(x)

for x in data:
    validate_keys(x)
    validate_values(x)
