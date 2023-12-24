import reflex as rx 
from components.link_button import link_button
import styles.styles as styles
from components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", 
                    "Directos para conversar sobre Humanidades Digitales", 
                    "https://twitch.tv/algoritmozero"),
        link_button("Instagram", 
                    "Aplicaciones de Python en las Ciencias Sociales", 
                    "https://instagram.com/maurokein"),
        link_button("XTwitter", 
                    "Todas las novedades del mundo sociotecnocultural",
                    "https://x.com/maurokein"),
        link_button("Discord", 
                    "Canal para compartir recursos con la comunidad",
                    "https://discord.com/mauro_on_an_island_06551"),
        title("Recursos y más"),
        link_button("Web de presentación de proyectos", 
                    "Acá podés ver los proyectos en HD y Desarrollo de Software", 
                    "https://maurokein.github.io"),
        link_button("Ensayos", 
                    "Escritos sobre tecnocultura", 
                    "https://tecnocultura-unlp.github.io/blog_linktr.ee"),
        link_button("Lista de libros", 
                    "Actualización semana a semana de lecturas terminadas",
                    "https://maurokein.github.io/lecturas"),
        link_button("Locx, no te sobra una moneda?", 
                    "Podés ayudarme a seguir creando contenido",
                    "https://mercadopago.com.ar"),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "https://mypublicinbox.com/maurokein"
        ),
        link_button(
            "Email",
            "maurokein1990@gmail.com",
            f"mailto:{styles.mail_direction}"
        ),
        width="100%",
        spacing=styles.Size.MEDIUM.value
        )