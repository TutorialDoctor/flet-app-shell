import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def ItemList():

    page_state, set_page_state = ft.use_state({"name": "PPart Page"})

    lv = ft.ListView(
        spacing=10,
        divider_thickness=2,
        width=150,
        height=400,
        scroll=ft.ScrollMode.ALWAYS,
    )
    lv.controls = [ft.Container(ft.Text("WELCOME"),padding=20)] + [ ft.Container(ft.Text(f"Line {i}", color="black"),padding=20) for i in range(0, 60)]


    content = ft.Container(
        ft.Column(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Row([ft.Image(fit=ft.BoxFit.COVER,border_radius=40,src="https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress",width=84,height=84)]),
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text("Emily Johnson",size=30),
                                            ft.Text("johnson@example.com"),
                                        ]
                                    ),
                                    ft.Icon(icon=ft.Icons.STAR),
                                ]
                            ),
                        ]
                    ),width=400
                ),
                ft.Container(),
                ft.Container(),
            ]
        )
    )

    return content
