from googletrans import Translator
translator= Translator()

# for gujarati to english for text
translated= translator.translate("સુપ્રભાત")
print(" Source Language:" + translated.src)
print(" Translated string:" + translated.text)

#for eng to gujarati for text
translated=translator.translate("I am a girl", dest='gu')
print(" Source Language:" + translated.src)
print(" Translated string:" + translated.text)