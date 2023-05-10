from threading import Thread
from controller import Controller

__author__ = "opeezy17"
__version__ = "0.1.0"

if __name__ == "__main__":
	app = Controller(__version__)
	app.mainloop()
