# Binance Futures Testnet Trading Bot

A Python CLI application to place MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY / SELL Support
- Input Validation
- Logging
- Error Handling
- Binance Futures Testnet Integration
- CLI using Typer

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
├── main.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_SECRET_KEY
```

## MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## LIMIT Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Technologies

- Python
- python-binance
- Typer
- Rich
- python-dotenv
