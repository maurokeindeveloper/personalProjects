import reflex as rx 
import styles.styles as styles
from styles.colors import Color as Color 
from styles.colors import TextColor as TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("mauro", color=Color.PRIMARY.value),
            rx.span("dev", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0"
    )