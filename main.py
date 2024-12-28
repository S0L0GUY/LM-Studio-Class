import lm_studio

def main():
    # Define the conversation history
    history = [
        {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
        {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
    ]

    # Create an instance of the LMStudio class
    lm = lm_studio.LMStudio(
        "model-identifier", 
        0.7, 
        history, 
        "server-ip"
    )

    while True:
        # Generate a response from the assistant
        lm.generate_response(True)

        # Get the user's response
        print("\n\n")
        user_response = input("> ")

        # Add the user's response to the conversation history
        lm.add_user_message(user_response)

def image_to_text():
    history = [
        {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
        {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
    ]

    lm = lm_studio.LMStudio(
        "model-identifier", 
        0.7, 
        history, 
        "server-ip"
    )

    lm.generate_response_with_image("C:/Users/evagrinn067/Pictures/Screenshots/embeding example.png", True)

if __name__ == "__main__":
    # main()
    image_to_text()