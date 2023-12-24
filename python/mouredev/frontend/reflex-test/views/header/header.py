import reflex as rx 
from components.link_icon import link_icon
from components.info_text import info_text 
import styles.styles as styles
from styles.styles import Size as Size
from styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Mauro Kein", size="xl"),
            rx.vstack(
                rx.heading("Mauro Kein", 
                           size="lg",
                           color=TextColor.HEADER.value
                ),
                rx.text("@maurokein",
                        margin_top=Size.ZERO.value,
                        color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://x.com/maurokein"),
                    link_icon("https://instagram.com/maurokein"),
                    link_icon("https://facebook.com/maurokein"),
                ),
                align_items="start",
            ),
            spacing=styles.Size.DEFAULT.value
        ), 
        rx.flex(
            info_text("+6", "años de experiencia docente"),
            rx.spacer(),
            info_text("+8", "años de investigación en ciencias sociales y tecnología"),
            rx.spacer(),
            info_text("+4", "años aprendiendo informática"),
            width="100%"
        ),
            rx.text(
            """Soy Profesor en Letras por la UNLP. Hace 4 años estudio Programación y Desarrollo de Software en la Facultad de Informática. Me gusta enseñar lo que aprendo y relacionar elementos de campos diferentes. A veces escribo. Nunca no estoy leyendo algo.""",
            color=TextColor.BODY.value
        ),
            align_items="start",
            spacing=styles.Size.BIG.value
        )
    