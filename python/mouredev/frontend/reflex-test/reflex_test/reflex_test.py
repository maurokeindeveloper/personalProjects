import reflex as rx 
from components.navbar import navbar
from views.header.header import header
from views.links.links import links
from components.footer import footer
import styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        ), 
        footer()
    ) 



app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.compile()