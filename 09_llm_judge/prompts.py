import logfire
from logfire import VariablesOptions
from dotenv import load_dotenv

load_dotenv()

logfire.configure(variables=VariablesOptions)


def get_prompt(name, default="You are a jokey assistant", label="latest"):
    prompt = logfire.var(
        name=f"prompt__{name}", default=default, type=str
    )
    prompt.refresh_sync(force=True)
    return prompt.get(label=label).value


if __name__ == "__main__":
    print(get_prompt("career_agent_instructions", label="staging2"))
