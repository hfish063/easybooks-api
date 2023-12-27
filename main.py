"""
Main module for goodreads api/webscraper project
author: haydenfish
"""

from goodreads import GoodReads

def run():
    gr = GoodReads()
    
    while True:
        print("0: terminate program, 1: scan result list, 2: find item key")

        user_input = input("Enter number (0-2): ")

        if user_input == "0":
            break
        elif user_input == "1":
            book_title = input("Enter book title: ")

            results = gr.scan_result_list(book_title)

            for result in results:
                print("Title: {title} Author(s): {author}".format(title=result.title, author=result.author))
        elif user_input == "2":
            book_title = input("Enter book title: ")

            id = gr.find_item_id(book_title)

            print(id)

if __name__ == "__main__":
    run()