from argparse import ArgumentParser
from argparse import Namespace

import requests

from . import Output
from . import Plugin


class CMCPrices(Plugin):
    def _update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("symbols_ids", type=int, nargs="+")
        parser.add_argument("-c", "--convert", type=str, metavar="str", default="USD")

    def _make_output(self, args: Namespace) -> Output:
        res = requests.post(
            "https://portal-api.coinmarketcap.com/v1/watchlist/ids",
            json={
                "ids": args.symbols_ids,
                "convert": args.convert,
                "include_untracked": False,
            },
        )
        data = res.json()

        green, red = "#a3be8c", "#bf616a"

        prices_change_info = []
        for i in data["watchlist"]:
            symbol = i["symbol"]
            price = i["quote"][args.convert]["price"]
            change_1h = i["quote"][args.convert]["percent_change_1h"]
            change_1h_color = green if change_1h > 0 else red
            change_24h = i["quote"][args.convert]["percent_change_24h"]
            change_24h_color = green if change_24h > 0 else red
            change_7d = i["quote"][args.convert]["percent_change_7d"]
            change_7d_color = green if change_7d > 0 else red
            prices_change_info.append(
                f"{symbol}: {price:.2f}"
                f" (<span fgcolor='{change_1h_color}'>{change_1h:+.2f}%</span>"
                f", <span fgcolor='{change_24h_color}'>{change_24h:+.2f}%</span>"
                f", <span fgcolor='{change_7d_color}'>{change_7d:+.2f}%</span>)"
            )

        icon = "\uf51e"  # fontawesome icon "coins"
        txt = "CoinMarketCap"
        txtclick = "xdg-open https://coinmarketcap.com/watchlist/"
        tool = "\n".join(prices_change_info)
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = CMCPrices()
    print(plugin.execute())


if __name__ == "__main__":
    main()
