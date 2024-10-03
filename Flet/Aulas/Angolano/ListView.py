import flet as ft

def main(page: ft.Page):
    #Configruando a pagina
    page.title = "Falando sobre ListView"
    page.padding = 0
    page.window.width = 1000
    page.window.height = 550
    page.bgcolor = ft.colors.GREY
    page.update()

    #Criando Container

    c1 = ft.Container(
        content = ft.ElevatedButton("Botão 1"),
        bgcolor = ft.colors.BLACK,
        padding = 10,
        width = 300,

    )

    c2 = ft.Container(
        content = ft.ElevatedButton("Botão 2"),
        bgcolor = ft.colors.BLACK,
        padding = 10,
        width = 300,

    )
    c3 = ft.Container(
        content = ft.ElevatedButton("Botão 3"),
        bgcolor = ft.colors.BLACK,
        padding = 10,
        width = 300,

    )
    #Criando Lista

    item = [c1]
    item2 = [c1, c2, c3]
    #Criando Row

    row = ft.Row(spacing=10, controls= item2)

    #Criando Coluna

    colum = ft.Column(spacing=10, controls=item2)

    #Criando uma ListView

    lv = ft.ListView(expand=1, spacing= 10, padding=20, auto_scroll=True)
    
    lv.controls.append(ft.Text("Ola mundo"))
    lv.controls.append(colum)


    
    #Criando Grid View
    gv = ft.GridView(
        expand = 1, runs_count = 5, max_extent = 150, child_aspect_ratio = 1.0, spacing= 10, run_spacing=5,
        )
    gv.controls.append(colum)
    

    page.add(lv, gv)
ft.app(target=main)