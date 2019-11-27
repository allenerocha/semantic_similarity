import re
import string


class clean_text:
    def __init__(self, text: str):
        self.text = text
        self.text_list = self.__clean_text(self.text)

    def __clean_text(self, text: str):
        return self.__sentence_split(text.lower())

    def __sentence_split(self, text: str) -> list:
        punctuation_table = []
        auxiliary_list = []
        final_list = []
        table = string.punctuation
        for index in range(len(table)):
            punctuation_table.append(table[index])
        for index in range(len(punctuation_table)):
            auxiliary_list.append(text.split(punctuation_table[index]))
        for aux_index in range(len(auxiliary_list)):
            for punc_index in range(len(punctuation_table)):
                if punctuation_table[punc_index] not in auxiliary_list[aux_index]:
                       final_list.append(auxiliary_list[aux_index])
        print(final_list)
        return self.__word_split([t.translate(table) for t in text])


filename = '../testing files/Metamorphosis_-_Franz_Kafka'
text = open(filename, 'rt').read()

ct = clean_text(text)

print(ct.text_list[:100])
