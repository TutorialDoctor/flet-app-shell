import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def TestComponent():
    def handle_click(e):
        set_page_state({"name": "New Page Template"})

    page_state, set_page_state = ft.use_state({"name": "Page Template"})

    return ft.Column([
        ft.Button("Click", on_click=handle_click),
        ft.Text(page_state['name'],color= PRIMARY_COLOR)
    ])