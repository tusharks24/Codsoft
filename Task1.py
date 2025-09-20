def chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()  # Handle spaces and case

        # Exit condition
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! 😃")
        elif "your name" in user_input:
            print("Chatbot: I'm RuleBot, your chatbot assistant.")
        elif "weather" in user_input:
            print("Chatbot: I can't check live weather, but I hope it's sunny 🌞")
        else:
            print("Chatbot: Sorry, I don’t understand that. Can you rephrase?")

# Run the chatbot safely
if _name_ == "_main_":
    chatbot()
