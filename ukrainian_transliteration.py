def transliterate_ukrainian(text):
    translit_dict = {
        'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
        'Г': 'H', 'г': 'h', 'Ґ': 'G', 'ґ': 'g', 'Д': 'D', 'д': 'd',
        'Е': 'E', 'е': 'e', 'Є': 'Ye', 'є': 'ie', 'Ж': 'Zh', 'ж': 'zh',
        'З': 'Z', 'з': 'z', 'И': 'Y', 'и': 'y', 'І': 'I', 'і': 'i',
        'Ї': 'Yi', 'ї': 'i', 'Й': 'Y', 'й': 'i', 'К': 'K', 'к': 'k',
        'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
        'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
        'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
        'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Ts', 'ц': 'ts',
        'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
        'Ю': 'Yu', 'ю': 'iu', 'Я': 'Ya', 'я': 'ia',
        ''': '', ''': '', 'ь': '', '`': ''
    }

    result = []
    for char in text:
        if char in translit_dict:
            if char.lower() in 'єїйюя' and (not result or result[-1] == ' '):
                result.append(translit_dict[char][0].upper() + translit_dict[char][1:])
            else:
                result.append(translit_dict[char])
        else:
            result.append(char)

    # Handle 'зг' special case
    output = ''.join(result)
    return output.replace('zgh', 'zgh')


# Main program
print("Enter Ukrainian text (type 'exit' to quit):")
while True:
    ukr_text = input()
    if ukr_text.lower() == 'exit':
        break
    translit_text = transliterate_ukrainian(ukr_text)
    print(f"Transliterated: {translit_text}")
