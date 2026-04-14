import qrcode

link = input("Enter your link : ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(link)
qr.make(fit=True)

#Convert to image
img = qr.make_image(fill_color = "black", back_color= "white")

qr_name = input("Enter a name to save the QR : ")

img.save(qr_name + ".png")

print(f"Your QR code generated and saved as {qr_name}.png")