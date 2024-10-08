import flet as ft

def main(page: ft.Page):
    #Configurando Página
    page.title = "Responsive Row"
    page.window.width = 1000
    page.window.height = 550
    page.update()

    #Função para contar o redimensionamento 
    def on_resize(e):
        # Atualizando o texto com a largura e altura da janela
        tamanho_janela.value = f"Largura: {page.window_width}, Altura: {page.window_height}"
        page.update()

    # Criando o componente de texto para mostrar o tamanho da janela
    tamanho_janela = ft.Text(f"Largura: {page.window_width}, Altura: {page.window_height}")

    # Definindo a função que será chamada ao redimensionar a janela
    page.on_resize = on_resize

    


    #Criando o Responsive Row
    res = ft.ResponsiveRow
    controls=[(
        ft.Column(col={"sm":6}, controls = [ft.Text("Coluna 1")]),
        ft.Column(col={"sm":6}, controls = [ft.Text("Coluna 2")])
    )]

    pw = ft.Text(bottom=50, right=50, style='displaysmall')
    page.overlay.append(pw)
    
    #Adicionando conteudo na página
    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text("Coluna 1"),
                    padding = 5,
                    bgcolor = ft.colors.YELLOW,
                    col = {'sm':6, "md":4, "xl":2},
                ),

                ft.Container(
                    ft.Text("Coluna 2"),
                    padding = 5,
                    bgcolor = ft.colors.GREEN,
                    col = {'sm':6, "md":4, "xl":2},
                ),
                    ft.Container(
                    ft.Text("Coluna 3"),
                    padding = 5,
                    bgcolor = ft.colors.BLUE,
                    col = {'sm':6, "md":4, "xl":2},
                ),
                ft.Container(
                    ft.Text("Coluna 4"),
                    padding = 5,
                    bgcolor = ft.colors.PINK_300,
                    col = {'sm':6, "md":4, "xl":2}
                )
                
            ]
        )

    )
    # Adicionando o texto à página
    page.add(tamanho_janela)
ft.app(target=main)