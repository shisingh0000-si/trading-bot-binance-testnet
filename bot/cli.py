from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
import typer
from rich import print

app = typer.Typer(help="Binance Futures Testnet Trading Bot")


@app.command()
def place_order(
    symbol: str = typer.Option(..., help="Trading symbol"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price for LIMIT order"),
):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        if order_type.upper() == "MARKET":
            result = place_market_order(symbol, side, quantity)
        else:
            result = place_limit_order(symbol, side, quantity, price)

        print("\n========== ORDER SUMMARY ==========")
        print(f"Order ID       : {result['orderId']}")
        print(f"Symbol         : {result['symbol']}")
        print(f"Side           : {result['side']}")
        print(f"Order Type     : {result['type']}")
        print(f"Status         : {result['status']}")
        print(f"Quantity       : {result['origQty']}")
        print(f"Executed Qty   : {result['executedQty']}")

        avg_price = result.get("avgPrice") or result.get("avgFillPrice") or "N/A"
        print(f"Average Price  : {avg_price}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        error = str(e)

        if "Order's notional must be no smaller than 50" in error:
            print("\n❌ LIMIT order value must be at least 50 USDT.")
        else:
            print(f"\n❌ Error: {error}")