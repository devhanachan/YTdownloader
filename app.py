from tkinter import Tk, Label, Text, Button, messagebox, Frame
from PIL import ImageTk, Image
import urllib.request, io
import logic

app = Tk()
app.geometry('420x500')
app.title("YTdownloader")

Label(app, text='Enter YouTube URL:', pady=10, font=("Arial", 12)).pack()

textbox = Text(app, height=1, width=40)
textbox.pack()

# card container
card = Frame(app, bd=2, relief="groove", padx=10, pady=10)
card.pack(pady=20, fill="both")

thumbnail_label = Label(card)
thumbnail_label.pack()

title_label = Label(card, text="", font=("Arial", 11, "bold"), wraplength=350, justify="left")
title_label.pack(pady=5)

info_label = Label(card, text="", font=("Arial", 10), justify="left")
info_label.pack()


def show_image(url):
    with urllib.request.urlopen(url) as u:
        data = u.read()
        img = Image.open(io.BytesIO(data)).resize((320, 180))
        tk_img = ImageTk.PhotoImage(img)
        thumbnail_label.config(image=tk_img)
        thumbnail_label.image = tk_img


def submit():
    url = textbox.get("1.0", "end-1c").strip()
    
    if not url:
        messagebox.showerror("Error", "Please enter URL")
        return

    data = logic.get_video_info(url)

    if "error" in data:
        messagebox.showerror("Error", data["error"])
        return

    # title
    title_label.config(text=data["title"])

    # thumbnail
    if data["thumbnail"]:
        try:
            show_image(data["thumbnail"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load thumbnail:\n{e}")

    # format views
    views = f"{data['views']:,}" if data["views"] else "Unknown"

    # format date
    date = data["upload_date"]
    if len(date) == 8:
        date = f"{date[:4]}-{date[4:6]}-{date[6:]}"

    # format duration
    mins = data["duration"] // 60
    secs = data["duration"] % 60
    dur_text = f"{mins}m {secs}s"

    # format likes
    likes= data['likes']
    info_text = (
        f"Channel: {data['channel']}\n"
        f"Views: {views}\n"
        f"Uploaded: {date}\n"
        f"Duration: {dur_text}\n"
        f"Likes: {likes}\n"
    )

    info_label.config(text=info_text)


Button(app, text="Submit", width=20, command=submit).pack(pady=10)

app.mainloop()
