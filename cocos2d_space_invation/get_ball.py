from PIL import Image, ImageDraw
img = Image.new("RGB", (200, 200), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.ellipse((50, 50, 150, 150), fill=(0, 255, 0), outline=(255, 0, 0), width=5)
img.save("circle.png")