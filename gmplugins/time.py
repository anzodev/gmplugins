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

    def _make_output(self, args: Namespace) -> Output:
        icon = "\uf017"  # fontawesome icon "clock"
        txt = datetime.datetime.now().strftime(args.format)
        txtclick = "dayplanner"
        tool = "Time"
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = Time()
    print(plugin.execute())


if __name__ == "__main__":
    main()
