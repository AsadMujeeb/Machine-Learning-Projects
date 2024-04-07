# Define a dictionary with predefined responses
responses = {
    "hi": "Hello there! How can I assist you today?",
    "how are you": "I'm a bot, so I don't have feelings, but I'm functioning properly!",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure, I can help you. What do you need assistance with?"
}

# Function to get the bot response
def get_bot_response(user_input):
    # Make the input lowercase to match the dictionary keys
    user_input = user_input.lower()

    # Return the matching response if it exists, otherwise return a default response
    return responses.get(user_input, "I'm not sure how to respond to that. Can you try asking something else?")

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")



-----------------------------------------------------------------------------------------

# Simple Customer Support Chatbot

responses = {
    "hi": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "do you have smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "shipping time": "Shipping usually takes 3-5 business days.",
    "shipping methods": "We offer standard, expedited, and overnight shipping.",
    "return policy": "You can return products within 30 days of receipt for a full refund.",
    "how to return": "To return a product, please visit our returns page for a step-by-step guide.",
    "won’t turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "bye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!"
}

def get_bot_response(user_input):
    user_input = user_input.lower()

    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    return "I'm not sure how to respond to that. Can you try asking something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")
