stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


# здесь продолжайте программу
class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def get(self):
        return " ".join(self.lst_words)


lst_text = [StringText([x.strip("–?!,.;") for x in y.split() if x.strip("–?!,.;")!=""]) for y in stich]
lst_text_sorted = [i.get() for i in sorted(lst_text, key=lambda x: len(x), reverse=True)]
print(lst_text_sorted)