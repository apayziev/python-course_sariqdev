from uzwords import words
import random

def getWord():
    random_word = random.choice(words)
    while " " in random_word or "-"  in random_word:
        random_word = random.choice(words)
    return random_word

def displayLetters(user_letters, random_word):
    store_letters = ''
    for letter in random_word:
        if letter in user_letters:
            store_letters += letter
        else:
            store_letters += '-'
    return store_letters

def playGame():
    random_word = getWord()
    setOfWords = set(random_word)
    user_letters = ''
    print(f"Мен {len(random_word)} хонали сўз ўйладим. Топа оласизми?")
    print(random_word)
    
    while setOfWords:
        print(displayLetters(user_letters, random_word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
            
        letter = input("Ҳарф киритинг: ")
     
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in random_word:
            setOfWords.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter   
    print(f"Табриклайман! {random_word} сўзини {len(user_letters)} та уринишда топдингиз.")
        