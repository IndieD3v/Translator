from translate import Translator

def main():
    
    your_lang = str(input("Enter Your Language : "))
    convert_lang  = str(input("Translate " +your_lang+ " to : "))

    words = str(input("Enter word to be converted to " +convert_lang + " : "))

    translator = Translator(from_lang = your_lang,to_lang = convert_lang)
    translate = translator.translate(words)

    print(translate)

    restart = input("Press r to Restart : ")
    if (restart == "r"):
        main()
        
main()
