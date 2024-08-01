from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define your OpenAI API key and organization if available
api_key = os.getenv('OPENAI_API_KEY')
organization = os.getenv('OPENAI_ORGANIZATION')
project = os.getenv('OPENAI_PROJECT')  # Optional, if using project-scoped API keys

# Initialize the OpenAI client
client = OpenAI(api_key=api_key, organization=organization, project=project)

def get_system_prompt(file_path):
    """Reads the system prompt from a txt file."""
    try:
        with open(file_path, 'r') as file:
            system_prompt = file.read()
        return system_prompt
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None

def get_user_prompt():
    """Prompts the user in the console for their input."""
    return input("Please enter your message: ")

def create_chat_completion(system_prompt, user_prompt):
    """Creates a chat completion using OpenAI's API."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=4000
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Specify the path to your system prompt file
    system_prompt_file_path = 'system_training.txt'
    
    # Get the system prompt from the file
    system_prompt = get_system_prompt(system_prompt_file_path)
    
    if system_prompt:
        # Get the user prompt from the console
        user_prompt = get_user_prompt()
        
        # Create the chat completion
        response = create_chat_completion(system_prompt, user_prompt)
        
        if response:
            # Print the response
            print(response.choices[0].message.content)
