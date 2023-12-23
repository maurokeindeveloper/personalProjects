import reflex as rx 
import styles.styles as styles

def link_button(text: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward"

                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(text, style=styles.button_body_style)
                )
            )
        ),
        href=link,
        is_external=True,
        width="100%",
    )

    return rx.link(
        rx.button(text, width="100%"),
        href=link,
        is_external=True,
        width="100%"
    )