import reflex as rx
import styles.styles as style

def link_icon(image: str, url: str, alt_text: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            alt=alt_text
        ),
        href=url,
        is_external=True
    )