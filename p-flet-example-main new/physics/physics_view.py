import flet as ft
from flet_core.colors import BLACK12, GREEN

from physics.thermal_phenomena.thermal_phenomena import Get_thermalPhenomena_view


def Get_physics_view(page):
    return ft.View(
        route="/physics",
        controls=[

            ft.AppBar(title=ft.Text("Physics"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("Physics", size=45),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/")),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Thermal phenomena", height=140, width=240, on_click=lambda _: page.go("/physics/thermalPhenomena")),
                    ft.ElevatedButton(text="Electric phenomena"),
                    ft.ElevatedButton(text="Mechanical work and energy"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25,
                ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Pressure.Achimedes law.Interaction of force bodies"),
                    ft.ElevatedButton(text="Mechanical movement"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Library of constant valuse"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=26,
        bgcolor=ft.colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            image=ft.DecorationImage(
                src="physics/physics.jpg",
                fit=ft.ImageFit.COVER,
                opacity=4,
            )
        )
    )
