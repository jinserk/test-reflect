import reflex as rx


def index() -> rx.Component:
    return rx.text("Hello World!")


app = rx.App()
app.add_page(index)
app.compile()
