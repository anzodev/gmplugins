from argparse import ArgumentParser
from argparse import Namespace

import requests

from . import Output
from . import Plugin


class Weather(Plugin):
    def _update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("city", type=str)

    def _make_output(self, args: Namespace) -> Output:
        res = requests.get(f"http://wttr.in/{args.city}", params={"format": "j1"})
        data = res.json()
        temp = data["current_condition"][0]["temp_C"]
        weather_description = data["current_condition"][0]["weatherDesc"][0]["value"]

        icon = "\uf76b"  # fontawesome icon "temperature-low"
        txt = f"{temp}°C"
        txtclick = f"xfce4-terminal -e 'curl http://wttr.in/{args.city}' --hold"
        tool = weather_description
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = Weather()
    print(plugin.execute())


if __name__ == "__main__":
    main()
