def validate_side(side: str):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    return order_type

# validators.py

def validate_order(
    symbol:str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
):
    side = side.upper()
    order_type = order_type.upper()

    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if price <= 0:
            raise ValueError("Price must be greater than 0")
    return symbol, side, order_type, quantity