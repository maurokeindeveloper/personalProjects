import reflex as rx 
from components.navbar import navbar
from views.header.header import header
from views.links.links import links
from components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width="600px",
                width="100% "
            )
        ), 
        footer()
    ) 



app = rx.App()
app.add_page(index)
app.compile()