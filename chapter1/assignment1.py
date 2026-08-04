import json
def build_order_summary(items):
    line_items = []
    grand_total = 0.0
    most_expensive_item = None
    for item in items:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]
        line_total = round(price * quantity, 2)
        line_item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "line_total": line_total,
        }
        line_items.append(line_item)
        grand_total += line_total
        if most_expensive_item is None or line_total > most_expensive_item["line_total"]:
            most_expensive_item = line_item
    summary = {
        "line_items": line_items,
        "grand_total": round(grand_total, 2),
        "most_expensive_item": most_expensive_item,  # None for empty orders
        "item_count": len(line_items),
    }
    return summary
def order_summary_to_json(items, indent=2):
    """Build the order summary and serialize it to a JSON string."""
    summary = build_order_summary(items)
    return json.dumps(summary, indent=indent)
if __name__ == "__main__":
    sample_order = [
        {"name": "Widget A", "price": 9.99, "quantity": 3},
        {"name": "Widget B", "price": 24.50, "quantity": 1},
        {"name": "Widget C", "price": 5.00, "quantity": 10},
    ]
    print("Sample order")
    print(order_summary_to_json(sample_order))
    print("\nEmpty order")
    print(order_summary_to_json([]))
