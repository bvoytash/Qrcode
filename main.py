import qrcode
TARGET_URL = 'https://some_url.com/'

features = qrcode. QRCode(version=1,box_size=40, border=3)
features.add_data(TARGET_URL)
features.make(fit=True)
generate_image = features.make_image(fill_color="black", back_color='white')
generate_image.save('image_1.png')