import tkinter as tk
import pyshorteners
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    shortened_label.configure(text="Shortened URL: " + short_url)
    copy_button.configure(state=tk.NORMAL)
    global copied_url
    copied_url = short_url

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(copied_url)
    messagebox.showinfo("Success", "URL copied to clipboard!")

window = tk.Tk()
window.title("URL Shortener")
window.configure(bg="#e6e6fa")
window_width = 400
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

label = tk.Label(window, text="Enter the long URL:", bg="#e6e6fa", fg="#191970", font=("Helvetica", 14))
label.pack(pady=10)
entry = tk.Entry(window, width=40, font=("Helvetica", 12))
entry.pack()
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url, bg="#9370db", fg="white", font=("Helvetica", 12))
shorten_button.pack(pady=10)
shortened_label = tk.Label(window, text="", bg="#e6e6fa", fg="#191970", font=("Helvetica", 12))
shortened_label.pack()
copy_button = ttk.Button(window, text="Copy URL", state=tk.DISABLED, command=copy_to_clipboard)
copy_button.pack(pady=10)

window.mainloop()
