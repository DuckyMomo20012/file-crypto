import re
from typing import Union

from pygments import highlight
from pygments.formatters import TerminalTrueColorFormatter
from pygments.lexers import get_lexer_for_filename


def syntaxHighlight(
    fileName: str, code: str, theme: str = "dracula"
) -> Union[str, None]:

    try:
        lexer = get_lexer_for_filename(fileName)
        # FIXME: We should check if the terminal supports TRUE color system
        formatter = TerminalTrueColorFormatter(style=theme)

        highlightedCode = highlight(code, lexer, formatter)

        return highlightedCode
    except (ValueError):
        return None


def removeHighlight(code: str) -> str:

    # NOTE: Ref: https://stackoverflow.com/a/14693789/12512981

    pattern = r"(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])"

    regex = re.compile(pattern)
    return regex.sub("", code)
