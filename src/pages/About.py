import flet as ft
from components.PageLayout import PageLayout
PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def About():
    def handle_click(e):
        set_page_state({"name": "About Page Clicked"})

    page_state, set_page_state = ft.use_state({"name": "About Page"})

    content = ft.Column([
        ft.Container(ft.Text(page_state['name']),expand=1),
        ft.Container(ft.Text("Two"),expand=1),
        ft.Container(ft.Text("three"),expand=1)
        ]
    )

    left_nav_items = [
        {"label": "Settings", "icon": ft.Icons.ABC, "url": "/settings", "subitems": []},
        {"label": "Profile", "icon": ft.Icons.ABC, "url": "profile", "subitems": []}
    ]

    return PageLayout(title="About", left_nav_items=left_nav_items, content=content)