#!/usr/bin/env python3

import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # cheapest model, perfect for CLI
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Give concise, practical answers."},
            {"role": "user", "content": question}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def main():
    if len(sys.argv) < 2:
        print("Usage: askai \"your question here\"")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    answer = ask(question)
    print(f"\n{answer}\n")

if __name__ == "__main__":
    main()
