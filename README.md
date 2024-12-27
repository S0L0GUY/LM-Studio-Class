# Project Title: LM Studio

## Description
This is a class that is made to make usage of LM Studio easy for the average developer who does not want to spend extra time getting their language model set up on their next big project.

## Features
- **Interactive Chat**: Engage in real-time conversations with the language model.
- **Conversation History**: Maintains a history of messages exchanged between the user and the assistant.
- **Customizable Parameters**: Allows configuration of model ID and temperature settings for response generation.
- **Real-Time Response Generation**: Option to print responses as they are generated.

## Installation
To set up LM Studio, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd lm-studio
   ```

2. Install required dependencies:
   ```bash
   pip install openai
   ```

3. Ensure that you have access to an OpenAI-compatible server.

## Usage
To run the application, execute the `main.py` script:

```bash
python main.py
```

### Configuration
Before running, modify the following parameters in `main.py`:

- `model_id`: Set this to your desired language model identifier.
- `lm_temperature`: Adjust the temperature for response variability (0.0 - 1.0).
- `server_ip`: Specify the IP address of your LM Studio server.

### Example Conversation
The following is an example of how the conversation is initialized:

```python
history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]
```

## Class Overview

### LMStudio Class

#### Initialization
```python
def __init__(self, model_id, lm_temperature, conversation_history, server_ip):
```
- **Parameters**:
  - `model_id` (str): Identifier for the language model.
  - `lm_temperature` (float): Temperature setting for variability in responses.
  - `conversation_history` (list): History of messages exchanged.
  - `server_ip` (str): IP address of the server hosting the language model.

#### Methods
- **add_user_message(message)**: Adds a user message to the conversation history.
- **add_assistant_message(message)**: Adds an assistant message to the conversation history.
- **add_system_message(message)**: Adds a system message to the conversation history.
- **retrieve_conversation()**: Retrieves the current conversation history.
- **generate_response(live_print=False)**: Generates a response from the assistant based on conversation history.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.