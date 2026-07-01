VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_order(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("LIMIT order requires a valid price.")

    return True