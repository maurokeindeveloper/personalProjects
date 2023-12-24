import reflex as rx 
from components.link_button import link_button
import styles.styles as styles
from components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", 
                    "Directos lunes, miércoles y viernes", 
                    "https://twitch.tv/algoritmozero"),
        link_button("Instagram", 
                    "Posts sobre aprendizaje de Python", 
                    "https://instagram.com/maurokein"),
        link_button("XTwitter", 
                    "Todas las novedades y actualizaciones",
                    "https://x.com/maurokein"),
        link_button("Discord", 
                    "Canal para compartir con la comunidad",
                    "https://discord.com/mauro_on_an_island_06551"),
        title("Comunidad"),
        link_button("Twitch", 
                    "Directos lunes, miércoles y viernes", 
                    "https://twitch.tv/algoritmozero"),
        link_button("Instagram", 
                    "Posts sobre aprendizaje de Python", 
                    "https://instagram.com/maurokein"),
        link_button("XTwitter", 
                    "Todas las novedades y actualizaciones",
                    "https://x.com/maurokein"),
        link_button("Discord", 
                    "Canal para compartir con la comunidad",
                    "https://discord.com/mauro_on_an_island_06551"),
        width="100%"
        )