#!/usr/bin/env python3

#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
    
    def get_page(self):
        return self._page_count
    
    def set_page(self, pagecount):
        if not isinstance(pagecount, int):
            print("page_count must be an integer")
        else:
            self._page_count = pagecount

    page_count = property(get_page, set_page)

    def turn_page(self):
        if isinstance(self.page_count, int):
            print("Flipping the page...wow, you read fast!")
        else:
            print("Cannot turn page. Page count is not an integer.")

# Example usage:
book = Book("And Then There Were None", 123)
book.page_count = "1256"
print(f"Title: '{book.title}' with page count: {book.page_count}")
book.turn_page()

    