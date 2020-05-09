# Сохранение картинок в цикле в папку
import requests

# Номер первой и последней картинки
first = i = 1
last = 15
# Сслыка на первую картинку (без последних 2-х значений)
img="http://example.com/img_"
# Тип файла
file_type=".jpg"


while i < last:
	img_while='%s%d%s' % (img, i, file_type)
	local_name='%d%s' % (i, file_type)
	# print(img_while)
	# print(local_name)

	file=open(local_name, 'wb')
	p=requests.get(img_while)
	file.write(p.content)
	file.close()
	i = i + 1

print("done")