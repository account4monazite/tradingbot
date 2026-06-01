# Trading Bot

Simple Binance Futures order CLI using `typer` and `python-binance`.

## Features

- Place market or limit futures orders via command line
- Validates order side, order type, and quantity
- Logs order results and failures to `logs/trading.log`
- Uses Binance API credentials from `.env`

## Requirements

- Python 3.11+ (or compatible)
- `python-binance`
- `typer`
- `python-dotenv`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Setup

Create a `.env` file in the project root with your Binance API credentials:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

The project currently points to the Binance Futures testnet in `bots/client.py`.

## Usage

Run commands from the project root:

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

For a limit order:

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 60000
```

## Logging

Order activity is logged to:

- `logs/trading.log`

The log file is created automatically when the CLI runs.

## Project structure

- `cli.py` - command-line interface and order entry point
- `bots/client.py` - Binance client configuration
- `bots/orders.py` - order placement functions
- `bots/validation.py` - input validation helpers
- `bots/logging.py` - logger setup
- `bots/balance.py` - account balance helper

## Notes

- The CLI currently uses `typer` options instead of explicit subcommands.
- If you encounter Binance API errors, check symbol filters, quantity precision, and testnet setup.
