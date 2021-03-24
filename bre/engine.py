import display
import input as input_manager


class BlueRingEngine:
    def __init__(self, book):
        self.book = book
        self.next_page_id = self.book.first_page_id
        self.running = False

    def play(self):
        story = self.book.story
        self.running = True
        while self.running:
            next_page = story.pages[self.next_page_id]
            display.display_page(next_page)
            self.next_page_id = input_manager.get_input(next_page)
            self.running = self.next_page_id is not None
        display.game_over()

