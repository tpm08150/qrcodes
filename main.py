import qrcode
from PIL import Image

hmx = 0
illusions = 1
av_solutions = 2

company = hmx

hmx_first_name = ['Tyler', 'Katie', 'Casey', 'Josh', 'Tyler', 'Pete', 'Brady', 'Dan']
hmx_last_name = ['Morton', 'Barnes', 'Faircloth', 'Koan', 'Nissen', 'McKiernan', 'Rose', 'Gable']
hmx_phone_number_c = ['573-694-6039', '816-223-9250', '813-786-6414', '913-522-7352', '816-536-3210', '913-645-7267',
                '785-443-9092', '913-205-7582']
hmx_phone_number_o = ['', '', '', '', '', '', '', '']
hmx_email = ['tmorton@harvestkc.com', 'kbarnes@harvestkc.com', 'cfaircloth@harvestkc.com', 'jkoan@harvestkc.com',
         'tnissen@harvestkc.com', 'pmckiernan@harvestkc.com', 'brose@harvestkc.com', 'dgable@harvestkc.com']

illusions_first_name = ['Allen']
illusions_last_name = ['Halsey']
illusions_phone_number_c = ['816-820-8165']
illusions_phone_number_o = ['']
illusions_email = ['allen@illusionskc.com']

av_first_name = ['Susan']
av_last_name = ['Surman']
av_phone_number_c = ['816-985-8505']
av_phone_number_o = ['816-612-8170']
av_email = ['ssurman@avsolutionskc.com']

hmx_green = (75,75,75)
illusions_orange = (211,113,22)
av_blue = (63, 87, 121)
black = (0,0,0)

first_names = [hmx_first_name, illusions_first_name, av_first_name]
last_names = [hmx_last_name, illusions_last_name, av_last_name]
phone_numbers_c = [hmx_phone_number_c, illusions_phone_number_c, av_phone_number_c]
phone_numbers_o = [hmx_phone_number_o, illusions_phone_number_o, av_phone_number_o]
emails = [hmx_email, illusions_email, av_email]
colors = [hmx_green, illusions_orange, av_blue]
logos = ['play_button.jpg', 'illusion_eye.jpg', 'AV_solutions.jpg']
address = ['HMXLive', 'Illusions Unlimited', 'AV Solutions']
websites = ['https://www.hmxlive.com/', 'https://www.illusionskc.com/', 'https://www.avsolutionskc.com/']


x = 0
for i in first_names[company]:
    logo = Image.open(logos[company])
    size = (164,164)
    new_logo = logo.convert('RGBA')
    new_logo.save('new_logo.png')
    #logo.thumbnail(size, Image.ANTIALIAS)

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    VCARD_TEMPLATE = f"""
    BEGIN:VCARD
VERSION:3.0
N:{last_names[company][x]};{first_names[company][x]}
FN:{first_names[company][x]} {last_names[company][x]}
ORG: {address[company]}
ADR;TYPE=WORK,POSTAL,PARCEL:;;{address[company]};1111 Virginia Ave;Kansas City;MO;64106;USA
TEL;TYPE=CELL,MSG:{phone_numbers_c[company][x]}
TEL;TYPE=Office,MSG:{phone_numbers_o[company][x]}
EMAIL;TYPE=Email:{emails[company][x]}
URL;TYPE=Website:{websites[company]}
END:VCARD
    """

    #img = qrcode.make(VCARD_TEMPLATE)
    #print(img)
    qr.add_data(VCARD_TEMPLATE)
    qr.make()
    img_qr = qr.make_image().convert('RGB')
    img_qr = qr.make_image(back_color=(255,255,255), fill_color=(colors[company]))
    pos = ((img_qr.size[0] - logo.size[0]) // 2, (img_qr.size[1] - logo.size[1]) // 2)

    img_qr.paste(logo, pos)

    img_qr.save(f'{first_names[company][x]}_{last_names[company][x]}vCard.png')
    #img.show()
    print(f'\n{first_names[company][x]}_{last_names[company][x]} QR Code Generated\n')
    x += 1


