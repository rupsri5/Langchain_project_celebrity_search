
# Langchain and Streamlit

Experimenting with the LangChain library to build robust applications that leverage large language models (LLMs) is the primary objective of this repository. This project uses modern language models like OpenAI's GPT-3.5 Turbo to provide the information on the celebrity provided as input, including a brief introduction, birthdate, and significant events that occurred at that time.

For the purpose of developing language model-powered applications, LangChain is a comprehensive framework. The most advanced and unique applications are not just calls to LLMs via APIs; they are also data-aware and agentic, enabling language models to interact with their environment and other data sources. The LangChain framework specifically addresses these ideas.

## Use Cases
#### Langchain
Developers can use LangChain to create a wide range of applications, including chatbots for customer service, content generators that operate automatically, tools for analyzing data, and intelligent search engines. These apps can assist companies in decreasing manual labor, streamlining operations, and enhancing client interactions. For more usercases read ```langchain documentation``` https://python.langchain.com/docs/get_started/introduction

#### Streamlit
Streamlit is an open-source Python library that enables you to create interactive web applications for machine learning, data visualization, and other data-centric tasks with minimal effort. It allows you to turn data scripts into shareable web apps in minutes. More about ```Streamlit``` https://docs.streamlit.io/

## Getting Started

To run this LangChain and Streamlit app locally, follow these steps:

#### 1. Clone the Repository:
```powershell
git clone git@github.com:rupsri5/Langchain_project_celebrity_search.git
```

#### 2. Create a Python environment:
Navigate to the Directory and Create Python environment
```powershell
cd Langchain_project_celebrity_search
python -m venv myenv
```

Activate environment in bash
```bash
source myenv/bin/Activate
```
or in powershell
```powershell
.\myenv\scripts\Activate
```

#### 3. Install Dependencies:
```powershell
pip install -r requirements.txt
```

#### 4. Set up the keys in a .env file
Firstly, create your OpenAI API key; you can do the same from here https://openai.com/ visit the website login/signup through your account, then select API option. After that you'll be redirected to the page where you can find ```API keys``` option on left navigation bar.

Now, create a ```.env``` file in the root directory. Inside the file, add you OpenAI API key:
```powershell
OPENAI_API_KEY="your_api_key_here"
```  

Save the file and close it. In your Python script or Jupyter notebook, load the .env file using the following code:
```powershell
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

When needed, you can access the OPENAI_API_KEY as an environment variable:
```powershell
import os
openai_api_key = os.environ['OPENAI_API_KEY']
```


#### 5. Run the App:
```powershell
streamlit run celebritySearch.py
```

#### 6. Open the App in Your Browser:
Once the app is running, you can access it by opening your web browser and navigating to http://localhost:8501.

## Deployment
This app is deployed using Streamlit Sharing. You can access the deployed version of the app https://celebrity-search-results-langchain0508.streamlit.app/.

## Features
• Celebrity Search: Enter the name of a celebrity to search for their introduction and date of birth.

• Major Events: Upon searching for a celebrity, the app displays five major events that happened around the celebrity's date of birth.

