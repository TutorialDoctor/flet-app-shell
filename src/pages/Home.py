import flet as ft
from components.PageLayout import PageLayout

from models import User

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"


@ft.component
def Home():
    def handle_click(e):
        set_page_state({"name": "Home Page Clicked"})

    page_state, set_page_state = ft.use_state({"name": "Home Page"})

    changed, set_changed = ft.use_state(False)

    # selected_row, set_selected_row = ft.use_state({1, 3, 5})

    selected_ids, set_selected_ids = ft.use_state(set())

    users = User.select()

    new_user, set_new_user = ft.use_state(
        {
            "email": "",
            "first_name": "No name",
            "last_name": "",
            "employer": "",
            "address": "",
            "phone": "",
            "info": "",
            "gallery_name":"images/td",
            "profile_image": "https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress",
        }
    )

    # selected_item_ids: set[int] = {1, 3, 5}

    def handle_select_all(e):
        if e.data:
            set_selected_ids({int(user.id) for user in users})
        else:
            set_selected_ids(set())

    def handle_row_selection_change(e):
        item_id = e.control.data

        new_selection = set(selected_ids)

        if e.data:
            new_selection.add(item_id)
        else:
            new_selection.discard(item_id)

        set_selected_ids(new_selection)

    def goToRoute(e, page):
        print(e.control.data)
        print(page)
        page.navigate(f"/profile/{e.control.data}")

    def deleteUser(e, id):
        set_changed(not changed)
        user = User.get(User.id == id)
        # Delete it from the database
        user.delete_instance()

    table = ft.DataTable(
        on_select_all=handle_select_all,
        columns=[
            ft.DataColumn(label=ft.Text("Cover")),
            ft.DataColumn(label=ft.Text("Name")),
            ft.DataColumn(label=ft.Text("Email")),
            ft.DataColumn(label=ft.Text("Created")),
            ft.DataColumn(label=ft.Text("Updated")),
            ft.DataColumn(label=ft.Text("")),
        ],
        rows=[
            ft.DataRow(
                on_select_change=handle_row_selection_change,
                selected=user.id in selected_ids,
                data=user.id,
                cells=[
                    ft.DataCell(
                        ft.Image(
                            src=user.profile_image,
                            width=30,
                            height=30,
                            fit=ft.BoxFit.COVER,
                            border_radius=60,
                        )
                    ),
                    ft.DataCell(
                        ft.Container(
                            ft.Text(user.first_name + " " + user.last_name),
                            on_click=lambda e: goToRoute(e, e.page),
                            data=user.id,
                        )
                    ),
                    ft.DataCell(ft.Text(user.email)),
                    ft.DataCell(ft.Text(user.created_at)),
                    ft.DataCell(ft.Text(user.updated_at)),
                    ft.DataCell(
                        ft.Button(
                            "Delete",
                            on_click=lambda e, user=user: deleteUser(e, user.id),
                        )
                    ),
                ],
            )
            for user in users
        ],
        border=ft.Border.all(color="#EEEEF0"),
        border_radius=12,
        data_row_color={
            ft.ControlState.HOVERED: ft.Colors.with_opacity(0.08, ft.Colors.PRIMARY),
            ft.ControlState.SELECTED: ft.Colors.with_opacity(0.14, ft.Colors.PRIMARY),
        },
        show_checkbox_column=True,
    )
    # print(users)

    user = User.get_by_id(1)
    print(user.first_name + user.last_name)

    left_nav_items = [
        {"label": "Settings", "icon": ft.Icons.ABC, "url": "/settings", "subitems": []},
        {"label": "Profile", "icon": ft.Icons.ABC, "url": "/profile", "subitems": []},
    ]

    # 2. Dynamic state handler
    def handle_field_change(key: str):
        def handler(e):
            # We use Python's dictionary unpacking to create a shallow copy
            # and override the specific key with the new TextField value
            set_new_user({**new_user, key: e.control.value})

        return handler

    def handle_banner_close(e: ft.Event[ft.TextButton]):
        ft.context.page.pop_dialog()

    banner_text, set_banner_text = ft.use_state("Created user")

    banner = ft.Banner(
        leading=ft.Icon(ft.Icons.INFO_OUTLINED, color=ft.Colors.PRIMARY),
        content=ft.Text(banner_text),
        actions=[ft.TextButton("Dismiss", on_click=handle_banner_close)],
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        open=True,
    )

    # 3. Create user function that leverages the state
    def create_user(e):
        # try:
        #     ft.context.page.show_dialog(banner)
        # except Exception as e:
        #     banner.open = False
        try:
            user = User(
                first_name=new_user["first_name"],
                last_name=new_user["last_name"],
                email=new_user["email"],
                profile_image=new_user["profile_image"],
                info=new_user["info"] or "developer of this website",
                employer=new_user["employer"],
                address=new_user["address"],
                phone=new_user["phone"],
                gallery_name=new_user["gallery_name"]
            )
            user.save()
            set_banner_text("Created User")
            ft.context.page.show_dialog(banner)
            print(f"Successfully created user: {user.email}")

            # Optional: Clear the form after saving
            # set_new_user({k: "" for k in new_user.keys()})

            set_new_user(  {
            "email": "",
            "first_name": "No name",
            "last_name": "",
            "employer": "",
            "address": "",
            "phone": "",
            "info": "",
            "gallery_name": "",
            "profile_image": "https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress",
        })

        except Exception as ex:
            print(f"Failed to create user: {ex}")
            set_banner_text("Failed to create user")
            try:
                ft.context.page.show_dialog(banner)
            except Exception as e:
                print(f"Already open {e}")

    # 4. Form Layout
    items = [
        ft.Column(
            [
                ft.TextField(
                    label="Email",
                    expand=True,
                    value=new_user["email"],
                    on_change=handle_field_change("email"),
                ),
                ft.TextField(
                    label="First Name",
                    expand=True,
                    value=new_user["first_name"],
                    on_change=handle_field_change("first_name"),
                ),
                ft.TextField(
                    label="Last Name",
                    expand=True,
                    value=new_user["last_name"],
                    on_change=handle_field_change("last_name"),
                ),
                ft.TextField(
                    label="Employer",
                    expand=True,
                    value=new_user["employer"],
                    on_change=handle_field_change("employer"),
                ),
                ft.TextField(
                    label="Address",
                    expand=True,
                    value=new_user["address"],
                    on_change=handle_field_change("address"),
                ),
                ft.TextField(
                    label="Phone",
                    expand=True,
                    value=new_user["phone"],
                    on_change=handle_field_change("phone"),
                ),
                ft.TextField(
                    label="Profile Image URL",
                    expand=True,
                    value=new_user["profile_image"],
                    on_change=handle_field_change("profile_image"),
                ),
                ft.TextField(
                    label="Gallery Name",
                    expand=True,
                    value=new_user["gallery_name"],
                    on_change=handle_field_change("gallery_name"),
                ),
                ft.TextField(
                    label="Info",
                    expand=True,
                    value=new_user["info"],
                    on_change=handle_field_change("info"),
                ),
                ft.Button("Create", on_click=create_user,width=200),
            ]
        )
    ]

    segment_state, set_segment_state = ft.use_state(0)

    def render(e):
        set_segment_state(1)

    segment = ft.CupertinoSlidingSegmentedButton(
        selected_index=segment_state,
        on_change=lambda e: set_segment_state(e.control.selected_index),
        width=200,
        bgcolor=BG_COLOR,
        proportional_width=True,
        thumb_color=PRIMARY_COLOR,
        controls=[
            ft.Text("Table", color="white"),
            ft.Text("Grid", color="white"),
        ],
    )
    table_content = ft.Column(
        [
            # ft.Container(ft.Text(page_state["name"]), expand=1),
            # ft.Container(ft.Text(user.first_name + user.last_name), expand=1),
            # ft.Container(ft.Text("three"), expand=1),
            ft.Column([table], scroll=ft.ScrollMode.ALWAYS, height=800)
        ]
    )

    grid = ft.GridView(
        runs_count=4,
        child_aspect_ratio=.75,
        run_spacing=30,
        max_extent=200,
        spacing=3,
        controls=[
            ft.Container(
                ft.Column([
                ft.Image(border_radius=16,expand=True,width=300,
                    src=user.profile_image, fit=ft.BoxFit.COVER
                ), ft.Text(user.first_name)]),
                on_click=lambda e: goToRoute(e, e.page),
                data=user.id,
            )
            for user in users
        ],
    )

    image_content = ft.Column(
        [
            # ft.Container(ft.Text(page_state["name"]), expand=1),
            # ft.Container(ft.Text(user.first_name + user.last_name), expand=1),
            # ft.Container(ft.Text("three"), expand=1),
            ft.Column([grid], scroll=ft.ScrollMode.ALWAYS, height=800)
        ]
    )

    return PageLayout(
        title="Home",
        content=(
            ft.Column([segment, table_content])
            if segment_state == 0
            else ft.Column([segment, image_content])
        ),
        control_items=items,
    )
