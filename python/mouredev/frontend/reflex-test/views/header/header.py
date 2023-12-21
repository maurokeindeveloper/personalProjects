import reflex as rx 

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Mauro Kein", size="xl"),
        rx.text("@maurokein"),
        rx.text("HOLA 👋, MI NOMBRE ES MAURO KEIN"),
        rx.text("""Soy Profesor en Letras por la UNLP. Hace 4 años estudio Programación y Desarrollo de Software 
                en la Facultad de Informática. Me gusta enseñar lo que aprendo y relacionar elementos de mundos diferentes.
                A veces escribo. Nunca no estoy leyendo algo.""")
        )