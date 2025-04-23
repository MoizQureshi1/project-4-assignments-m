import qrcode

data = 'QR code  using  make() function'
img =  qrcode.make(data)

img.save('qr_code_project_7.png')