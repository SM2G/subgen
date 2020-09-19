# import required classes
import os
from PIL import Image, ImageDraw, ImageFont

directory = os.fsencode('texts/')
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
(x, y) = (50, 50)
message = "Happy Birthday!"
color = 'rgb(0, 0, 0)' # black color
stroke_color = (0, 0, 255)

# draw the message on the background

for filename in os.listdir(directory):
    print(filename.decode("utf-8"))
    image = Image.open('background.png')
    draw = ImageDraw.Draw(image)
    #print(os.path.join(directory, filename))
    file_object =  open('texts/'+filename.decode("utf-8") , 'r')
    content = file_object.read()
    print(content)

    draw.text((x, y), content, fill=color, font=font, stroke_width=1, stroke_fill=stroke_color)

    image.save('images/'+filename.decode("utf-8")+'.png')
    del image
    file_object.close()
