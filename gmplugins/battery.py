from subprocess import getoutput

from . import Output
from . import Plugin


class Battery(Plugin):
    def _make_output(self, _) -> Output:
        percentage = "%?"
        state = ""
        time_to_empty = ""

        data = getoutput("upower -i /org/freedesktop/UPower/devices/battery_BAT0")
        data = data.rstrip("\n")

        rows = data.split("\n")
        for row in rows:
            if "percentage" in row:
                percentage = row.split()[-1]
                value = int(percentage.replace("%", ""))
                if value < 80:
                    icon = "\uf241"  # fontawesome icon "battery-three-quarters"
                elif value < 50:
                    icon = "\uf242"  # fontawesome icon "battery-half"
                elif value < 30:
                    icon = "\uf243"  # fontawesome icon "battery-quarter"
                elif value < 15:
                    icon = "\uf244"  # fontawesome icon "battery-empty"
                else:
                    icon = "\uf240"  # fontawesome icon "battery-full"

            if "state" in row:
                state = row.split()[-1]

            if "time to empty" in row:
                time_to_empty = " ".join(row.split()[-2:])

        current_state = None
        if state == "charging":
            current_state = state
        elif state == "fully-charged":
            current_state = "charged"
        elif time_to_empty != "":
            current_state = time_to_empty
        else:
            current_state = "discharging"

        txt = f"{percentage} ({current_state})"
        tool = "\n".join([i[2:] for i in rows])  # remove left offset
        txtclick = "xfce4-power-manager-settings &"
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = Battery()
    print(plugin.execute())


if __name__ == "__main__":
    main()
