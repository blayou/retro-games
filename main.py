from tkinter import *
import pathlib

filesPath = str(pathlib.Path(__file__).parent.absolute()) + "\\mainfiles"
filesPath = filesPath.replace("\\",'/')

window = Tk()
window.title("Jeux rétro")
window.geometry("1280x720")
window.minsize(1280, 720)
window.iconbitmap(filesPath + "/logo.ico")