from translate import Translator

translator = Translator(to_lang="Turkish")
translation = translator.translate("Follow us ")
print(translation)