import reflex as rx 
import datetime
from styles.styles import Size as Size 

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(f"©️ 2022-{datetime.date.today().year}-@maurokein by Mauro Kein",
                href="https://maurokein.github.io",
                is_external=True,
                font_size=Size.MEDIUM.value),
        rx.text("BUILDING SOFTWARE FROM LA PLATA TO THE WORLD",
                font_size=Size.MEDIUM.value,
                margin_top="0px !important"),
                margin_bottom=Size.BIG.value,
    )