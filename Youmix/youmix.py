from threading import Thread
from controller import Controller

__title__ = "YouMix"
__author__ = "Chris Openshaw, Blake Calhoun"
__version__ = "0.1.0"

if __name__ == "__main__":
	app = Controller(__version__)
	app.mainloop()
