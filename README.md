# 0.28-openAI-python-template

This repository contains a simple chatbot application that uses the OpenAI GPT-4 model to generate responses based on user input. The project leverages the `openai` Python package and uses a `.env` file to securely manage API keys.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/0.28-openAI-python-template.git
    cd 0.28-openAI-python-template
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Create a `.env` file** in the root directory of the project and add your OpenAI API key:
    ```dotenv
    OPENAI_API_KEY=your_openai_api_key_here
    ```

2. **Add your system prompt** to a `system_training.txt` file in the root directory of the project.

3. **Run the chatbot**:
    ```bash
    python chatbot.py
    ```

4. **Enter your message** when prompted in the console.

## Project Structure
0.28-openAI-python-template/
├── chatbot.py
├── requirements.txt
├── .env
└── system_training.txt

- `chatbot.py`: Main script to run the chatbot.
- `requirements.txt`: Contains the list of dependencies.
- `.env`: Contains environment variables like the OpenAI API key.
- `system_training.txt`: Contains the system prompt.

## Configuration

- **API Key**: Store your OpenAI API key in the `.env` file as shown above.
- **System Prompt**: Customize your system prompt in the `system_training.txt` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss changes.

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -am 'Add new feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Create a new Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
