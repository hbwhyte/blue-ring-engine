import csv


def init():
    with open("data/sample.csv") as story_file:
        csv_reader = csv.reader(story_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'Page {row[0]} scenario is: {row[1]}')
                line_count += 1
        print(f'Processed {line_count} pages')


def start_game():
    print("Start the game!")
    init()
    print("Game over!")


if __name__ == '__main__':
    start_game()
