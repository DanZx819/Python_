import flet as ft

def main(page: ft.Page):
    # adicionar controles na pagina
    page.padding  = 0
    page.window_width = 400
    page.window_height = 550

    page.update()
    page.add(ft.Text('olo'))
    

ft.app(port=8550, target=main)
