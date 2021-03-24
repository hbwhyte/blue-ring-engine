def display_page(page):
    """Display content on the screen"""
    print(f'\n{page.id}')
    print(f'---- \n{page.text}')

    if len(page.choices) > 0:
        print()
        for i, choice in enumerate(page.choices):
            print(f'{i + 1}. {choice.text}')


def game_over():
    """Display the game over message"""
    print("Game over!")
