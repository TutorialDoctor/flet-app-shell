import flet as ft
from components.Sidebar import Sidebar
from components.ControlSidebar import ControlSidebar

PRIMARY_COLOR = "#FF0EC1"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"

def PageLayout(title="App Shell Heading",left_nav_items=[],control_items=[],**kwargs):
    """Creates a layout to inject controls into

    Args:
        kwargs (Control): any content you want to pass

    Returns:
        Row: A row of controls separated into three sections
    """

    def handle_click(e):
        print("Handled")

    return ft.Column(
        [
            ft.Text(title + ": " + ft.context.page.route,size=20),
            ft.Row(
                [
                    Sidebar(items=left_nav_items) if left_nav_items else ft.Container(),
                    ft.Container(
                        content=ft.Column([kwargs["content"]]),expand=4,border=ft.Border.all(color="#EEEEF0"),padding=12,border_radius=12
                    ),
                    ControlSidebar(items=control_items) if control_items else ft.Container()
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.MainAxisAlignment.START,
            ),
        ]
    )
