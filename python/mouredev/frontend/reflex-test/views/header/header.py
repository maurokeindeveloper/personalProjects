import reflex as rx 
from components.link_icon import link_icon
from components.info_text import info_text 
import styles.styles as styles
from styles.styles import Size as Size
from styles.colors import TextColor as TextColor
from styles.colors import Color as Color
from styles.fonts import Font as Font 


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Mauro Kein", 
                size="xl",
                src="profile.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading("Mauro Kein",
                           size="lg"),
                rx.text("@maurokein",
                        margin_top=Size.ZERO.value,
                        color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/square-x-twitter.svg", 
                        "https://x.com/maurokein",
                        "X-Twitter"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        "https://instagram.com/maurokein",
                        "Instagram"
                    ),
                    link_icon(
                        "icons/facebook.svg",
                        "https://facebook.com/maurokein",
                        "Facebook"    
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        "https://linkedin.com/in/maurokein",
                        "Linkedin"
                    ),
                    spacing=Size.LARGE.value
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
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value
        ),
            align_items="start",
            spacing=styles.Size.BIG.value
        )
    