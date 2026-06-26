import flet as ft
from components.Nav import Nav
from models import database, User, Items, UserItems, UserInfo, Images, Videos
from datetime import date
from faker import Faker
fake = Faker()


def _db_connect():
    if database.is_closed():
        database.connect()

def _db_close(exc):
    if not database.is_closed():
        database.close()

def create_db_tables():
    try:
        database.create_tables([UserInfo, User, Items, UserItems,Images,Videos])
    except e:
        print(f"Tables already created {e}")

def seed_db():
    users = [
        {"first_name": "Tutorial","last_name": "Doctor", "email": "td@gmail.com"},
        {"first_name": "George","last_name": "Williams", "email": "gw@gmail.com"}
    ]
    for user in users:
        try:
            user = User(
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    employer="Google",
                    address="123 Street",
                    gallery_name="images",
                    phone="1234567890",
                    email=user['email'],
                    profile_image="https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress",
                    birthday=date(1960, 1, 15),
                    info="developer of this website",
                )
            user.save()
        except Exception as e:
            print(f"User ({user.email}) already exists: {e}")

def seed_fakenames():
    for _ in range(2):
        try:
            user = User(
                email = fake.email(),
                first_name = fake.name(),
                last_name = fake.name()
            )
            user.save()
        except Exception as e:
            print(f"User ({user.email}) already exists: {e}")

# def create_user():
#     try:
#         user = User(
#                 first_name="Tutorial",
#                 last_name="Doctor",
#                 email="td123@gmail.com",
#                 profile_image="https://images.prismic.io/upskil/ZrvRh0aF0TcGI6Kq_valley.webp?auto=format,compress",
#                 birthday=date(1960, 1, 15),
#                 info="developer of this website",
#             )
#         user.save()
#     except Exception as e:
#         print(f"User already exists: {e}")

create_db_tables()
seed_db()
# seed_fakenames()
# create_user()

PRIMARY_COLOR = "blue"
BG_COLOR = "#212224"
BORDER_COLOR = "#111214"
CARD_BG = "#131517"


@ft.component
def App():
    users = User.select()
    # print(users)
    return ft.SafeArea(
        content=ft.Container(
            content= Nav(),
            padding=5,
        )
    )

def main(page: ft.Page):
    # page.window.resizable = False
    page.bgcolor = "white"  # Set page background
    # page.window.bgcolor = ft.Colors.TRANSPARENT
    page.window.left=200
    page.window.top=200
    page.window.width = 2117
    page.window.height = 1391
    page.db = "dbname"
    page.window.frameless = True
    page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thickness=0.0))
    width_text = ft.Text(f"Width: {page.width}", size=12)
    height_text = ft.Text(f"Height: {page.height}", size=12)

    async def set_value(e):
        key, value = e.control.data
        await ft.SharedPreferences().set(key, value)
        page.show_dialog(ft.SnackBar(f"Value saved to SharedPreferences: {key}: {value}"))

    async def get_value(e):
        key = e.control.data
        contents = await ft.SharedPreferences().get(key)
        # ft.context.page.add(ft.Text(f"SharedPreferences contents: {contents}"))
        page.show_dialog(ft.SnackBar(f"Got Value From Shared Prefs: {contents}"))

    # Function that fires when the window is resized
    def on_window_resize(e):
        width_text.value = f"Width: {page.width}"
        height_text.value = f"Height: {page.height}"
        width_text.update()
        height_text.update()

    # Bind the resize event to the page
    page.on_resize = on_window_resize

    async def close_app(e):
        await page.window.destroy()
    
    page.appbar = ft.AppBar(
        title=ft.Row(
            [
                ft.Text("Flet App Shell", size=16, color=PRIMARY_COLOR),
                # ft.Button("Set", on_click=set_value,data=("name","Tutorial Doctor")),
                # ft.Button("Get", on_click=get_value,data="name"),
                ft.Row([width_text, height_text]),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        leading=ft.IconButton(icon=ft.Icons.CLOSE, on_click=close_app),
        center_title=True,
    )

    page.bottom_appbar = ft.BottomAppBar(
        content=ft.Row(
            [
                ft.Row([ft.Text("©TDLLC")]),
            ],
            alignment=ft.MainAxisAlignment.END,
        )
    )
    page.render(App)


ft.run(main, assets_dir="src/assets")
