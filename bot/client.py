import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


def get_client():
    client = Client(API_KEY, API_SECRET)

    # Binance Futures Testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client