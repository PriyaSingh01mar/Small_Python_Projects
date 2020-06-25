from translate import Translator
def language():
    '''Sample of the langauages in which you can convert your text
German
CHINESE
Hindi
    '''
    translator= Translator(to_lang=input("Enter the language in which you want to convert: "))
    translation = translator.translate(input("Enter the text to convert : "))
    print(translation)
print(language.__doc__)
language()
