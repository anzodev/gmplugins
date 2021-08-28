import psutil

from . import Output
from . import Plugin


class LoadAverage(Plugin):
    def _make_output(self, _) -> Output:
        icon = "\uf2db"  # fontawesome icon "microchip"
        txt = " ".join([str(i) for i in psutil.getloadavg()])
        txtclick = "xfce4-terminal -e 'top -d 1'"
        tool = "Load average"
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = LoadAverage()
    print(plugin.execute())


if __name__ == "__main__":
    main()
