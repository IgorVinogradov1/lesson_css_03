
import json
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_book_catalog():
    with open("meta_data.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()
    return json.loads(books_json)

def main():
    load_dotenv()
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
    print("index.html создан!")

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()