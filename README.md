# People AI Search Agent

A powerful AI-driven tool that collects and synthesizes information about people from their LinkedIn profiles and X posts. This project uses LangChain, OpenAI's GPT models, and various APIs to create comprehensive personal insights.

## Features

- 🔍 Automated LinkedIn profile discovery and data extraction
- 🐦 X (Twitter) profile discovery and tweet analysis
- 🤖 AI-powered summary generation
- 📊 Integration of multiple data sources
- 🎯 Custom output formatting

## Prerequisites

- Python 3.13+
- Pipenv for dependency management
- Required API Keys:
  - OpenAI API Key
  - Tavily API Key (for web searching)
  - Scrapin.io API Key (for LinkedIn data)
  - Twitter API Keys (for X/Twitter data)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/h0p3sf4ll/people-ai-search-agent.git
cd people-ai-search-agent
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Create a `.env` file in the root directory with your API keys:
```env
# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Scrapin.io for LinkedIn data
SCRAPIN_API_KEY=your_scrapin_api_key

# Tavily for web search
TAVILY_API_KEY=your_tavily_api_key

# Twitter/X API credentials
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_KEY_SECRET=your_twitter_api_secret
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# LangChain and LangSmith configuration
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=People-AI-Search-Agent
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# Python path configuration
PYTHONPATH=/path/to/your/project/people-ai-search-agent
```

## Usage

### Command Line Interface
Run the search tool using the CLI:

```bash
python search_cli.py
```

The tool will:
1. Search for and analyze the person's LinkedIn profile
2. Find and analyze their X (Twitter) posts
3. Generate an AI-powered summary with interesting facts

## Project Structure

- `agents/` - Contains AI agents for LinkedIn and X profile discovery
- `third_parties/` - API integrations for LinkedIn and X
- `tools/` - Utility functions and search tools
- `output_parsers/` - Custom output formatting

## Dependencies

- langchain - For AI chain-of-thought processing
- langchain-openai - OpenAI integration
- langchain-community - Community tools and utilities
- tweepy - Twitter/X API client
- python-dotenv - Environment variable management
- Additional dependencies listed in Pipfile

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details