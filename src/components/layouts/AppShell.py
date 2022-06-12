import pytermgui as ptg


def AppShell():
    layout = ptg.Layout()

    # A header slot with a height of 1
    layout.add_slot("Header", height=1)
    layout.add_break()

    # A slot in the same row as body, using the full non-occupied height and
    # 20% of the terminal's height.
    layout.add_slot("Nav Bar", width=0.2)

    # A body slot that will fill the entire width, and the height is remaining
    layout.add_slot("Body")

    layout.add_break()

    # A footer with a static height of 1
    layout.add_slot("Footer", height=1)

    return layout
