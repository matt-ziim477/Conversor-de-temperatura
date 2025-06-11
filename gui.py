from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button
import webbrowser

window = Tk()
window.attributes("-fullscreen", True)
window.configure(bg="#183B4E")
window.resizable(False, False)

def exit(event=None):
    window.destroy()
window.bind("<Escape>", exit)

canvas = Canvas(
    window,
    bg="#183B4E",
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.pack(fill="both", expand=True)  

canvas.create_text(
    87.0,
    80.0,
    anchor="nw",
    text="Conversor de temperatura",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 64 * -1)
)

canvas.create_text(
    90.0,
    253.0,
    anchor="nw",
    text="Digite a temperatura em graus celsius:",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 40 * -1)
)

canvas.create_text(
    90.0,
    518.0,
    anchor="nw",
    text="Temperatura em fahrenheit:",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 40 * -1)
)

canvas.create_rectangle(
    90.0,
    319.0,
    916.0,
    413.0,
    fill="#27548A",
    outline=""
)

canvas.create_rectangle(
    87.0,
    574.0,
    913.0,
    668.0,
    fill="#27548A",
    outline=""
)

entry_celsius = Entry(
    bd=0,
    bg="#27548A",
    fg="#FFFFFF",
    font=("Arial", 32),
    highlightthickness=0
)
entry_celsius.place(
    x=100.0,
    y=330.0,
    width=800.0,
    height=60.0
)

label_resultado = Text(
    bd=0,
    bg="#27548A",
    fg="#FFFFFF",
    font=("Arial", 32),
    highlightthickness=0
)
label_resultado.place(
    x=100.0,
    y=585.0,
    width=800.0,
    height=60.0
)
label_resultado.insert("1.0", "")

def converter():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9 / 5) + 32
        label_resultado.delete("1.0", "end")
        label_resultado.insert("1.0", f"{fahrenheit:.2f} °F")
    except ValueError:
        label_resultado.delete("1.0", "end")
        label_resultado.insert("1.0", "Inválido!")

botao_converter = Button(
    text="Converter",
    font=("Arial", 24),
    fg="white",
    bg="#1E6F9F",
    borderwidth=0,
    highlightthickness=0,
    command=converter
)
botao_converter.place(
    x=100.0,
    y=440.0,
    width=300.0,
    height=60.0
)


def adicionar_creditos():
    altura = canvas.winfo_height()
    
    github_text = canvas.create_text(
        20.0,
        altura - 30,  
        anchor="sw",
        text="https://github.com/matt-ziim477",
        fill="#00BFFF",
        font=("Arial", 16),
        activefill="#1E90FF"
    )
    canvas.tag_bind(github_text, "<Button-1>", lambda e: webbrowser.open_new("https://github.com/matt-ziim477"))
    canvas.tag_bind(github_text, "<Enter>", lambda e: canvas.config(cursor="hand2"))
    canvas.tag_bind(github_text, "<Leave>", lambda e: canvas.config(cursor=""))


window.after(100, adicionar_creditos)

window.mainloop()
