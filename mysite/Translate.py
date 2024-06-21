from translate import Translator


translator = Translator(to_lang="Swahili")
translation = translator.translate("WELCOME TO KENYA")

print(translation)