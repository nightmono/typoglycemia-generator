import string
import random

def transpose(text: str) -> str:
    current = 0
    output = ""
    
    while current < len(text):
        if text[current] in string.ascii_letters:
            output += text[current]
            word = []
            head = current + 1
            
            while head < len(text) and text[head] in string.ascii_letters:
                word.append(text[head])
                head += 1
            
            if len(word) == 1:
                output += word.pop()
            elif len(word) > 1:
                last_letter = word.pop()
                random.shuffle(word)
                output += "".join(word)
                output += last_letter
                
            current = head
        
        else:
            output += text[current]
            current += 1
            
    return output
        
def main():
    while 1:
        print(transpose(input("> ")))

if __name__ == "__main__":
    main()