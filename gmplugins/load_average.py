import psutil

from . import Output
from . import Plugin


class LoadAverage(Plugin):
    def _make_output(self, _) -> Output:
        loadavg = psutil.getloadavg()
        cpu_count = psutil.cpu_count()

        icon = "\uf2db"  # fontawesome icon "microchip"
        txt = " ".join([str(i) for i in loadavg])
        txtclick = "xfce4-terminal -e 'top -d 1'"
        tool = " ".join([f"{x / cpu_count * 100:.2f}%" for x in loadavg])
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = LoadAverage()
    print(plugin.execute())


if __name__ == "__main__":
    main()
