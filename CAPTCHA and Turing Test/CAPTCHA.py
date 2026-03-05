import random, string
from PIL import Image, ImageDraw, ImageFont
import math

def generate_captcha(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))



def draw_captcha_image(text, path="captcha.png"):
    w, h = 260, 90
    img = Image.new("RGB", (w, h), (245, 245, 250))
    draw = ImageDraw.Draw(img)



   
    for _ in range(80):
        x, y = random.randint(0, w), random.randint(0, h)
        draw.ellipse([x, y, x+2, y+2], fill=(random.randint(200, 230),)*3)



 
    points = []
    x = 0
    while x < w:
        y = h // 2 + int(10 * math.sin(0.05 * x))
        points.append((x, y))
        x += 3
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=(180, 180, 200), width=1)

   


    try:
        font = ImageFont.truetype("arial.ttf", 42)
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        except:
            font = ImageFont.load_default()

    



    for i, char in enumerate(text):
        char_img = Image.new("RGBA", (45, 70), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        color = (random.randint(0, 80), random.randint(0, 80), random.randint(120, 200))
        char_draw.text((4, 5), char, fill=color, font=font)
        rotated = char_img.rotate(random.randint(-10, 10), expand=True)
        img.paste(rotated, (10 + i * 40, random.randint(5, 15)), rotated)

    img.save(path)





def run_captcha():
    text = generate_captcha()
    draw_captcha_image(text)
    Image.open("captcha.png").show()
    return input("Enter CAPTCHA: ").strip().upper() == text




if __name__ == "__main__":
    print("Passed!" if run_captcha() else "Failed!")