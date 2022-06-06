from environs import Env
from mongoengine import connect
from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Placeholder
from textual.widget import Widget
from rich.panel import Panel
import json

from src.auth.service import getOneUser


env = Env()
# Read .env into os.environ
env.read_env()

connect(host=env.str("MONGODB_HOST"))

user = getOneUser(username="admin")
# print(json.loads(user.to_json()))


class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel(
            f"Hello user: [b]{user.username}[/b]",
            style=("on blue" if self.mouse_over else ""),
        )

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class SmoothApp(App):
    """Demonstrates smooth animation. Press 'b' to see it in action."""

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("b", "toggle_sidebar", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

    show_bar = Reactive(False)

    def watch_show_bar(self, show_bar: bool) -> None:
        """Called when show_bar changes."""
        self.bar.animate("layout_offset_x", 0 if show_bar else -40)

    def action_toggle_sidebar(self) -> None:
        """Called when user hits 'b' key."""
        self.show_bar = not self.show_bar

    async def on_mount(self) -> None:
        """Build layout here."""
        footer = Footer()
        self.bar = Placeholder(name="left")

        hovers = (Hover() for _ in range(10))

        await self.view.dock(footer, edge="bottom")
        await self.view.dock(Hover(), Placeholder(), edge="top")
        await self.view.dock(self.bar, edge="left", size=40, z=1)

        self.bar.layout_offset_x = -40

        # self.set_timer(10, lambda: self.action("quit"))


SmoothApp.run(log="textual.log", log_verbosity=2)
