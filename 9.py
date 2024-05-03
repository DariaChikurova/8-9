def zadanie1():
    import os
    # Путь к исходной папке с изображениями
    source_folder = 'D:/Чикурова хомяк 1-МД-4/xomm'
    # Путь к папке, куда будут сохранены обработанные изображения
    destination_folder = 'D:/Чикурова хомяк 1-МД-4/xomm1'
    # Создаем папку для сохранения обработанных изображений, если она еще не существует
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # Список имен файлов, которые нужно обработать
    file_names = ['хом1.jpg', 'хом2.jpg', 'хом3.jpg', 'хом4.jpg', 'хом5.jpg']
    for file_name in file_names:
        # Открываем изображение
        img = Image.open(os.path.join(source_folder, file_name))
        # Применяем фильтр "черно-белое"
        img_gray = img.convert('L')
        # Сохраняем обработанное изображение в новой папке с новым именем
        new_file_name = 'new_' + file_name
        img_gray.save(os.path.join(destination_folder, new_file_name))
    print("Обработка изображений завершена.")

def zadanie2():
    import os
    source_folder = 'D:/Чикурова хомяк 1-МД-4/xomm'
    destination_folder = 'D:/Чикурова хомяк 1-МД-4/xomm1'
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    file_names = ['хом1.jpg', 'хом2.jpg', 'хом3.jpg', 'хом4.jpg', 'хом5.jpg']
    for file_name in file_names:
        img = Image.open(os.path.join(source_folder, file_name))
        # Применяем фильтр "черно-белое"
        img_gray = img.convert('L')
        new_file_name = 'new_' + file_name
        img_gray.save(os.path.join(destination_folder, new_file_name))
    print("Обработка изображений завершена.")

def zadanie3():
    import csv
    fieldnames = ['Product', 'Quantity', 'Price']
    with open("C:/Users/chiku/PycharmProjects/pythonProject1/pythonProject1/sym.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",", fieldnames=fieldnames)
        total_cost = 0
        sym = 0
        print("Нужно купить:")
        for row in reader:
            print(f"Reading row: {row}") # Debugging: print the row being read
            if row['Quantity'] and row['Price'] and row['Quantity'].isdigit() and row['Price'].isdigit():
                print(row['Product'], "-", row['Quantity'], "шт. за", row['Price'], "руб.")
                sym += int(row['Quantity']) * int(row['Price'])
            total_cost += 1
        print(f"Итоговая сумма: {sym} руб.")
zadanie3()

from PIL import Image, ImageDraw, ImageFont
def prazd():
    image_path = '../pug.hbd.jpg'
    image = Image.open(image_path)
    image.show()
    left = 10
    top = 10
    right = 500
    bottom = 500

    cropped_image = image.crop((left, top, right, bottom))

    new_image_path = 'pug.hbd2.jpg'
    cropped_image.save(new_image_path)
    print(f"Обрезанное изображение сохранено как {new_image_path}")
def prazds():
    prazd = {
        'День святого валентина': 'val.pug.jpg',
        'День рождения': 'pug.hbd.jpg',
        'Рождество': 'chrism.pug.jpg'
    }
    s = input("Напишите выбранный праздник: ")
    if s == "День святого валентина":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "День рождения":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "Рождество":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    else:
        print("Введенное значение не найдено в списке.")
def w():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя: ")
    try:
        image = Image.open("../pug.hbd.jpg")
    except IOError:
        print("Ошибка открытия изображения.")
        return

    draw = ImageDraw.Draw(image)

    text = f"{name}, поздравляю!"
    font = ImageFont.truetype('arial.ttf', 20)
    position = ((image.width) // 2, 10)  # Позиция текста в центре вверху
    draw.text(position, text, font=font, fill=(0, 0, 0))  # Исправлено на кортеж RGB
    image.save("new_pug.hbd.png")  # Исправлено: не указываем расширение

while True:
    print('1. обрезка')
    print('2. выбор')
    print('3. знак')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        prazd()
    elif a == 2:
        prazds()
    elif a == 3:
        w()
    elif a == 4:
        break
    else:
        print('Неверное действие')