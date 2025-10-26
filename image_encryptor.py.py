from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

def load_image():
    global img, tk_img, path
    path = filedialog.askopenfilename(title="Select Image",
                                      filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if path:
        img = Image.open(path).convert("RGB")
        show_image(img)
        status.config(text="Image Loaded")

def show_image(im):
    global tk_img
    im_copy = im.copy()
    im_copy.thumbnail((400, 400))
    tk_img = ImageTk.PhotoImage(im_copy)
    lbl.config(image=tk_img)

def encrypt_image():
    global img
    if img is None:
        status.config(text="No image loaded")
        return
    img = Image.eval(img, lambda x: x ^ 100)  # XOR with key=100
    show_image(img)
    status.config(text="Image Encrypted")

def decrypt_image():
    global img
    if img is None:
        status.config(text="No image loaded")
        return
    img = Image.eval(img, lambda x: x ^ 100)  # XOR again to decrypt
    show_image(img)
    status.config(text="Image Decrypted")

def save_image():
    if img is None:
        status.config(text="No image to save")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG", "*.png")])
    if save_path:
        img.save(save_path)
        status.config(text="Image Saved")

# --- GUI ---
root = Tk()
root.title("Basic Image Encryptor")
img = None
tk_img = None
path = ""

Label(root, text="Simple Image Encryptor", font=("Arial", 14, "bold")).pack(pady=5)

lbl = Label(root)
lbl.pack()

Button(root, text="Load Image", command=load_image).pack(pady=3)
Button(root, text="Encrypt", command=encrypt_image).pack(pady=3)
Button(root, text="Decrypt", command=decrypt_image).pack(pady=3)
Button(root, text="Save Image", command=save_image).pack(pady=3)

status = Label(root, text="No image loaded", fg="blue")
status.pack(pady=5)

root.mainloop()
