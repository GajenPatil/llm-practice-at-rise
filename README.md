# LLM Chatbot

This repository contains a collection of AI-powered Python apps and experiments built with LangChain, Groq, OpenAI, and Streamlit. It includes chatbots, content generators, interview tools, and document-based assistants.

## Features

- Streamlit-based chatbot interface
- PDF document Q&A workflow
- Groq-powered LLM integrations
- AI interview assistant
- Email and LinkedIn post generators
- Story generator and travel planner experiments
- Multi-agent examples

## Project structure

- `app.py` - main chatbot application
- `chatbot.py` - document-based Q&A assistant
- `AI_interview.py` - interview simulation app
- `Email_generator.py` - email generation script
- `Linkedin_post_generator.py` - social media post generation script
- `Story_teller.py` - story generation app
- `career_mentor.py` - career guidance assistant
- `multiagent.py` and `miniagent.py` - multi-agent examples
- `ollama.py` - Ollama integration example

## Setup

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:

   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Run the app

Start the main Streamlit app:

```bash
streamlit run app.py
```

You can also run individual scripts directly depending on the app you want to test.

## Notes

- Some files may rely on external LLM providers and require valid API keys.
- If you are using a local model or alternative provider, update the relevant script imports and environment variables accordingly.
- For best results, keep your `.env` file out of version control.

## License

This project is intended for learning and personal experimentation.
