from agents import coach_agent, ClientDeps
from pydantic_evals.evaluators import LLMJudge, Evaluator, EvaluatorContext
from dataclasses import dataclass
from pydantic_evals import Dataset, Case
from model import nvidia_model

# 2 types of evals
# - deterministic
# - llm judge

model = nvidia_model()


# determinstic
@dataclass
class WordCountLimit(Evaluator):
    limit: int

    def evaluate(self, ctx: EvaluatorContext[str, str]) -> bool:
        return len(ctx.output.split()) < self.limit
