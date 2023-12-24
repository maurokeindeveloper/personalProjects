import reflex as rx 
import styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Mauro Kein",
        ),
        position="sticky",
        bg="lightgray",
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0"
    )