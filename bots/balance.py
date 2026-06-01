import time
from binance.client import Client

def get_av_balance(client: Client, asset_symbol: str = "USDT") -> float:
    while True:
        try:
            account_info = client.futures_account()

            av_balance = next(
                (
                    float(asset["availableBalance"])
                    for asset in account_info["assets"]
                    if asset["asset"] == asset_symbol
                ),
                None,
            )

            if av_balance is None:
                raise ValueError(f"{asset_symbol} not found in futures account assets")

            return round(av_balance, 2)

        except Exception as e:
            print("Account Error:", e)
            time.sleep(1)