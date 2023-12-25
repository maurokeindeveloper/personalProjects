import reflex as rx 
import styles.styles as styles
from styles.styles import Size as Size  

def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            width="180px",
            height="110px",
            src=imagen
        ),
        href=url,
        is_external=True
    )