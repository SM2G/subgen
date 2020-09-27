# import required classes
import os
from PIL import Image, ImageDraw, ImageFont

directory = os.fsencode('texts/')
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
(x, y) = (20, 20)
color = (0, 163, 255)
stroke_color = (0, 0, 0)

for filename in os.listdir(directory):
    print(filename.decode("utf-8"))
    image = Image.open('background.png')
    draw = ImageDraw.Draw(image)
    #print(os.path.join(directory, filename))
    file_object =  open('texts/'+filename.decode("utf-8") , 'r')
    content = file_object.read()
    print(content)

    # draw the content on the background
    draw.text((x, y), content, fill=color, font=font, stroke_width=1, stroke_fill=stroke_color)

    image.save('images/'+filename.decode("utf-8")+'.png')
    del image
    file_object.close()
