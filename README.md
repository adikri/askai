# askai 🤖

A lightweight CLI tool to query GPT from your terminal.

## Usage
askai "explain this error: list index out of range"
askai "write a git commit message for adding login feature"
askai "summarize this: $(cat notes.txt)"

## Setup
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install openai python-dotenv`
5. Add your OpenAI API key to `.env`: `OPENAI_API_KEY=your-key`
6. Run: `python3 askai.py "your question"`

## Tech
- Python 3
- OpenAI API (gpt-4o-mini)
- python-dotenv