import base64
from PIL import Image
from io import BytesIO

b = open('yuiPic.png', 'rb').read()

height = 150
# img = Image.frombytes(b)
img = Image.open(BytesIO(b))
bx, by = img.size[0], img.size[1]
x = int(round(float(height / float(by) * float(bx))))
y = height
img.thumbnail((x, y), Image.ANTIALIAS)
after_b = BytesIO()
# img.save('resize.png')
img.save(after_b, 'PNG')
# after_b = open('resize.png', 'rb').read()
# after_b = img.info['icc_profile']
# print(img.info['icc_profile'])
with open('resize.b64', 'wb') as f:
    f.write(base64.b64encode(after_b.getvalue()))
