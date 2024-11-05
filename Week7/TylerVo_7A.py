# Tyler Vo
# 10/27/2024

# import regular expression
import re

def starter(sentence):
    # Pattern to determine sentences
    pat = r'([A-Z0-9][^.!?]*[.!?]?)'
    final_sentences = re.findall(pat, sentence, flags=re.MULTILINE | re.DOTALL)
    return final_sentences

def main():
    print("Enter text:")
    userinput = ""

    # Loop to collect user input until 'y' is entered
    while True:
        end = input()
        if end.strip() == 'y':
            break
        print("Are you finished? (type y, otherwise continue)")
        userinput += end + "\n"

    # Call starter function and display the sentences
    final_sentences = starter(userinput)

    print("\nSentences:")
    for i, sentence in enumerate(final_sentences, 1):
        print(f"{i}. {sentence}")

    # Display total count of sentences
    print(f"\nTotal sentences: {len(final_sentences)}")

main()

