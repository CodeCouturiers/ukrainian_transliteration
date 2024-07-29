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
        'І': 'I', 'і': 'i',
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
    for char in text:
        if char in translit_table:
            if char == 'Є' and result and result[-1].isalpha():
                result.append('ie')
            elif char == 'Ї' and result and result[-1].isalpha():
                result.append('i')
            elif char == 'Й' and result and result[-1].isalpha():
                result.append('i')
            elif char == 'Ю' and result and result[-1].isalpha():
                result.append('iu')
            elif char == 'Я' and result and result[-1].isalpha():
                result.append('ia')
            else:
                result.append(translit_table[char])
        else:
            result.append(char)

    # Особый случай для 'зг'
    result = ''.join(result)
    result = result.replace('zgh', 'zgh')

    return result


# Пример использования
ukrainian_text = "Згорани Борщагівка Гоща"
transliterated = transliterate(ukrainian_text)
print(transliterated)
