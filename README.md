# 🤖 AI Commit Message Generator

A CLI tool that uses AI to automatically generate meaningful git commit messages based on your staged changes.

## ✨ Features

- 🧠 **AI-Powered Commit Messages**: Generate semantic commit messages using Google's Gemini AI
- ⚙️ **Seamless Integration**: Works with staged or unstaged changes in git repositories
- 🔧 **Interactive Mode**: Accept or modify suggested commit messages
- 🚀 **Auto-Commit Option**: Automatically commit changes with generated messages

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git installed on your system
- Google Gemini API key

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HenriqueCosta05/ai-commit.git
   cd ai-commit
   ```

2. **Install the Package**:

   ```bash
   pip install -e .
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the root directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🛠️ Usage

1. **Stage Your Changes**:

   ```bash
   git add .
   ```

2. **Generate Commit Message**:

   ```bash
   commit-ai generate
   ```

   The tool will analyze your staged changes and output a suggested commit message.

3. **Additional Options**:

   Generate a message for all changes (staged and unstaged):
   ```bash
   commit-ai generate --no-staged-only
   ```

   Generate and automatically commit:
   ```bash
   commit-ai generate --auto-commit
   ```

## 📋 Command Options

| Option | Description |
|--------|-------------|
| `--staged-only` | Only consider staged changes (default: True) |
| `--no-staged-only` | Consider all changes (staged and unstaged) |
| `--auto-commit` | Automatically commit with the generated message |
| `--model` | Specify an alternative AI model (currently uses Gemini 2.0 Flash) |

## 📁 Project Structure

```
ai-commit/
├── src/
│   └── commit_ai/
│       ├── __init__.py
│       ├── cli.py           # Command line interface
│       ├── git_utils.py     # Git operations
│       └── ai_handler.py    # AI integration
├── setup.py                 # Package installation
└── README.md                # This file
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
