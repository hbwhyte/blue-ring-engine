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
        next(csv_reader, None)
        pages = {}
        first_page = "Not Set Yet"
        for row in csv_reader:
            if first_page == "Not Set Yet":
                first_page = row[0]
            choice1 = Choice(row[2], row[3])
            choice2 = Choice(row[4], row[5])
            pages[row[0]] = Page(row[0], row[1], [choice1, choice2])
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
    print(page.page)
    print('----')
    print(page.text+'\n')
    print(f'1. {page.choices[0].choice}')
    print(f'2. {page.choices[1].choice}')

    while True:
        try:
            choice = input('Which do you choose? (1/2) ')
            if choice == '1':
                return page.choices[0].next_page
            if choice == '2':
                return page.choices[1].next_page
            print("Invalid response entered. Do you choose 1 or 2? ")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    start_game()
