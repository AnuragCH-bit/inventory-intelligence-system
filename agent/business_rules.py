def evaluate_inventory(inventory: dict):

    current_stock = inventory["current_stock"]
    reorder_point = inventory["reorder_point"]
    safety_stock = inventory["safety_stock"]

    if current_stock <= safety_stock:
        priority = "CRITICAL"

    elif current_stock <= reorder_point:
        priority = "HIGH"

    else:
        priority = "NORMAL"

    reorder_required = current_stock <= reorder_point

    return {
        "priority": priority,
        "reorder_required": reorder_required
    }