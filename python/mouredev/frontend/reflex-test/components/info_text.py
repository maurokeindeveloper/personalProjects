import reflex as rx 
from styles.styles import Size as Size
from styles.colors import TextColor as TextColor
from styles.colors import Color as Color 

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )