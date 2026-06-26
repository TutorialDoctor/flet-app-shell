import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def ControlSidebar(items=[]):
    def handle_click(e):
        set_page_state({"name": "New Page Template"})

    page_state, set_page_state = ft.use_state({"name": "Page Template"})

    container = ft.Container(width=500,
        padding=12,
        on_click=handle_click,
        expand=2,
        border=ft.Border.all(color="#EEEEF0"),
        border_radius=12)
    column = ft.Column()
    container.content = column

    column.controls = items
    return container

    # return ft.Column([
    #     ft.Button("Click", on_click=handle_click),
    #     ft.Text(page_state['name'],color= PRIMARY_COLOR)
    # ])