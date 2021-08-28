import json
import os
from abc import ABC
from abc import abstractmethod
from argparse import ArgumentParser
from argparse import Namespace
from collections import namedtuple


CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config/gmplugins")
STYLE_PATH = os.path.join(CONFIG_DIR, "style.json")


Output = namedtuple("Output", ["icon", "txt", "txtclick", "tool"])


class Plugin(ABC):
    def execute(self) -> str:
        style = self._default_style()
        style.update(self._load_user_style())

        parser = ArgumentParser()
        self._update_parser(parser)
        args = parser.parse_args()

        try:
            output = self._make_output(args)
        except Exception:
            output = Output("\uf059", "n/a", None, "n/a")

        offset = " " * style["padding"]
        icon = output.icon
        txt = output.txt
        tool = output.tool or "n/a"
        txtclick = output.txtclick

        rows = []

        rows.append("<txt>{offset}")
        if icon is not None:
            rows.append(
                "<span"
                " font_desc='Font Awesome 5 Free {icon_font_size}'"
                " fgcolor='{icon_color}'>"
                "{icon}"
                "</span>"
                "  "
            )
        rows.append(
            "<span"
            " font_desc='{font_face} {txt_font_size}'"
            " fgcolor='{txt_color}'>"
            "{txt}"
            "</span>"
        )
        rows.append("{offset}</txt>\n")

        rows.append(
            "<tool>"
            "<span"
            " font_desc='{font_face} {tooltip_font_size}'"
            " fgcolor='{tooltip_color}'>"
            "{tool}"
            "</span>"
            "</tool>"
        )

        if txtclick is not None:
            rows.append("\n<txtclick>{txtclick}</txtclick>")

        return "".join(rows).format(
            font_face=style["font-face"],
            icon_font_size=style["icon-font-size"],
            icon_color=style["icon-color"],
            txt_font_size=style["txt-font-size"],
            txt_color=style["txt-color"],
            tooltip_font_size=style["tooltip-font-size"],
            tooltip_color=style["tooltip-color"],
            offset=offset,
            icon=icon,
            txt=txt,
            tool=tool,
            txtclick=txtclick,
        )

    def _default_style(self) -> dict:
        return {
            "font-face": "monospace",
            "icon-font-size": 9,
            "icon-color": "#000000",
            "txt-font-size": 10,
            "txt-color": "#000000",
            "tooltip-font-size": 9,
            "tooltip-color": "#ffffff",
            "padding": 1,
        }

    def _load_user_style(self) -> dict:
        if not os.path.exists(STYLE_PATH):
            return {}

        with open(STYLE_PATH) as f:
            return json.load(f)

    def _update_parser(self, parser: ArgumentParser) -> None:
        ...

    @abstractmethod
    def _make_output(self, args: Namespace) -> Output:
        ...
