class Book:
    """A Blue Ring Engine Book.

     It contains the Story itself and Metadata about it."""

    def __init__(self, first_page_id, story, metadata):
        self.first_page_id = first_page_id
        self.story = story
        self.metadata = metadata


class Story:
    """The Story content itself.

    It is a dictionary of page ids to Pages."""

    def __init__(self, pages):
        self.pages = pages


class Metadata:
    """Metadata about the story.

    For example, author, title etc."""

    pass


class Page:
    """An individual Page in a BRE story.

    A page contains a page id, the page text itself, and a list of Choices."""

    def __init__(self, page_id, text, choices):
        self.id = page_id
        self.text = text
        self.choices = choices


class Choice:
    """An individual Choice in a BRE Page.

    The choice has text and the the """
    def __init__(self, text, next_page_id):
        self.text = text
        self.next_page_id = next_page_id
