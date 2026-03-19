# AI Commit Message Assistent
A CLI tool that leverages Google Gemini 2.5 Flash to analyze your staged Git changes and suggest meaningful, context-aware commit messages in multiple languages. This tool is designed to provide a personalized user experience, if you wish to modify the prompt for a more suitable version, please, feel free to do so in `prompts.py`. You can also update the Gemini model version in `llm.py` (check the note comment).

# Features
- **Automatic Context:** Analyzes `git diff` to understand your changes in the current repository.

- **Multi-language Support:** Generate messages in English, Portuguese, Spanish, Russian, Chinese and more using ISO codes.

- **Interactive Help:** Built-in help menu with tutorials for Git basics, API setup and language support.

- **Personalized UI:** Powered by Rich for a clean and easy-to-use terminal experience.
###
# Installation
**1. Clone the repository:**

```bash
git clone https://github.com/davijr28/aiCommitAssistent
cd aiCommitAssistent
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

**3. Configure your API Key:**

Create a **.env** file in the root folder and add your Gemini API key:

```bash
GEMINI_API_KEY="your_key_here"
```
Note: You must have a valid Gemini API key from Google AI Studio. Detailed setup instructions are available in the built-in help menu.
# Usage
**1. Stage your changes**

First, use standard Git commands to track your files:

```bash
git add .
```

**2. Generate the commit**

Run the tool to get a suggested message and commit instantly:

```bash
# Default (English)
python main.py

# Specific Language (e.g., Portuguese)
python main.py pt
```

**3. Get Help**

If you're stuck, use the interactive help menu by typing:

```bash
python main.py help
```

# Requirements
This project relies on the following libraries:

`google-genai`: Integration with Gemini.

`typer`: CLI command handling.

`rich`: Terminal formatting and interactive prompts.

`pycountry`: ISO language validation.

`python-dotenv`: Environment variable management.


### Author: Davi Jordani Ramos