#Tyler Vo
#09/13/2024
#Description: This program analyzes the content of an email entered by the user to determine if it contains common spam keywords. It calculates a 'spam score' based on the number of spam keywords detected and assesses the likelihood that the email is spam. The results, including the spam score, spam likelihood, and any triggered keywords, are displayed to the user.


# List of common spam words or phrases
spam_keywords = [
    "Free", "100% free", "Congratulations", "Winner", "Click here", 
    "Limited time offer", "Act now", "Call now", "Earn money", 
    "Make money fast", "Risk-free", "Guaranteed", "Special promotion", 
    "Save big", "Extra cash", "Cheap", "Investment opportunity", 
    "Lowest price", "You have been selected", "No cost", "Eliminate debt", 
    "Get paid", "Act fast", "Instant access", "Apply now", "Order now", 
    "Cash bonus", "Satisfaction guaranteed", "Debt-free", "Free trial"
]

# Function to check email
def check_spam(email):

    spam_score = 0
    triggered_words = []
    
    # Convert email content to lower case
    content = email.lower()
    
    # Check each keyword in the spam list
    for keyword in spam_keywords:
        if keyword.lower() in content:
            spam_score += 1
            triggered_words.append(keyword)
    
    return spam_score, triggered_words

# Function to display results
def display_results(score, keywords):
    
    # Elseif statements to give approriate score
    print(f"\nSpam Score: {score}")
    if score == 0:
        print("Likelihood of Spam: Low")
    elif 1 <= score <= 5:
        print("Likelihood of Spam: Medium")
    elif 6 <= score <= 10:
        print("Likelihood of Spam: High")
    else:
        print("Likelihood of Spam: Very High")
    # Prints in spam keywords that were used
    if keywords:
        print("Triggered Spam Keywords:", ", ".join(keywords))
    else:
        print("No spam keywords detected.")

# Main function to request email and execute functions display_results and check_spam
def checker():
    print("Welcome to the Spam Detection Program!")
    email_message = input("Please enter the email message you'd like to analyze:\n")
    score, triggered_words = check_spam(email_message)
    display_results(score, triggered_words)

# Runs checker function
checker()