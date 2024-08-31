import random

# Create the responses for Magic 8 Ball
eight_ball_responses = [
    "Yes, of course.",
    "Without a doubt, yes.",
    "You can count on it.",
    "For sure!",
    "Ask me later!",
    "I'm not sure.",
    "I can't tell you right now.",
    "I'll tell you after my nap.",
    "No way!",
    "I don't think so.",
    "Without a doubt, no.",
    "The answer is clearly NO!"
]

# Function to create the file 8ball_responses.txt
def magic_8_ball_start():
    with open("8ball_responses.txt", "w") as txtfile:
        for response in eight_ball_responses:
            txtfile.write( response + "\n")

# Function to read from the file and generate a random number for a response
def magic_8_ball():
    with open("8ball_responses.txt", "r") as txtfile:
        responses = txtfile.readlines()

        # Generates a random number 0 - 11
        rng = random.randint(0,11) 

        # Selects the correspoding line to it's number
        return responses[rng].strip()
    

# Function will run both previous functions and start the game
def main():
    magic_8_ball_start()
    continue_game = True

    # Requests user question
    while continue_game:
        userInput = input("Ask a yes or no question: ")

        # 8 Ball responds to the question.
        response = magic_8_ball()
        print(f"Magic 8 Ball says: {response}")

        # Asks if the player wants to continue playing and if "yes" the game continues
        user_continue = input("Do you want to ask another question? (yes/no): ").strip().lower()
        if user_continue !="yes":
            continue_game = False
            print("Thanks for Playing!")

# Runs the program
main()
