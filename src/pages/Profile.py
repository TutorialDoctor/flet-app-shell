import flet as ft
from components.PageLayout import PageLayout
from components.ProfileContent import ProfileContent
from models import User
import os

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#17191B"

def getImages(directory="images"):
    photo_images = [
        _
        for _ in os.listdir(os.path.join("./", f"src/assets/{directory}/"))
        if _.endswith("png")
        or _.endswith("jpg")
        or _.endswith("PNG")
        or _.endswith("JPG")
        or _.endswith("webp")
    ]
    return photo_images

# use flet-video with this
def getVideos(directory="videos"):
    videos = [
        _
        for _ in os.listdir(os.path.join("./", f"src/assets/{directory}/"))
        if _.endswith("mov")
        or _.endswith("MOV")
        or _.endswith("mp4")
        or _.endswith("MP4")
        or _.endswith("webv")
    ]
    return videos

# use flet-audio library with this
def getAudio(directory="audio"):
    audio_files = [
        _
        for _ in os.listdir(os.path.join("./", f"src/assets/{directory}/"))
        if _.endswith("mp3")
        or _.endswith("wav")
        or _.endswith("MP3")
        or _.endswith("WAC")
    ]
    return audio_files



@ft.component
def Profile():
    def handle_click(e):
        set_page_state({"name": "Profile Page Clicked"})

    page_state, set_page_state = ft.use_state({"name": "Profile Page"})
    params = ft.use_route_params()


    # 1. Safely extract user_id
    user_id = params.get("id")
    user = None

    if user_id:
        user = User.get_by_id(user_id)
    else:
        # FALLBACK: If no ID is passed, load the default or current user
        # user = User.get_current_session_user() # <-- Swap to your actual auth method if you have one
        pass
    
    # NO USE PROFILE VIEW
    if not user:
        return PageLayout(
            title="Profile",
            left_nav_items=[],
            content=ft.Container(ft.Text("Backups")
            ),
            control_items=ft.Text("No data available"),
        )
     # END NO USE PROFILE VIEW

    def show_popover(e, i):
        page = ft.context.page
        alert = ft.AlertDialog(
            bgcolor="white",
            content=ft.Row(
                [
                    ft.Image(
                        src=f"{user.gallery_name}/{i}",
                        expand=4,border_radius=12
                    ),
                    ft.Text("Image Details")
                ],vertical_alignment=ft.MainAxisAlignment.START
            ),
            actions=[ft.TextButton("Close", on_click=lambda e: page.pop_dialog())],
        )

        page.show_dialog(alert)
    
    def buildImageGrid(location="images", show_time=True):
        grid = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )
        for i in getImages(location):
            grid.controls.append(
                ft.Stack(
                    [
                        ft.Container(ft.Image(
                            width=300,
                            border_radius=10,
                            src=f"{location}/{i}",
                            fit=ft.BoxFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                        ),on_click=lambda e, i=i: show_popover(e,i)),
                        # (
                        #     Container(Text("0:00", color=Colors.WHITE), padding=10)
                        #     if show_time == True
                        #     else Text("")
                        # ),
                        ft.RadioGroup(content=ft.Radio(active_color=PRIMARY_COLOR)),
                    ]
                )
            )
        return grid
    
    user_details, set_user_details = ft.use_state(
        {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "employer": user.employer,
            "address": user.address,
            "phone": user.phone,
            "profile_image": user.profile_image,
            "gallery_name": user.gallery_name,
        }
    )

    user_fullname = f"{user_details['first_name']} {user_details['last_name']}"

    print(params)

    def handle_field_change(field):
        def handler(e):
            set_user_details({**user_details, field: e.control.value})

        return handler

    def save_user(e):
        user = User.get_by_id(params["id"])
        user.email = user_details["email"]
        user.first_name = user_details["first_name"]
        user.last_name = user_details["last_name"]
        user.employer = user_details["employer"]
        user.address = user_details["address"]
        user.phone = user_details["phone"]
        user.profile_image = user_details["profile_image"]
        user.gallery_name = user_details["gallery_name"]

        try:
            user.save()
        except Exception as e:
            print(f"User already exists: {e}")

        print(f"USER UPDATED {user.id}")

    fields = [
        {"label": "First Name", "key": "first_name"},
        {"label": "Last Name", "key": "last_name"},
        {"label": "Email", "key": "email"},
        {"label": "Employer", "key": "employer"},
        {"label": "Address", "key": "address"},
        {"label": "Phone", "key": "phone"},
        {"label": "Profile Image", "key": "profile_image"},
        {"label": "Gallery Name", "key": "gallery_name"},
    ]

    table = ft.DataTable(
        heading_row_color="#FDFDFD",
        columns=[
            ft.DataColumn(
                label=ft.Row(
                    [ft.Text("Personal Details"), ft.Button("Save", on_click=save_user)]
                )
            ),
            ft.DataColumn(label=ft.Text("")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(field["label"])),
                    ft.DataCell(
                        ft.TextField(
                            value=user_details[field["key"]],
                            on_change=handle_field_change(field["key"]),
                            border=ft.InputBorder.NONE,
                            expand=True,
                        )
                    ),
                ],
            )
            for field in fields
        ],
        border=ft.Border.all(color="#EEEEF0"),
        border_radius=12,
        data_row_color={
            ft.ControlState.HOVERED: ft.Colors.with_opacity(0.08, ft.Colors.PRIMARY),
            ft.ControlState.SELECTED: ft.Colors.with_opacity(0.14, ft.Colors.PRIMARY),
        },
        show_checkbox_column=True,
        width=900,
    )

    # add security table

    content = ft.Column(
        [
            ft.Container(
                ProfileContent(
                    name=f"{user_details['first_name']} {user_details['last_name']}",
                    email=user_details['email'],
                    profile_image=user.profile_image,
                ),
                expand=1,
            ),
            ft.Container(table, expand=1),
            # ft.Container(security_table, expand=1),
        ]
    )

    left_nav_items = [
        {
            "label": "Settings",
            "icon": ft.Icons.SETTINGS,
            "url": "/settings",
            "subitems": [],
        },
        {
            "label": "Chat Settings",
            "icon": ft.Icons.CHAT_BUBBLE_OUTLINE,
            "url": "/settings",
            "subitems": [],
        },
        {
            "label": "Reply Settings",
            "icon": ft.Icons.REPLY_OUTLINED,
            "url": "/settings",
            "subitems": [],
        },
        {
            "label": "Gift",
            "icon": ft.Icons.FENCE_OUTLINED,
            "url": "/settings",
            "subitems": [],
        },
        {
            "label": "Bookmark",
            "icon": ft.Icons.BOOK_OUTLINED,
            "url": "/settings",
            "subitems": [],
        },
        {
            "label": "Coffee",
            "icon": ft.Icons.COFFEE_OUTLINED,
            "url": "/settings",
            "subitems": [],
        },
    ]

    cards = [
        ft.Card(
            shadow_color="#EEEEF0",
            bgcolor="white",
            content=ft.Container(
                width=400,
                padding=10,
                content=ft.ListTile(
                    bgcolor="white",
                    leading=ft.Icon(ft.Icons.FOREST),
                    title=ft.Text("Card Name"),
                ),
            ),
        )
        for i in ["One", "Two", "Three"]
    ]

    control_items = ft.Column([ft.Text("Photo Gallery"),buildImageGrid(user.gallery_name)])

    return PageLayout(
        title="Profile",
        left_nav_items=left_nav_items,
        content=content,
        control_items=control_items,
    )
