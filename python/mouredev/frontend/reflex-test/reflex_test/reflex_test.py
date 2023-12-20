import reflex as rx 
from components.navbar import navbar
from views.header.header import header
from views.links.links import links
from components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    ) 

app = rx.App()
app.add_page(index)
app.compile()