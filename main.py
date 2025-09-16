import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # To handle non-GIF image formats
import requests  # Import the requests library to send data to the webhook

def on_login_click():
    username = entry_username.get()
    password = entry_password.get()
    
    # Check if username and password are both "admin"
    if username == "admin" and password == "admin":
        show_spammer_form()  # Proceed to webhook spammer interface
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password!")

def show_spammer_form():
    # Clear the login form
    for widget in root.winfo_children():
        widget.destroy()

    # Display the Webhook Spammer form
    label_webhook = tk.Label(root, text="Enter Webhook URL:", fg="white", bg="black")
    label_webhook.pack(pady=5)

    entry_webhook = tk.Entry(root, fg="black", bg="white")
    entry_webhook.pack(pady=5)

    # Update the label text here to "Enter Message"
    label_message = tk.Label(root, text="Enter Message:", fg="white", bg="black")
    label_message.pack(pady=5)

    entry_message = tk.Entry(root, fg="black", bg="white")
    entry_message.pack(pady=5)

    label_times = tk.Label(root, text="Enter times to spam:", fg="white", bg="black")
    label_times.pack(pady=5)

    entry_times = tk.Entry(root, fg="black", bg="white")
    entry_times.pack(pady=5)

    def send_message():
        webhook_url = entry_webhook.get()
        message = entry_message.get()
        times = entry_times.get()

        try:
            times = int(times)
            if webhook_url and message and times > 0:
                print(f"Webhook URL: {webhook_url}")
                print(f"Message: {message}")
                print(f"Times to spam: {times}")
                # Sending message to the webhook multiple times
                for _ in range(times):
                    # Send the message to the webhook URL
                    data = {"content": message}  # Assuming the webhook expects a 'content' field
                    try:
                        response = requests.post(webhook_url, json=data)
                        if response.status_code == 204:
                            print(f"Successfully sent message to {webhook_url}")
                        else:
                            print(f"Failed to send message: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error sending message: {e}")
            else:
                messagebox.showerror("Invalid Input", "Please fill all fields correctly.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for times to spam.")

    # Send message button
    send_button = tk.Button(root, text="Send Message", command=send_message, fg="white", bg="black")
    send_button.pack(pady=20)

# Function to handle the window close event
def on_closing():
    root.quit()  # This will close the window

# Create the main window
root = tk.Tk()

# Set window size
root.geometry("500x400")

# Set window title
root.title("Webhook Spammer")

# Set background color to black
root.config(bg="black")

# Add an image (ghostface.jpg)
try:
    img = Image.open("ghostface.jpg")  # Replace with full path if needed
    img = img.resize((150, 150), Image.ANTIALIAS)  # Resize the image to fit
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(root, image=img_tk, bg="black")
    label_img.image = img_tk  # Keep a reference
    label_img.pack(pady=20)
except Exception as e:
    print(f"Error loading image: {e}")

# Add the username field
label_username = tk.Label(root, text="Username", fg="white", bg="black")
label_username.pack(pady=5)

entry_username = tk.Entry(root, fg="black", bg="white")
entry_username.pack(pady=5)

# Add the password field
label_password = tk.Label(root, text="Password", fg="white", bg="black")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", fg="black", bg="white")
entry_password.pack(pady=5)

# Add the login button
login_button = tk.Button(root, text="Login", command=on_login_click, fg="white", bg="black")
login_button.pack(pady=20)

# Set the close button handler
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter event loop
root.mainloop()
