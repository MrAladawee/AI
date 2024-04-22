import random
from datetime import datetime, timedelta


class MarkovChain:
    def __init__(self):
        self.adjacency_dict = {}

    def add_words(self, text):
        words = text.split()
        for current_word, next_word in zip(words[:-1], words[1:]):
            if current_word in self.adjacency_dict:
                self.adjacency_dict[current_word].append(next_word)
            else:
                self.adjacency_dict[current_word] = [next_word]
        # Замыкание для последнего слова
        last_word = words[-1]
        self.adjacency_dict[last_word] = self.adjacency_dict.get(last_word, []) + [words[0]]

    def generate_text(self, length, company_name):
        seed_word = "{company}"  # Используем "{company}" как начальное слово
        if seed_word not in self.adjacency_dict:
            seed_word = random.choice(list(self.adjacency_dict.keys()))  # выбор случайного слова, если "{company}" отсутствует
        current_word = seed_word
        text = [current_word.replace("{company}", company_name)]  # Заменяем "{company}" на переданное название компании
        for _ in range(length - 1):
            current_words = self.adjacency_dict[current_word]
            current_word = random.choice(current_words)
            text.append(current_word)
        today = datetime.today()
        random_date = today - timedelta(days=random.randint(1, 90))
        return ' '.join(text).replace("{company}", company_name).replace("{date}", random_date.strftime("%d.%m.%Y"))  # Заменяем все вхождения "{company}" на переданное название компании


# Использование:
text = ("Спутниковый интернет от {company} становится более доступным для жителей удаленных районов, начиная с {date}."
        "В рамках новой инициативы, {company} обещает обеспечить 100% надежность связи по всей стране к {date}."
        "{company} анонсировала создание 500 новых рабочих мест в регионах к {date}, в связи с расширением "
        "производства."
        "Акции {company} выросли на 5% после объявления о новых инвестициях в сфере ИИ и машинного обучения."
        "{company} приступил к строительству комплекса «Умный дом» в Якутске. Свердловский телекоммуникационный холдинг {company} завершил возведение комплекса по «Умному» дому в Якутске. Комплекс по управлению инженерными системами включает в себя центр мониторинга инженерных систем (Continuum Detection Center) на основе программных комплексов «УльтраУстройства» и «Мобильный дом». Комплекс строится на средства, предоставленные ГК «Акселер».")
markov = MarkovChain()
markov.add_words(text)
generated_text = markov.generate_text(15, "Ростелеком")
print(generated_text)


# Результат, который можно получить:
# доступным для жителей удаленных районов, начиная с {date}.В рамках новой инициативы, {company} обещает обеспечить 100%
# после объявления о новых инвестициях в сфере ИИ и машинного обучения.{Company} приступил к строительству комплекса
# Ростелеком обещает обеспечить 100% надежность связи по «Умному» дому в регионах к 14.03.2024, в Якутске.
