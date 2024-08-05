# from dotenv import load_dotenv
# from langchain.prompts.prompt import PromptTemplate
# from transformers import pipeline

# if __name__ == "__main__":
#     load_dotenv()

#     print("Hello LangChain")
#     information = """
#         Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $254 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

#     A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

#     In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, he founded xAI, an artificial intelligence company.
#     """

#     # Load the summarization model from Hugging Face
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#     # Generate summary
#     summary = summarizer(information, max_length=200, min_length=50, do_sample=False)

#     print("Summary:")
#     print(summary[0]['summary_text'])


from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser, Summary
from typing import Tuple

def ice_break_with(name: str) -> Tuple[Summary]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username) 

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them

    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()},
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    # linkedin_data = scrape_linkedin_profile(likein_profile_url="https://gist.githubusercontent.com/Naman0918/c3617ee29183796fb07c9745c79f779d/raw/c0bc8ab79e1248669f1d4766ec050edd37b9daa5/naman-labhsetwar.json", mock=True)

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # chain = summary_prompt_template | llm| StrOutputParser()
    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke(input={"information": linkedin_data})

    # print(res)
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()

    print("Hey, Let's Explore the World!!")
    ice_break_with(name="Sundar Pichai Google")
    

# Based on the provided LinkedIn information, here's a summary and two interesting facts about the person:

# **Summary:** Naman Labhsetwar is a professional with expertise in data science, as evident from his certification in "British Airways - Data Science Job Simulation" and "Career Essentials in Generative AI by Microsoft and LinkedIn". He has a strong network of connections (670) and has been involved in various activities.

# **Interesting Facts:**

# 1. **Certified Data Scientist**: Naman holds certifications in data science from reputable organizations like British Airways and Microsoft, indicating his expertise in this field.
# 2. **Connected to Training and Placement Cell, PICT Pune**: Among his connections are several notable organizations, including the Training and Placement Cell at PICT Pune, suggesting that he may have had interactions or collaborations with them.
