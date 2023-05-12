from editor.editorgui import EditWindow

class EditController(EditWindow):
    def __int__(self):
        super().__init__()

if __name__ == "__main__":
    EditController().mainloop()