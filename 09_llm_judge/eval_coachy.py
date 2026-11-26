from agents import coach_agent, ClientDeps
from pydantic_evals.evaluators import LLMJudge, Evaluator, EvaluatorContext, Contains
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


@dataclass
class CoachInput:
    prompt: str
    client: ClientDeps


dataset = Dataset(
    name="coach_agent_eval",
    cases=[
        Case(
            name="swedish_train_track",
            inputs=CoachInput(
                prompt="Jag älskar tåg och skulle vilja lära mig att laga tågspår i Sverige.",
                client=ClientDeps(
                    name="Annika", goal="Att få ett jobb i det här området"
                ),
            ),
            evaluators=(Contains("tåg", case_sensitive=False),),
        ),
        Case(),
        Case(),
    ],
    evaluators=[WordCountLimit(limit=150)],
)
