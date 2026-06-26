import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


def SidebarTemplate(items=[]):
    
    items = [
        {
            "label": "",
            "icon": ft.Icons.ABC,
            "url": "",
            "subitems": []
        }
    ]

    def handle_click(e):
        return

    return ft.Container(
        content=ft.Card(
                content=ft.Container(
                    width=500,
                    padding=ft.Padding.symmetric(vertical=10),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            ft.ListTile(title=ft.Text("One-line list tile")),
                            ft.ListTile(
                                title=ft.Text("One-line dense list tile"),
                                dense=True,
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SETTINGS),
                                title=ft.Text("One-line selected list tile"),
                                selected=True,
                            ),
                            ft.ListTile(
                                leading=ft.Image(
                                    src="assets/icon-192.png",
                                    fit=ft.BoxFit.CONTAIN,
                                ),
                                title=ft.Text("One-line with leading control"),
                            ),
                            ft.ListTile(
                                title=ft.Text("One-line with trailing control"),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Item 1"),
                                        ft.PopupMenuItem(content="Item 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ALBUM),
                                title=ft.Text(
                                    value=(
                                        "One-line with leading and trailing controls"
                                    )
                                ),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Item 1"),
                                        ft.PopupMenuItem(content="Item 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SNOOZE),
                                title=ft.Text(
                                    value=(
                                        "Two-line with leading and trailing controls"
                                    )
                                ),
                                subtitle=ft.Text("Here is a second title."),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Item 1"),
                                        ft.PopupMenuItem(content="Item 2"),
                                    ],
                                ),
                            ),
                        ],
                    ),
                )
            ),expand=1
    )