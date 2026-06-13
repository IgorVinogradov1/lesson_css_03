import os
import json
from livereload import Server
from dotenv import load_dotenv
from more_itertools import chunked
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_book_catalog():
    with open("meta_data.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()
    books_data = json.loads(books_json)
    return list(chunked(books_data, 20))

def on_reload(books_catalog):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    for index, books_chunk in enumerate(books_catalog, start=1):
        rendered_page = template.render(
            books = books_chunk,
        )
        with open(f'pages/index{index}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
        print(f"index{index}.html обновлен!")

def main():
    load_dotenv()
    os.makedirs('pages', mode=0o755, exist_ok=True)
    books_catalog = get_book_catalog()
    on_reload(books_catalog)
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')

if __name__ == '__main__':
    main()