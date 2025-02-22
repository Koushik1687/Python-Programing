import qrcode
name = "Koushik Paul"
img = qrcode.make(name)
img.save("My QR.png")
print("Generated")
