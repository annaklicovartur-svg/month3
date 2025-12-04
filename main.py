import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.tite = 'My first app'
    greeting_text = ft.Text(value='Hello wrold', color=ft.Colors.RED)
    
    # greeting_text.value = 'Hi'
    # greeting_text.Colors = ft.Colors.GREEN
    def one_button_click(_):
        
        name = name_input.value.strip()

        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S") 
        if name:
            greeting_text.value  = f'{timestamp}Hello {name}'
            greeting_text.color = None
            name_input.value = None   
        else:
            greeting_text.value = 'Enter correct name'
            greeting_text.color = ft.Colors.RED
        
        page.update()

    name_input = ft.TextField(label='enter your name', on_submit=one_button_click)
    button_text = ft.TextButton(text='Send', on_click=one_button_click)
    button_elevated = ft.ElevatedButton(text='Send', on_click=one_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=one_button_click)

    page.add(greeting_text, name_input, button_text, button_elevated, button_icon)

    

    # page.ubdate()

ft.app(target=main, view=ft.WEB_BROWSER)