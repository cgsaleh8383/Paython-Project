from PIL import Image
sajjat = Image.open('sajjat.png')
bg = Image.open('tower.jpg')
bg.paste(sajjat, (0, 0), sajjat)
bg.save('first_python.jpg')