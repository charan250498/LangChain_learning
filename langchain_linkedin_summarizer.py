from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv

from third_party.linkedin import scarpe_linekdin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def lookup_linkedin(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scarpe_linekdin_profile(linkedin_profile_url=linkedin_url)

    summary_template = """
            given the information {information} about a person I want you to create:
            1. a short summary
            2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # Temperature parameter is a measure of how creative the model.

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template) # Removed as it deprecated in LangChain 0.1.17
    chain = summary_prompt_template | llm

    result = chain.invoke(input={"information": linkedin_data})

    print(result)

if __name__ == "__main__":
    load_dotenv()
    print("Summary of a person using his name fetched from LinkedIn and Summarised by LLM")
    lookup_linkedin(name="Charan Kumar S Hypothetic")
