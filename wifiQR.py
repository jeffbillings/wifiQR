import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_wifi_qr(ssid, password, encryption='WPA'):
    wifi_string = f"WIFI:S:{ssid};T:{encryption};P:{password};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(wifi_string)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("wifi_qr.png")
    messagebox.showinfo("Success", "QR Code generated and saved as wifi_qr.png")

def on_generate():
    ssid = ssid_entry.get()
    password = password_entry.get()
    encryption = encryption_var.get()

    if not ssid or not password:
        messagebox.showwarning("Input Error", "SSID and Password cannot be empty")
        return

    generate_wifi_qr(ssid, password, encryption)

app = tk.Tk()
app.title("WiFi QR Code Generator")

tk.Label(app, text="SSID:").grid(row=0, column=0, padx=10, pady=10)
ssid_entry = tk.Entry(app)
ssid_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(app, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Encryption:").grid(row=2, column=0, padx=10, pady=10)
encryption_var = tk.StringVar(value="WPA")
encryption_menu = tk.OptionMenu(app, encryption_var, "WPA", "WEP", "None")
encryption_menu.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(app, text="Generate QR Code", command=on_generate)
generate_button.grid(row=3, columnspan=2, pady=20)

app.mainloop()
