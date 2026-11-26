from agents import coach_agent, ClientDeps
from pydantic_evals.evaluators import LLMJudge
from dataclasses import dataclass
from pydantic_evals import Dataset, Case
from model import nvidia_model

# 2 types of evals
# - deterministic
# - llm judge


