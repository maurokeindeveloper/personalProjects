import reflex as rx 
import styles.styles as styles

def link_button(title: str, body: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value

                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start"
                )
            )
        ),
        href=link,
        is_external=True,
        width="100%",
    )