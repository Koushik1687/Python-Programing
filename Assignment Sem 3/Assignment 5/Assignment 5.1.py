# WAP: Chatbot Code
from tkinter import *

def send():
    user_msg = "You: " + e.get()
    text.insert(END, "\n" + user_msg)

    msg = e.get().lower()

    if msg == 'hi':
        text.insert(END, "\nBot: hello")

    elif msg == 'hello':
        text.insert(END, "\nBot: hi")

    elif msg == 'how are you?':
        text.insert(END, "\nBot: I'm fine, and you?")

    elif msg == "i'm fine too" or msg == "im fine too":
        text.insert(END, "\nBot: Nice to hear that.")

    else:
        text.insert(END, "\nBot: Sorry, I didn't get it.")

    e.delete(0, END)

root = Tk()
root.title('Simple Chatbot')
root.geometry("500x500")

text = Text(root, bg='light blue')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_btn = Button(root, text='Send', bg='blue', width=20, command=send)
send_btn.grid(row=1, column=1)

root.mainloop()
