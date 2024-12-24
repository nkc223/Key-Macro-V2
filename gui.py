from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from main import StartMacro, StopMacro
import keyboard

def StartMacroGUI():
    key = entry_1.get()
    interval = entry_2.get()
    StartMacro(key, interval, canvas, Tip)

def StopMacroGUI():
    StopMacro()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\voidd\Desktop\Key-Macro-2.0\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("Key Macro v2.0")
window.geometry("400x180")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 180,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    25.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    126.0,
    80.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    126.0,
    129.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    157.5,
    80.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=113.0,
    y=71.0,
    width=89.0,
    height=16.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    166.5,
    129.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=126.0,
    y=120.0,
    width=81.0,
    height=16.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: StartMacroGUI(),
    relief="flat"
)
button_1.place(
    x=243.0,
    y=87.0,
    width=141.0,
    height=32.0
)

Tip = canvas.create_text(
    251.0,
    122.0,
    anchor="nw",
    text="",
    fill="#3F3F3F",
    font=("Inter ExtraLightItalic", 14 * -1)
)

window.resizable(False, False)
window.mainloop()