import qrcode
qr = qrcode.make('https://seppeg.github.io/')
qr.save("qr-code.png")