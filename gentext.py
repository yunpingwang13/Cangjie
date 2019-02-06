from PIL import Image, ImageDraw, ImageFont

def main():
    lines = [line.rstrip('\n') for line in open('input_unicode.txt')]
    count = 0    
    for l in lines:
        img = Image.new("RGB", (32, 32), color = (255, 255, 255))
        fnt = ImageFont.truetype("C:\\WINDOWS\\FONTS\\MSYH.TTC", 25)
        d = ImageDraw.Draw(img)
        d.fontmode = "1"
        d.text((0, 0), l, font = fnt, fill = (0, 0, 0))
        img = img.convert("L")
        img = img.convert("RGB")
        img.save("img\\" + str(count) + ".png")
        count += 1

if __name__ == '__main__':
    main()