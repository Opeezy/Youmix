from typing import Optional, List
from editor.editorgui import EditWindow

class EditController(EditWindow):
    def __init__(self, streams: Optional[List[str]] = None) -> None:
        super().__init__(streams)


if __name__ == "__main__":
    pass