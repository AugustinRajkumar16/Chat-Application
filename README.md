# Chat Bot Application using LangChain, Streamlit, and Ollama2

## Overview

This repository contains a chatbot built using LangChain, Streamlit, and the Ollama model. The chatbot interacts with users by providing helpful responses based on their queries.

**Note:** The application requires a system with at least 8 GB of RAM to run smoothly, as the Ollama2 model file is approximately 3.8 GB. The response time for each query may vary based on your system's performance.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.9+
- pip (Python package installer)
- [Ollama](https://ollama.com/download) (Download and install the Ollama model)

## Get the Source Code

You can get the source code in two ways:

- **Download as a ZIP file:** [Download here](https://github.com/AugustinRajkumar16/Chat-Application/archive/refs/heads/main.zip), then extract it to a folder of your choice.
- **Clone the repository using Git:** 

    ```bash
    git clone https://github.com/AugustinRajkumar16/Chat-Application.git
    ```

## Install the Required Python Packages

In your project directory, install the necessary Python libraries:

```bash
    pip install langchain 
    pip install langchain_core 
    pip install langchain-community
    pip install streamlit
```

## Running the Chat Bot

To run the chatbot locally, follow these steps:

Open a terminal or command prompt in the project directory.

Start the Streamlit app by running the following command:

```bash
    streamlit run Ollama_LLM.py
```
The chatbot will launch in your default web browser. You can start interacting by entering queries into the input field.

## Exit Commands

To exit the chatbot, you can type any of the following commands:

- close
- exit
- bye
- quit

## Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)

## Contributions:

Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests.