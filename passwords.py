def word_in_file(word,filename,case_sensitive=False):
    global response
    with open(filename+".txt", "r",encoding="utf-8") as file:
        for line in file:
            if case_sensitive == True:
                if line.strip().lower() == word.strip().lower():
                    response ="Password is a commonly used password and is not secure"
                    return True
            else:
                if line.strip() == word.strip():
                    response ="Password is a dictionary word and is not secure."
                    return True

def word_has_character(word,character_list):
    global response
    word_list = list(set(word.replace(' ', '')))
    for letters in word_list:
        for digite in character_list:
            if letters == digite:
                response =""
                return True   
    response =""                         
    return False

def word_complexity(word):
    complexity = 0
    if (word_has_character(word, LOWER) == True):
        complexity += 1
    if (word_has_character(word, UPPER) == True):
        complexity += 1
    if (word_has_character(word, DIGITS) == True):
        complexity += 1
    if (word_has_character(word, SPECIAL) == True):
        complexity += 1
    return complexity

def password_strength(password,min_length=10,strong_length=16):
    global response
    if len(password) < 10:
        response = "Password is too short and is not secure."
        return 1
        
    if len(password) < 10:
        response = "Password is too short and is not secure."
        return 1
        
    if len(password) > 15:
        response = "Password is long, length trumps complexity this is a good password"
        return 5
    

    strength = 1
    strength += word_complexity(password)
    return strength

def main():
    global response
    while (True):
        print("--------------------------------------")
        print("If you whant to cancel, enter 'Q or q'.")
        password = input("Enter your password:")

        if password.lower() == "q":
            break
        
        if word_in_file(password, "toppasswords", True) == True or word_in_file(password, "wordlist") == True:
            print(response)
            print("Security: 0")
            continue
        
        finalScurity = password_strength(password)
        print(response)
        print(f"Security: {finalScurity}")
        


response = ""
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

if __name__ == "__main__":
    main()

