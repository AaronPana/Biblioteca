""" 'Biblioteca' Proyect """

from flet import Page, Text
import flet as ft


def main(page: Page) -> None:
    """Main function"""
    txt_hello: Text = ft.Text("Hello again, Flet!!")
    page.add(txt_hello)


if __name__ == "__main__":
    ft.app(target=main)
# end main
