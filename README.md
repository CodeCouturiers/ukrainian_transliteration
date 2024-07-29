# Ukrainian-Latin Transliteration

This project implements Ukrainian to Latin transliteration according to the official Ukrainian transliteration system.

## Description

This Python script provides a function to transliterate Ukrainian text into the Latin alphabet following the rules established by the Cabinet of Ministers of Ukraine in Resolution No. 55 of January 27, 2010.

The transliteration system is designed to represent Ukrainian names and place names in a standardized Latin form for use in official documents, passports, scientific publications, cartography, and other international contexts.

## Features

- Implements the full Ukrainian-Latin transliteration table
- Handles special cases like 'зг' -> 'zgh'
- Accounts for position-specific rules (e.g. 'ї' at the beginning of words)
- Preserves capitalization
- Removes soft sign (ь) and apostrophe (') as per the official rules

## Usage

```python
from transliterate import transliterate

ukrainian_text = "Київ"
latin_text = transliterate(ukrainian_text)
print(latin_text)  # Output: Kyiv
```

## Examples

The script includes a set of example Ukrainian words and names to demonstrate the transliteration:

```python
examples = [
    "Алушта Андрій",
    "Борщагівка Борисенко",
    "Вінниця Володимир",
    # ... (more examples)
]

for example in examples:
    transliterated = transliterate(example)
    print(f"{example} -> {transliterated}")
```

## Official Reference

This implementation is based on the official transliteration table approved by the Cabinet of Ministers of Ukraine. The full table and rules can be found in the original document:

[ТАБЛИЦЯ транслітерації українського алфавіту латиницею](https://www.kmu.gov.ua/npas/243262567)

## License

MIT License

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit issues or pull requests.
