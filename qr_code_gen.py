import qrcode

link = input("Enter your link : ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
) #converts the link into QRcode

qr_name = input("Enter a name to save the QR : ")

qr.save(qr_name + ".png")

print(f"Your QR code generated and saved as {qr_name}.png")