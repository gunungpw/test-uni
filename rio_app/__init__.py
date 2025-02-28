from __future__ import annotations

from pathlib import Path
import typing as t

import rio

from . import components as comps

# Define a theme for Rio to use.
#
# You can modify the colors here to adapt the appearance of your app or website.
# The most important parameters are listed, but more are available! You can find
# them all in the docs
#
# https://rio.dev/docs/api/theme
theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex("01dffdff"),
    secondary_color=rio.Color.from_hex("0083ffff"),
    mode="light",
)


# Create the Rio app
app = rio.App(
    name='.',
    # You can optionally provide a root component for the app. By default,
    # Rio's default navigation is used. By providing your own component, you
    # can create components which stay put while the user navigates between
    # pages, such as a navigation bar or footer.
    #
    # When you do this, make sure your component contains a `rio.PageView`
    # so the currently active page is still visible.
    build=comps.RootComponent,
    theme=theme,
    assets_dir=Path(__file__).parent / "assets",
)

