def transliterate(text):
    translit_table = {
        'А': 'A', 'а': 'a',
        'Б': 'B', 'б': 'b',
        'В': 'V', 'в': 'v',
        'Г': 'H', 'г': 'h',
        'Ґ': 'G', 'ґ': 'g',
        'Д': 'D', 'д': 'd',
        'Е': 'E', 'е': 'e',
        'Є': 'Ye', 'є': 'ie',
        'Ж': 'Zh', 'ж': 'zh',
        'З': 'Z', 'з': 'z',
        'И': 'Y', 'и': 'y',
        'І': 'І', 'і': 'і',
        'Ї': 'Yi', 'ї': 'i',
        'Й': 'Y', 'й': 'i',
        'К': 'K', 'к': 'k',
        'Л': 'L', 'л': 'l',
        'М': 'M', 'м': 'm',
        'Н': 'N', 'н': 'n',
        'О': 'O', 'о': 'o',
        'П': 'P', 'п': 'p',
        'Р': 'R', 'р': 'r',
        'С': 'S', 'с': 's',
        'Т': 'T', 'т': 't',
        'У': 'U', 'у': 'u',
        'Ф': 'F', 'ф': 'f',
        'Х': 'Kh', 'х': 'kh',
        'Ц': 'Ts', 'ц': 'ts',
        'Ч': 'Ch', 'ч': 'ch',
        'Ш': 'Sh', 'ш': 'sh',
        'Щ': 'Shch', 'щ': 'shch',
        'Ю': 'Yu', 'ю': 'iu',
        'Я': 'Ya', 'я': 'ia',
        'ь': '', "'": ''
    }

    result = []
    i = 0
    while i < len(text):
        if text[i:i + 2].lower() == 'зг':
            result.append('Zgh' if text[i].isupper() else 'zgh')
            i += 2
        elif i == 0 and text[i] == 'Ї':
            result.append('Yi')
            i += 1
        elif i == 0 and text[i] == 'ї':
            result.append('yi')
            i += 1
        elif text[i] in translit_table:
            if text[i] in 'ЄЇЙЮЯ' and i > 0 and text[i - 1].isalpha():
                result.append(translit_table[text[i]].lower())
            else:
                result.append(translit_table[text[i]])
            i += 1
        else:
            result.append(text[i])
            i += 1

    return ''.join(result)


# Примеры использования
examples = [
    "Алушта Андрій",
    "Борщагівка Борисенко",
    "Вінниця Володимир",
    "Гадяч Богдан Згурський",
    "Ґалаґан Ґорґани",
    "Донецьк Дмитро",
    "Рівне Олег Есмань",
    "Єнакієве Гаєвич Короп'є",
    "Житомир Жанна Жежелів",
    "Закарпаття Казимирчук",
    "Медвин Михайленко",
    "Іванків Іващенко",
    "Їжакевич Кадиївка Мар'їне",
    "Йосипівка Стрий Олексій",
    "Київ Коваленко",
    "Лебедин Леонід",
    "Миколаїв Маринич",
    "Ніжин Наталія",
    "Одеса Онищенко",
    "Полтава Петро",
    "Решетилівка Рибчинський",
    "Суми Соломія",
    "Тернопіль Троць",
    "Ужгород Уляна",
    "Фастів Філіпчук",
    "Харків Христина",
    "Біла Церква Стеценко",
    "Чернівці Шевченко",
    "Шостка Кишеньки",
    "Щербухи Гоща Гаращенко",
    "Юрій Корюківка",
    "Яготин Ярошенко Костянтин Знам'янка Феодосія"
]

for example in examples:
    transliterated = transliterate(example)
    print(f"{example} -> {transliterated}")
