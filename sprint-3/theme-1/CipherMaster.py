class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def cipher(self, original_text, shift):
        return self._process_text(original_text, shift)

    def decipher(self, cipher_text, shift):
        return self._process_text(cipher_text, -shift)

    def _process_text(self, text, shift):
        result = []

        for char in text:
            lower_char = char.lower()
            if lower_char in self.alphabet:
                current_index = self.alphabet.index(lower_char)
                new_index = (current_index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(lower_char)

        return "".join(result)


# Тестирование
cipher_master = CipherMaster()
print(
    cipher_master.cipher(
        original_text="Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь",
        shift=2,
    )
)
print(
    cipher_master.decipher(
        cipher_text="рёпвиёэ тждюажт сткпбн стржмф у сжтдрер твйв, у фжч срт б жер граую",
        shift=2,
    )
)
