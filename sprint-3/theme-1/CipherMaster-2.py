class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def process_text(self, text, shift, is_encrypt):
        result = []

        if not is_encrypt:
            shift = -shift

        for char in text:
            lower_char = char.lower()

            if lower_char in self.alphabet:
                current_index = self.alphabet.index(lower_char)
                new_index = (current_index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(lower_char)

        return "".join(result)


cipher_master = CipherMaster()
print(
    cipher_master.process_text(
        text="Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь",
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text="Олебэи яфвнэ мроплж сэжи – э пэй рдв злийвкпш лп нвящывнэ",
        shift=-3,
        is_encrypt=False,
    )
)
