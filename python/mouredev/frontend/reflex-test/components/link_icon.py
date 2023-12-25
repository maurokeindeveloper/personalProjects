import reflex as rx
import styles.styles as style

def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image
        ),
        href=url,
        is_external=True
    )