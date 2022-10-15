class Morph:


    def __init__(self, *args):
        self.spisok = [i for i in args]


    def add_word(self, word):
        if word not in self.spisok:
            self.spisok.append(word)

    def get_words(self):
        return tuple(self.spisok)

    def __eq__(self, other):
        return other.lower() in self.spisok

dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]
text = "Мы будем устанавливать связь завтра днем."
count = 0
for i in text.split():
    for j in dict_words:
        if i.strip(",.;:!?")==j:
            count+=1
            break
print(count)