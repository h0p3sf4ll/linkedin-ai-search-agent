from typing import Tuple
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from langchain_openai import ChatOpenAI

from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.x_lookup_agent import lookup as x_lookup_agent
from third_parties.x import scrape_user_tweets


def search(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    x_username = x_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=x_username)

    summary_template = """
        given the information about a person from linkedin {information},
        and their latest twitter posts {twitter_posts} I want you to create:
        1. a short summary
        2. two interestring facts about them

        Use both information from twitter and linkedin.
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    # Langchain expression language (lcl)

    # Here we feed the summary_prompt_template into the llm,
    # and then feed the output of the llm into the summary_parser
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    print("Searching...")
    search(name="Eden Marco Udemy")
