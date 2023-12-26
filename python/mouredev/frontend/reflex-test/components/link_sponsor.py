import reflex as rx 
import styles.styles as styles
from styles.styles import Size as Size  

def link_sponsor(imagen: str, url: str, alt_text: str) -> rx.Component:
    return rx.link(
        rx.image(
            height="110px",
            width="200px",
            src=imagen, 
            alt=alt_text
        ),
        href=url,
        is_external=True
    )