import csv

special_char = [
        "Ÿ", 
        "¤", 
        "·", 
        "", 
        "»", 
        "â", 
        "€", 
        "", 
        "â", 
        "™", 
        "ï", 
        "((", 
        "))", 
        "(", 
        ")", 
        "~", 
        "ƒ", 
        "œ", 
        "–", 
        "š", 
        "&gt;", 
        "’”'", 
        "¥", 
        "Œ",
        "Ž", 
        "©", 
        "&lt;", 
        "’•", 
        "ž",
         "•", 
         "s$;*t",
         "ð", 
         ".",
         "¸",
         "¦",
         "’›",
         "¢˜",
         "¹",
         "“ˆ",
         "„¢",
         "- -",
         "ˆ",
         "‰",
         "¡",
         ]

    
def compute (file, outFile):
    tweets =[]
    with open(file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            for char in special_char:
                if char in row[1]:
                    row[1] = row[1].replace(char, "")
                    row[1] = row[1].replace("  ", " ")
            tweets.append(row)


    with open(outFile, 'w', encoding="utf-8", newline="")as test:
        writer = csv.writer(test, delimiter=",")
        for tweet in tweets:
            writer.writerow(tweet)      

compute('','')

