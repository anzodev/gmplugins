import datetime
from argparse import ArgumentParser
from argparse import Namespace

from . import Output
from . import Plugin


class Time(Plugin):
    def _update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-f", "--format", type=str, metavar="str", default="%Y-%m-%d %H:%M:%S"
        )
        parser.add_argument("--disable-dayplanner", action="store_true")

    def _make_output(self, args: Namespace) -> Output:
        current_date = datetime.datetime.now()

        icon = "\uf017"  # fontawesome icon "clock"
        txt = current_date.strftime(args.format)
        txtclick = None if args.disable_dayplanner else "dayplanner"
        tool = current_date.strftime("%A")
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = Time()
    print(plugin.execute())


if __name__ == "__main__":
    main()
