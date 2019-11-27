class semantic_descriptor_vector:
    def __init__(self, word: str) -> None:
        if type(word) != str:
            raise TypeError("Input must be a string")
        self.word = word
        self.components = dict()

    def add_component(self, component: str) -> None:
        if type(component) != str:
            raise TypeError("Input must be a string")
        component = component.replace('.', '').replace('!', '').replace('?', '').replace(',', '').lower()
        if component == self.word or component == '':
            return
        if component in self.components:
            self.components[component] += 1
        else:
            self.components[component] = 1

    def __str__(self) -> str:
        outStr = self.word
        outStr += "\n{"
        for key, value in self.components.items():
            outStr += '\n\t"{}": {},'.format(key, value)
        outStr += '\n}'
        return outStr


test = 'I am a sick man. I am a spiteful man. I am an unattractive man.'
smvs = []

for w in test.split():
    if len(smvs) < 1:
        smvs.append(semantic_descriptor_vector(w))
        for wrd in test.split():
            smvs[-1].add_component(wrd)
    else:
        for index in range(len(test.split())):
            # case 1: very last item is the same
            if index == (len(test.split())-1) and test.split()[index] != w:
                smvs.append(semantic_descriptor_vector(w))
                for wrd in test.split():
                    smvs[-1].add_component(wrd)
            # case 2: very last item is not the same
            elif index == (len(test.split()) - 1) and test.split()[index] == w:
                for wrd in test.split():
                    smvs[-1].add_component(wrd)
            # case 3 any of the items is the same
            elif test.split()[index] == w:
                for wrd in test.split():
                    smvs[index].add_component(wrd)

for smv in smvs:
    print(smv.__str__())
