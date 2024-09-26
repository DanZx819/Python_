import flet as ft

def main(page: ft.Page):
    # adicionar controles na pagina
    page.title = "Falando sobre container"
    page.padding  = 0
    page.window.width = 400
    page.window.height = 550

    page.update()
    # Criando o container
    c1 = ft.Container(
        content =  ft.ElevatedButton("Botão elevado no container"),
        bgcolor = ft.colors.YELLOW,
        padding = 10, 
        margin = 5,
        width = 300,
        
    )
    c2 = ft.Container(
        content =  ft.ElevatedButton("Botão elevado no container"),
        bgcolor = ft.colors.GREEN,
        padding = 10, 
        margin = 5,
        width = 300,
        
    )
    c3 = ft.Container(
        content =  ft.ElevatedButton("Botão elevado no container"),
        bgcolor = ft.colors.RED,
        padding = 10, 
        margin = 5,
        width = 300,
        
    )
    # adicionando o container
    page.add(c1, c2, c3)
    

ft.app(target=main)
