from pydantic_ai import Agent
from pydantic_ai import RunContext
from model import nvidia_model

model = nvidia_model()

study_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a study expert. Give concrete study plans and learning techniques."
    ),
)

career_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a career advisor. Give practical advice on jobs, resumes, and career paths.",
    ),
)

coach_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a personal coach. Follow these steps IN ORDER:\n"
        "1. Call `ask_study_agent` for study questions.\n"
        "2. Call `ask_career_agent` for career questions.\n"
        "3. Combine the answers into ONE short, simple response.\n"
        "4. Call `export_report` with that final response as `text`.\n"
        "5. Reply to the user with the final response."
    ),
)