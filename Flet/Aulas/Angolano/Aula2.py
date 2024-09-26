import flet as ft

def main(page: ft.Page):
    #Configuração da pagina
    page.title = "Falando sobre row e column"
    page.window.width = 750
    page.window.height = 550
    page.padding = 0

    page.update()
    # Criando Containers
    c1 = ft.Container(
        content = ft.ElevatedButton("Botão"),
        bgcolor = ft.colors.LIGHT_BLUE,
        padding = 10,
        width = 300,
    )
    c2 = ft.Container(
        content = ft.ElevatedButton("Botão"),
        bgcolor = ft.colors.LIGHT_BLUE,
        padding = 10,
        width = 300,
    )
    c3 = ft.Container(
        content = ft.ElevatedButton("Botão"),
        bgcolor = ft.colors.LIGHT_BLUE,
        padding = 10,
        width = 300,
    )
    # Lista de elementos
    
    item = [c1, c2, c3]

    # Criando row
    
    row = ft.Row(spacing=10, controls = item)
    
    # Criando coluna

    coluna = ft.Column(spacing=10, controls = item)

    # Criando Stack

    stack = ft.Stack(
        [
            ft.ElevatedButton("Botão stack"),
            ft.Image(
                src = f"Flet\Aulas\Angolano\isso.png",
                width = 150,
                height = 150,
                
            ),
        ],
        width = 300,
        height = 300
        
    )
    
    # Adicionando o container
    page.add(row, coluna, stack)
    
ft.app(target=main)