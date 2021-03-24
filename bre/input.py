def get_input(page):
    if len(page.choices) > 0:
        selection = input("Which do you choose? ")

        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(page.choices):
                return page.choices[int(selection) - 1].next_page_id
            else:
                print("\tSorry, didn't get that. Please enter one of the numbers listed. ")
        else:
            print(f'\tWhat are you going on about?? {selection} is not a valid number. ')
    return None

