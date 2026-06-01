import typer
from bots.client import client
from bots.balance import get_av_balance
from bots.orders import (
    place_market_order,
    place_limit_order
)
from bots.validation import validate_side, validate_order_type,validate_order

app = typer.Typer()
balance = get_av_balance(client)
'''
print("DEBUG|USDT balance:", balance)
info = client.futures_account_balance()
print("|DEBUG|")
for item in info:
    if item["asset"] == "USDT":
        print(item)'''
@app.command()
def order(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading symbol, e.g., BTCUSDT"),
    side: str = typer.Option(..., "--side", help="BUY or SELL"),
    order_type: str = typer.Option(..., "--order-type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Order quantity"),
    price: float = typer.Option(0.0, "--price", help="Price for LIMIT orders")
):

    try:
        symbol, side, order_type, quantity = validate_order(symbol,side,order_type,quantity)
        side = validate_side(side)
        order_type = validate_order_type(order_type)

        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            if price is None:
                raise ValueError(
                    "Price required for LIMIT orders"
                )

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\n=== ORDER SUCCESS ===")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app()