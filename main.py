"""
Main module for goodreads api/webscraper project
author: haydenfish
"""

from goodreads import GoodReads

def run():
    gr = GoodReads()
    
    while True:
        print("0: terminate program, 1: scan result list, 2: scan result item, 3: find item key")

        user_input = input("Enter number (0-3): ")

        if user_input == "0":
            break
        elif user_input == "1":
            book_title = input("Enter book title: ")

            results = gr.scan_result_list(book_title)

            for result in results:
                print("Title: {title}\nAuthor(s): {author}\n".format(title=result.title, author=result.author))
        elif user_input == "2":
            book_title = input("Enter book title: ")
            
            result = gr.scan_result_item(book_title)

            if result is not None:
                print(result.title + "\n")
                print(result.author + "\n")
                print(result.description + "\n")
        elif user_input == "3":
            book_title = input("Enter book title: ")

            id = gr.find_item_id(book_title)

            print(id + "\n")

if __name__ == "__main__":
    run()