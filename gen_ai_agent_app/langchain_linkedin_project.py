from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_party.linkedin import scarpe_linekdin_profile

if __name__ == "__main__":
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # Temperature parameter is a measure of how creative the model.

    chain = summary_prompt_template | llm

    linkedin_data = scarpe_linekdin_profile("", True)

    result = chain.invoke(input={"information": linkedin_data})

    print(result)
