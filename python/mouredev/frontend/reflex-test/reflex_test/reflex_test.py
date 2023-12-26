import reflex as rx 
from components.navbar import navbar
from views.header.header import header
from views.links.links import links
from components.footer import footer
import styles.styles as styles
from styles.styles import Size as Size
from views.sponsors.sponsors import sponsors as sponsors

""" BACKEND-SIDE """
""" class State(rx.State):
    pass """

""" FRONTEND-SIDE """
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=Size.BIG.value 
            )
        ), 
        footer()
    ) 



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="kein_dev | Programación y H++",
    description="Mi nombre es Mauro Kein, me especializo en Desarrollo de Software con Python y en Humanidades Digitales",
    image="logo.jpg"
)
app.compile()