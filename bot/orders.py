from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    client = get_client()

    logger.info(
        f"MARKET Order Request | Symbol={symbol}, Side={side}, Qty={quantity}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side.upper(),
        type="MARKET",
        quantity=quantity,
    )

    logger.info(f"MARKET Order Response | {response}")

    return response


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    logger.info(
        f"LIMIT Order Request | Symbol={symbol}, Side={side}, Qty={quantity}, Price={price}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side.upper(),
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price,
    )

    logger.info(f"LIMIT Order Response | {response}")

    return response