import csv


class Story:
    def __init__(self, pages, current_page):
        self.pages = pages
        self.current_page = current_page


class Page:
    def __init__(self, page, text, choices):
        self.page = page
        self.text = text
        self.choices = choices


class Choice:
    def __init__(self, choice, next_page):
        self.choice = choice
        self.next_page = next_page


def init():
    with open("data/sample.csv") as story_file:
        csv_reader = csv.reader(story_file, delimiter=',')
        next(csv_reader, None)  # Skips header row
        pages = {}
        first_page = "Not Set Yet"

        for row in csv_reader:
            page_id = row[0]
            if first_page == "Not Set Yet":
                first_page = page_id
            pages[page_id] = Page(page_id, row[1], [])
            col_index = 2

            while col_index < len(row) and row[col_index] != '':
                choice = Choice(row[col_index], row[col_index+1])
                pages[page_id].choices.append(choice)
                col_index += 2

        story = Story(pages, first_page)
        return story


def start_game():
    print("Start the game!")
    story = init()
    next_page = show_options(story.pages[story.current_page])
    while next_page is not '':
        next_page = show_options(story.pages[next_page])
    print("Game over!")


def show_options(page):
    print(f'\n{page.page}')
    print(f'---- \n{page.text}')

    while len(page.choices) > 0:
        print()
        for i, choice in enumerate(page.choices):
            print(f'{i + 1}. {choice.choice}')

        selection = input("Which do you choose? ")

        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(page.choices):
                return page.choices[int(selection)-1].next_page
            else:
                print("\tSorry, didn't get that. Please enter one of the numbers listed. ")
        else:
            print(f'\tWhat are you going on about?? {selection} is not a valid number. ')

    return ''


if __name__ == '__main__':
    start_game()
