import qrcode as qr
usr = input("Paste link or message you want to transorm into QR CODE.")
title = input("title of your qr code.")


img = qr.make(usr)
img.save(title+".png")



