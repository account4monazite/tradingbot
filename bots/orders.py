from .client import client

def place_market_order(symbol, side, quantity):

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )


def place_limit_order(symbol, side, quantity, price):

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )