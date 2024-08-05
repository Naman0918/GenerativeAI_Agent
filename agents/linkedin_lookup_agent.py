import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate  
from langchain_core.tools import Tool
from langchain_ollama import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn profile page."""
    search = TavilySearchResults()
    res = search.run(f"{name} LinkedIn")
    return res[0]["url"] if res else "No profile found"

def lookup(name: str) -> str:
    llm = ChatOllama(
        temperature=0,# optional
        model="llama3"
    )

    template = """Given the full name {name_of_person}, I want you to get me a link to their LinkedIn profile page.
                    Your answer should contain only a URL."""

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the LinkedIn page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

    
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = lookup(name = "Andrea Vahl")
    print(linkedin_url)
