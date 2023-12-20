import reflex as rx 
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(f"©️ 2022-{datetime.date.today().year}-MAUROKEIN BY MAURO KEIN",
                href="https://maurokein.github.io",
                is_external=True),
        rx.text("BUILDING SOFTWARE FROM LA PLATA TO THE WORLD")
    )