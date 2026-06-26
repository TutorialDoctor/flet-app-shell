import flet as ft
from pages.Home import Home
from pages.About import About
from pages.Settings import Settings
from pages.Profile import Profile

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"

STATES = {
    ft.ControlState.HOVERED: PRIMARY_COLOR,
    ft.ControlState.FOCUSED: ft.Colors.BLUE,
    ft.ControlState.DEFAULT: ft.Colors.BLACK,
}


@ft.component
def Nav():
    troute = ft.TemplateRoute(ft.context.page.route)

    if troute.match("/profile/:id"):
        print("Book ID:", troute.id)
    elif troute.match("/account/:account_id/orders/:order_id"):
        print("Account:", troute.account_id, "Order:", troute.order_id)
    else:
        print("Unknown route")

    return ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Image(src="icon.png", width=30, height=30),
                                ft.TextButton(
                                    "Home",
                                    style=ft.ButtonStyle(color=STATES),
                                    on_click=lambda: ft.context.page.navigate("/"),
                                ),
                                ft.TextButton(
                                    "About",
                                    style=ft.ButtonStyle(color=STATES),
                                    on_click=lambda: ft.context.page.navigate("/about"),
                                ),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.CupertinoTextField(
                                                placeholder_text="Search", width=500
                                            )
                                        ]
                                    ),
                                    border_radius=8,
                                    padding=ft.Padding.symmetric(
                                        vertical=4, horizontal=12
                                    ),
                                )
                            ]
                        ),
                        ft.Row(
                            [
                                ft.TextButton(
                                    "Settings",
                                    on_click=lambda: ft.context.page.navigate(
                                        "/settings"
                                    ),
                                )
                                # ft.TextButton(
                                #     "Profile",
                                #     on_click=lambda: ft.context.page.navigate(
                                #         "/profile"
                                #     ),
                                # ),
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Router(
                    [
                        ft.Route(index=True, component=Home),
                        ft.Route(path="about", component=About),
                        ft.Route(path="settings", component=Settings),
                        ft.Route(
                            path="profile",
                            component=Profile,
                        ),
                        ft.Route(
                            path="profile/:id",
                            component=Profile
                        ),
                    ]
                ),
            ]
        ),
        padding=2,
    )
