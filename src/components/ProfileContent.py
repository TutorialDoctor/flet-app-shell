import flet as ft

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def ProfileContent(name="No Name",email="noname@gmail.com",profile_image="https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress"):

    page_state, set_page_state = ft.use_state({"name": "ProfileContent Page"})

    content = ft.Container(
        ft.Column(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Row([ft.Image(fit=ft.BoxFit.COVER,border_radius=40,src=profile_image,width=84,height=84)]),
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(name,size=30),
                                            ft.Text(email),
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
