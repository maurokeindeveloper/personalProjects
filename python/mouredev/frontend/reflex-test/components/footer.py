import reflex as rx 
import datetime
from styles.styles import Size as Size 
from styles.colors import Color as Color 
from styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.jpg",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
            alt="Logotipo de kein_dev. Una \"eme\" y una \"ka\" entrelazadas."
        ),
        rx.link(f"©️ 2022-{datetime.date.today().year}-@maurokein by Mauro Kein",
                href="https://maurokein.github.io",
                is_external=True,
                font_size=Size.MEDIUM.value),
        rx.text("BUILDING SOFTWARE FROM LA PLATA TO THE WORLD",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.SMALL.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )