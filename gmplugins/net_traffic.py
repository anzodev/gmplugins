from argparse import ArgumentParser
from argparse import Namespace

import psutil

from . import Output
from . import Plugin


class NetTraffic(Plugin):
    def _update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("interface", type=str)

    def _make_output(self, args: Namespace) -> Output:
        io_counters = psutil.net_io_counters(pernic=True)
        net_itf = io_counters[args.interface]

        icon = "\uf542"  # fontawesome icon "project-diagram"
        txt = (
            f"S:{(net_itf.bytes_sent / 1000 ** 3):.2f}G"
            f" R:{(net_itf.bytes_recv / 1000 ** 3):.2f}G"
        )
        txtclick = None
        tool = "\n\n".join(
            [
                "\n".join(
                    [
                        itf,
                        "\n".join([f"  {k}: {v}" for k, v in data._asdict().items()]),
                    ]
                )
                for itf, data in io_counters.items()
            ]
        )
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = NetTraffic()
    print(plugin.execute())


if __name__ == "__main__":
    main()
