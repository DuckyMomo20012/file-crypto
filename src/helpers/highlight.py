import re

from pygments import highlight  # type: ignore
from pygments.formatters import TerminalTrueColorFormatter  # type: ignore
from pygments.lexers import get_lexer_for_filename  # type: ignore


def syntaxHighlight(fileName: str, code: str) -> str:

    lexer = get_lexer_for_filename(fileName)
    # FIXME: We should check if the terminal supports 256 colors
    formatter = TerminalTrueColorFormatter(style="monokai")

    highlightedCode = highlight(code, lexer, formatter)

    return highlightedCode


def removeHighlight(code: str) -> str:

    # NOTE: Ref: https://stackoverflow.com/a/14693789/12512981

    pattern = r"(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])"

    regex = re.compile(pattern)
    return regex.sub("", code)
