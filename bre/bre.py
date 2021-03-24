import csv
import sys
import os
from story import *
from engine import *


def init(game_path):
    with open(game_path) as story_file:
        csv_reader = csv.reader(story_file, delimiter=',')
        next(csv_reader, None)  # Skips header row
        pages = {}
        first_page_id = None

        for row in csv_reader:
            page_id = row[0]
            if not first_page_id:
                first_page_id = page_id
            pages[page_id] = Page(page_id, row[1], [])
            col_index = 2

            while col_index < len(row) and row[col_index] != '':
                choice = Choice(row[col_index], row[col_index + 1])
                pages[page_id].choices.append(choice)
                col_index += 2

        story = Story(pages)
        return Book(first_page_id, story, None)  # todo: add metadata


def load_book(game_path):
    while not os.path.isfile(game_path):
        game_path = input("Sorry, we can't seem to find that file. Try again? ")
    print("Story time!")
    return init(game_path)


if __name__ == '__main__':
    path = "data/metal.csv"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    book = load_book(path)

    engine = BlueRingEngine(book)
    engine.play()
