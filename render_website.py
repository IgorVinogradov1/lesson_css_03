import json
from livereload import Server
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_book_catalog():
    with open("meta_data.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()
    return json.loads(books_json)

def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        books = get_book_catalog(),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("index.html обновлен!")

def main():
    load_dotenv()

    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')

if __name__ == '__main__':
    main()