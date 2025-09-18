
### `/src/playlist.py` (starter)

class _DNode:
    __slots__ = ("title", "prev", "next")
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        ...

    def play_first(self):
        ...

    def next(self):
        ...

    def prev(self):
        ...

    def insert_after_current(self, title):
        ...

    def remove_current(self):
        ...

    def to_list(self):
        ...