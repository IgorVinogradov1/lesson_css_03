# Онлайн-библиотека

Учебный проект: верстка онлайн-библиотеки книг с оффлайн-версией.

**Опубликованная версия:** [GitHub Pages](https://igorvinogradov1.github.io/lesson_css_03/pages/index1.html)
**Репозиторий:** [GitHub](https://github.com/IgorVinogradov1/lesson_css_03)
**Курс:** [Девман — Верстаем онлайн-библиотеку](https://dvmn.org/modules/website-layout-for-pydev/lesson/books-library-restyle-3/)

---

## Что это?

Онлайн-библиотека книг с пагинацией. Карточка книги: фото, название, автор, жанр. Ссылка «Читать» → текст книги. Оффлайн-версия работает локально без интернета.

---

## Как использовать

### Хочу скачать библиотеку

1. Перейдите на репозиторий: [GitHub](https://github.com/IgorVinogradov1/lesson_css_03)
2. Нажмите **`Code`** → **`Download ZIP`**.
3. Распакуйте.
4. Откройте `pages/index1.html` в браузере.
5. Выберите книгу → кликните **«Читать»**.

---

### Хочу посмотреть опубликованную версию

1. Перейдите на сайт: [GitHub Pages](https://igorvinogradov1.github.io/lesson_css_03/pages/index1.html)
2. Покликайте навигацию, проверьте работу

---

### Хочу развернуть проект локально

1. Скачать репозиторий:
```
git clone https://github.com/IgorVinogradov1/lesson_css_03
cd lesson_css_03
```

2. Установить зависимости:
```
pip install -r requirements.txt
```

3. Запустить сервер:
```
python render-website.py
```

4. Открыть в браузере: `http://127.0.0.1:5500`

---

## Источник данных

Файл: `meta_data.json` (JSON)  
Каталоги: `books/` (тексты книг), `img/` (фото)

**Пример объекта:**
```json
{
  "title": "Название книги",
  "author": "Имя автора",
  "genres": "Жанр 1, Жанр 2",
  "img_src": "book1.jpg",
  "book_path": "books/book1.txt"
}
```