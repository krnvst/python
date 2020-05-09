# Сохранение одной картинки в папку по сслыке
import requests

# В переменную img указать ссылку на картинку
# В переменную local_name указать как будет называтся файл на компютере

img="https://images.wallpaperscraft.ru/image/el_vetki_igolki_128622_1920x1080.jpg"
local_name="image.jpg"

file=open(local_name, 'wb')
p=requests.get(img)
file.write(p.content)
file.close()
print("saved")