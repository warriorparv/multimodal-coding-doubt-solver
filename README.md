# Multimodal Coding Doubt Solver 🤖

This project is a Streamlit-based multimodal chatbot that solves coding problems using both text and image inputs. It leverages OpenRouter API and a vision-capable large language model to analyze problems and generate optimized solutions.

## Features
- Accepts text-based coding questions
- Supports image-based problem input
- Provides step-by-step explanations
- Generates optimized code solutions
- Interactive web-based interface

## Tech Stack
- Python
- Streamlit
- OpenRouter API
- GPT-4o-mini (Vision Model)

## How the System Works
1. User enters a question or uploads an image
2. The input is processed in the Streamlit interface
3. The request is sent to OpenRouter API
4. The vision-language model analyzes the problem
5. The chatbot returns an explanation and solution

## Setup Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt

2.Set API Key
export OPENROUTER_API_KEY="your_api_key"

3.Run the app
streamlit run app.py


