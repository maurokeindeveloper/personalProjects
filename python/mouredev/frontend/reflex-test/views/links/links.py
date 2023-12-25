import reflex as rx 
from components.link_button import link_button
import styles.styles as styles
from components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", 
                    "Directos para conversar sobre Humanidades Digitales",
                    "icons/twitch.svg", 
                    "https://twitch.tv/algoritmozero"),
        link_button("Instagram", 
                    "Aplicaciones de Python en las Ciencias Sociales", 
                    "icons/instagram.svg", 
                    "https://instagram.com/maurokein"),
        link_button("XTwitter", 
                    "Todas las novedades en el mundo de la tecnocultura",
                    "icons/square-x-twitter.svg", 
                    "https://x.com/maurokein"),
        link_button("Discord", 
                    "Canal para compartir recursos con la comunidad",
                    "icons/discord.svg", 
                    "https://discord.com/mauro_on_an_island_06551"),
        title("Recursos y más"),
        link_button("Web de presentación de proyectos", 
                    "Distintos proyectos en Humanidades Digitales y Desarrollo de Software", 
                    "icons/github.svg", 
                    "https://maurokein.github.io"),
        link_button("Artículos", 
                    "Escritos sobre tecnocultura",
                    "icons/blog-solid.svg",  
                    "https://tecnocultura-unlp.github.io/blog_linktr.ee"),
        link_button("Lista de libros", 
                    "Actualización semana a semana de lecturas terminadas",
                    "icons/book-solid.svg", 
                    "https://maurokein.github.io/lecturas"),
        link_button("Locx, no te sobra una moneda?", 
                    "Podés ayudarme a seguir creando contenido",
                    "icons/mug-hot-solid.svg", 
                    "https://mercadopago.com.ar"),
        title("Contacto"),
        link_button(
            "MyPublicInbox: maurokein",
            "Respuesta rápida y con preferencia",
            "icons/inbox-solid.svg", 
            "https://mypublicinbox.com"
        ),
        link_button(
            "Email",
            "maurokein1990@gmail.com",
            "icons/envelope-solid.svg", 
            "https://mail.google.com"
        ),
        width="100%",
        align_items="start",
        spacing=styles.Size.MEDIUM.value
        )