import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Homework 3.3"
    
    name_input = ft.TextField(label="Введите ваше имя")
    result = ft.Text(value="", color=ft.Colors.BLUE)
    
    def on_submit(e):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        
        if name:
            result.value = f"{timestamp} - Привет, {name}!"
            result.color = ft.Colors.GREEN
        else:
            result.value = "Пожалуйста, введите ваше имя!"
            result.color = ft.Colors.RED
        
        page.update()
    
    name_input.on_submit = on_submit
    
    page.add(name_input, result)

ft.app(target=main, view=ft.WEB_BROWSER)