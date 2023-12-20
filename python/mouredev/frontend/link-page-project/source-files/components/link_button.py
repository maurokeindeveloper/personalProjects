import reflex as rx 

def link_button(text: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=link,
        is_external=True
    )
