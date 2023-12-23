import reflex as rx 
from components.link_button import link_button
import styles.styles as styles

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://twitch.tv/algoritmozero"),
        link_button("Instagram", "https://instagram.com/maurokein"),
        link_button("XTwitter", "https://x.com/maurokein"),
        link_button("Discord", "https://discord.com/mauro_on_an_island_06551"),
        width=styles.MAX_WIDTH
    )