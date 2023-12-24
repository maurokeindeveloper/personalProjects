import reflex as rx 
from components.link_icon import link_icon
import styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Mauro Kein", size="xl"),
            rx.vstack(
                rx.heading("Mauro Kein", 
                           size="lg"
                ),
                rx.text("@maurokein",
                        margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://x.com/maurokein"),
                    link_icon("https://instagram.com/maurokein"),
                    link_icon("https://facebook.com/maurokein")
                ),
                align_items="start"
            )
        ), 
        rx.text("""Soy Profesor en Letras por la UNLP. Hace 4 años estudio Programación y Desarrollo de Software en la Facultad de Informática. Me gusta enseñar lo que aprendo y relacionar elementos de campos diferentes. A veces escribo. Nunca no estoy leyendo algo."""),
        align_items="start",
        spacing=styles.Size.BIG.value
        )