# Generative AI Agent

## Overview

This project is a generative AI agent developed using LangChain and various open-source APIs, including Llama3 and Ollama. The agent leverages these technologies to provide advanced natural language processing and generation capabilities.

## Features

- **LangChain Integration**: Utilizes LangChain for seamless interaction with large language models and external APIs.
- **Open-Source APIs**: Incorporates Llama3 and Ollama for generative AI tasks.
- **Customizable**: Easily configurable to fit different use cases and requirements.

## Getting Started

To get started with this project, follow these instructions:

### Prerequisites

- Python 3.11 or higher
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/your-repository.git](https://github.com/Naman0918/GenerativeAI_Agent.git)
    cd your-repository
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the project root and add the following environment variables:
    ```dotenv
    API_KEY=your_api_key_here
    OPENAI_API_KEY  = your_api_key_here
    PROXYCURL_API_KEY = your_api_key_here
    TAVILY_API_KEY = your_api_key_here
    ```

2. Update the `config.py` file with your specific configuration settings.

### Usage

To run the generative AI agent, use the following command:
```bash
python3 main.py
