import reflex as rx 
from components.title import title as title 
from components.link_sponsor import link_sponsor as sponsor
from styles.styles import Size as Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.responsive_grid(
            sponsor(
                "filo-uba.jpg",
                "http://www.filo.uba.ar"
            ),
            sponsor(
                "fahce-unlp.png",
                "https://www.fahce.unlp.edu.ar"
            ),
            spacing=Size.DEFAULT.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="center"
    )