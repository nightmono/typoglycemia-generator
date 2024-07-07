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
    
def interactive():
    print("CTRL-C to exit.")
    while 1:
        try:
            print(transpose(input("> ")))
        except KeyboardInterrupt:
            print("\nInteractive mode exitted.")
            break
        
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Script that jumbles text except for the first and last letter to prove Typoglycemia.")
    parser.add_argument("text", nargs="*", help="text that will be shuffled")
    parser.add_argument('-i', '--interactive', help="enter interactive mode", action='store_true') 
    
    args = parser.parse_args()

    if args.interactive:
        interactive()
    
    else:
        text = " ".join(args.text)    
        if not text:
            parser.print_help()
        else:
            print(transpose(text))

if __name__ == "__main__":
    main()