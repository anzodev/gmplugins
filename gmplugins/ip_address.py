from subprocess import getoutput

import requests

from . import Output
from . import Plugin


class IPAddress(Plugin):
    def _make_output(self, _) -> Output:
        icon = "\uf3c5"  # fontawesome icon "map-marker"
        txt = requests.get("https://ipecho.net/plain").text
        txtclick = f"/bin/bash -c 'echo {txt} | xclip -in -sel c'"
        tool = f"All addresses: {getoutput('hostname -I')[:-1].replace(' ', ', ')}"
        return Output(icon, txt, txtclick, tool)


def main() -> None:
    plugin = IPAddress()
    print(plugin.execute())


if __name__ == "__main__":
    main()
