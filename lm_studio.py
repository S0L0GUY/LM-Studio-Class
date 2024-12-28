import base64

class LMStudio:
    def __init__(self, model_id, lm_temperature, conversation_history, server_ip):
        """
        Initializes the LM_STUDIO class with the given parameters.
        Args:
            model_id (str): The identifier for the language model.
            lm_temperature (float): The temperature setting for the language model.
            conversation_history (list): The history of the conversation.
            server_ip (str): The IP address of the server hosting the language model.
        Attributes:
            model_id (str): The identifier for the language model.
            lm_temperature (float): The temperature setting for the language model.
            history (list): The history of the conversation.
            server_ip (str): The IP address of the server hosting the language model.
            client (OpenAI): The OpenAI client initialized with the server's base URL and API key.
        """
        from openai import OpenAI
        import requests

        self.model_id = model_id
        self.lm_temperature = lm_temperature
        self.history = conversation_history
        self.server_ip = server_ip

        self.client = OpenAI(base_url=f"http://{self.server_ip}:1234/v1", api_key="lm-studio")

    def add_user_message(self, message):
        """
        Adds a user message to the history.

        Args:
            message (str): The message content to be added to the history.
        """
        self.history.append({"role": "user", "content": message})

    def add_assistant_message(self, message):
        """
        Adds a message from the assistant to the conversation history.

        Args:
            message (str): The message content to be added to the history.
        """
        self.history.append({"role": "assistant", "content": message})

    def add_system_message(self, message):
        """
        Adds a system message to the conversation history.

        Args:
            message (str): The system message to be added to the history.
        """
        self.history.append({"role": "system", "content": message})

    def retrieve_conversion(self):
        """
        Retrieves the conversation history.

        Returns:
            list: The conversation history.
        """
        return self.history

    def generate_response(self, live_print=False):
        """
        Generates a response from the assistant model based on the conversation history.
        Args:
            live_print (bool, optional): If True, prints the response in real-time as it is generated. Defaults to False.
        Returns:
            str: The generated response content from the assistant.
        """
        completion = self.client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
            messages=self.history,
            temperature=0.7,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}

        for chunk in completion:
            if chunk.choices[0].delta.content:
                if live_print:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                new_message["content"] += chunk.choices[0].delta.content

        self.add_assistant_message(new_message["content"])
        return new_message["content"]

    def generate_response_with_image(self, image_path, live_print=False):
            """
            Generates a response from the assistant model based on the conversation history and an attached image.
            
            Args:
                image_path (str): The local file path to the image.
                live_print (bool, optional): If True, prints the response in real-time as it is generated. Defaults to False.
            
            Returns:
                str: The generated response content from the assistant.
            """
            # Read the image and encode it to base64
            try:
                with open(image_path, "rb") as image_file:
                    base64_image = base64.b64encode(image_file.read()).decode("utf-8")
            except Exception as e:
                print(f"Couldn't read the image. Error: {e}")
                return ""

            # Add user message indicating an image was attached
            self.add_user_message("user attached a photo")

            # Prepare the message with the image
            image_message = [
                {"type": "text", "text": "What’s in this image?"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            ]

            # Add the image message to the history
            self.history.append({"role": "user", "content": image_message})

            # Generate the response
            completion = self.client.chat.completions.create(
                model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
                messages=self.history,
                temperature=0.7,
                stream=True,
            )

            new_message = {"role": "assistant", "content": ""}

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    if live_print:
                        print(chunk.choices[0].delta.content, end="", flush=True)
                    new_message["content"] += chunk.choices[0].delta.content

            # Add the assistant's detailed description of the image to the history
            self.add_assistant_message(new_message["content"])
            return new_message["content"]