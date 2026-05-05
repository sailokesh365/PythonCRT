import qrcode
qr=qrcode.QRCode()
a="TVK os rocking "
qr.add_data(a)
qr.make(fit=True)
res=qr.make_image(fill_color="black",back_color="white")
res.save("lokesh.png")
print("created rr")
