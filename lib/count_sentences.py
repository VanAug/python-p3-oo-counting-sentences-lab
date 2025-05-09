#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self._value = ""

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
       return self._value.endswith(".")

    def is_question(self):
       return self._value.endswith("?")
       
    def is_exclamation(self):
       return self._value.endswith("!")

    def count_sentences(self):
        #replace other ending punctuations with fullstops
        placeholder = self._value.replace("!", ".").replace("?", ".")

        #split by fullstop
        sentences = placeholder.split(".")

        #loop and filter
        count = [sentence for sentence in sentences if sentence.strip()]
        return len(count)
