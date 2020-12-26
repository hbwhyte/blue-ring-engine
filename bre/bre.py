import csv


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
        return pages[first_page]


def start_game():
    print("Start the game!")
    first_page = init()
    print(first_page.text)
    print("Game over!")


if __name__ == '__main__':
    start_game()
