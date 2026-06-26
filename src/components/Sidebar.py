import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"

def Sidebar(items=[{"label": "Settings", "icon": ft.Icons.ABC, "url": "/settings", "subitems": []}]):


    def handle_click(e):
        print("Going to page")

    nav_items = [
        ft.Container(
            ft.ListTile(
                leading=ft.Icon(i["icon"]),
                title=ft.Text(value=(i["label"])),
                # subtitle=ft.Text("Here is a second title."),
                trailing=ft.PopupMenuButton(
                    icon=ft.Icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(content="Item 1"),
                        ft.PopupMenuItem(content="Item 2"),
                    ],
                ),
            ),
            on_click=lambda e, i=i: ft.context.page.navigate(f"{i['url']}"),
        )
        for i in items
    ]

    return ft.Container(
        width=500,
        padding=ft.Padding.symmetric(vertical=10),
        content=ft.Column(spacing=0, controls=nav_items),
        on_click=handle_click,
        expand=1,
        border=ft.Border.all(color="#EEEEF0"),
        border_radius=12,
    )
