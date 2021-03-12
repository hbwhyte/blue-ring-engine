import csv
import sys
import os
from story import *


def init(game_path):
    with open(game_path) as story_file:
        csv_reader = csv.reader(story_file, delimiter=',')
        next(csv_reader, None)  # Skips header row
        pages = {}
        first_page_id = "Not Set Yet"

        for row in csv_reader:
            page_id = row[0]
            if first_page_id == "Not Set Yet":
                first_page_id = page_id
            pages[page_id] = Page(page_id, row[1], [])
            col_index = 2

            while col_index < len(row) and row[col_index] != '':
                choice = Choice(row[col_index], row[col_index+1])
                pages[page_id].choices.append(choice)
                col_index += 2

        story = Story(pages)
        book = Book(first_page_id, story, None)  # todo: add metadata

        return book


def start_game(game_path):
    while not os.path.isfile(game_path):
        game_path = input("Sorry, we can't seem to find that file. Try again? ")
    print("Story time!")
    book = init(game_path)
    story = book.story
    next_page_id = show_options(story.pages[book.first_page_id])
    while next_page_id is not '':
        next_page_id = show_options(story.pages[next_page_id])
    print("Game over!")


def show_options(page):
    print(f'\n{page.id}')
    print(f'---- \n{page.text}')

    while len(page.choices) > 0:
        print()
        for i, choice in enumerate(page.choices):
            print(f'{i + 1}. {choice.text}')

        selection = input("Which do you choose? ")

        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(page.choices):
                return page.choices[int(selection)-1].next_page_id
            else:
                print("\tSorry, didn't get that. Please enter one of the numbers listed. ")
        else:
            print(f'\tWhat are you going on about?? {selection} is not a valid number. ')

    return ''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        start_game(sys.argv[1])
    else:
        start_game("data/metal.csv")
