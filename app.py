import tkinter as tk
from chatbot import get_response

def send_message():
    user_text = user_entry.get()
    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_text + "\n")
    response = get_response(user_text)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    user_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Ankit Personal Chatbot 🤖")
root.geometry("500x500")

# Chat box
chat_box = tk.Text(root, height=20, width=60)
chat_box.pack(pady=10)

# User input
user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()
