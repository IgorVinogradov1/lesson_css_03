import os
import argparse
import json
from livereload import Server
from dotenv import load_dotenv
from more_itertools import chunked
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_book_catalog(books_per_page, file_path):
    with open(file_path, 'r', encoding='utf-8') as my_file:
        books_data = json.load(my_file)
    return list(chunked(books_data, books_per_page))

def on_reload(books_catalog):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    number_of_pages = len(books_catalog)
    for index, books_chunk in enumerate(books_catalog, start=1):
        rendered_page = template.render(
            books = books_chunk,
            number_of_pages = number_of_pages,
            current_page = index,
        )
        with open(f'pages/index{index}.html', 'w', encoding='utf8') as file:
            file.write(rendered_page)

def main():
    load_dotenv()
    os.makedirs('pages', mode=0o755, exist_ok=True)

    parser = argparse.ArgumentParser(description='Загрузка пользовательского файла с данными')
    parser.add_argument('--file', '-f', nargs='?', default='meta_data.json', help='Укажите путь к файлу (по умолчанию: meta_data.json)')
    parser.add_argument('--books-per-page', '-p', type=int, default=20, help='Укажите количество книг на странице (по умолчанию: 20)')
    args = parser.parse_args()
    file_path = args.file
    books_per_page = args.books_per_page
    
    try:
        books_catalog = get_book_catalog(books_per_page, file_path)
    except FileNotFoundError:
        parser.error(f'файл с данными не найден')
    except json.JSONDecodeError as error:
        parser.error(f'некорректный json-файл')

    on_reload(books_catalog)
    server = Server()
    server.watch('template.html', lambda: on_reload(books_catalog))
    server.serve(root='.')

if __name__ == '__main__':
    main()