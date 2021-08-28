import psutil

from . import Output
from . import Plugin


class Memory(Plugin):
    def _make_output(self, _) -> Output:
        mem = psutil.virtual_memory()
        swap_mem = psutil.swap_memory()

        icon = "\uf538"  # fontawesome icon "memory"
        txt = " ".join(
            [
                f"{(mem.used / 1000 ** 3):.2f}GB",
                f"{(mem.available / 1000 ** 3):.2f}GB",
                f"{(swap_mem.used / 1000 ** 3):.2f}GB",
            ]
        )
        txtclick = "xfce4-terminal -e 'top -d 1'"
        tool = "\n".join(
            [
                f"Total: {(mem.total / 1000 ** 3):.2f}G",
                f"Available: {(mem.available / 1000 ** 3):.2f}G",
                f"Used: {(mem.used / 1000 ** 3):.2f}G ({mem.percent}%)",
                f"Free: {(mem.free / 1000 ** 3):.2f}G",
                f"Swap total: {(swap_mem.total / 1000 ** 3):.2f}G",
                f"Swap used: {(swap_mem.used / 1000 ** 3):.2f}G ({swap_mem.percent}%)",
                f"Swap free: {(swap_mem.free / 1000 ** 3):.2f}G",
            ]
        )
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = Memory()
    print(plugin.execute())


if __name__ == "__main__":
    main()
