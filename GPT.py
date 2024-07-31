import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_system_prompt(file_path):
    """Reads the system prompt from a txt file."""
    with open(file_path, 'r') as file:
        system_prompt = file.read()
    return system_prompt

def get_user_prompt():
    """Prompts the user in the console for their input."""
    user_prompt = input("Please enter your message: ")
    return user_prompt

def create_chat_completion(system_prompt, user_prompt):
    """Creates a chat completion using OpenAI's API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response

if __name__ == "__main__":
    # Specify the path to your system prompt file
    system_prompt_file_path = 'system_training.txt'
    
    # Get the system prompt from the file
    system_prompt = get_system_prompt(system_prompt_file_path)
    
    # Get the user prompt from the console
    user_prompt = get_user_prompt()
    
    # Create the chat completion
    response = create_chat_completion(system_prompt, user_prompt)
    
    # Print the response
    print(response.choices[0].message['content'])