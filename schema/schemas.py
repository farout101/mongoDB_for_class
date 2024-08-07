def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }
    
def lsist_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]