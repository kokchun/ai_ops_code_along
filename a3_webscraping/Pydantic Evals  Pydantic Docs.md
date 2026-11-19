[Skip to content](https://pydantic.dev/docs/ai/evals/evals/#_top)

# Pydantic Evals

**Pydantic Evals** is a powerful evaluation framework for systematically testing and evaluating AI systems, from simple LLM calls to complex multi-agent applications. It grades an agent’s final outputs and its [trajectory](https://pydantic.dev/docs/ai/evals/evaluators/agentic/) (the sequence and arguments of its tool calls), against datasets in code or, with [online evaluation](https://pydantic.dev/docs/ai/evals/online-evaluation/), against a sample of live production traffic.

## Design Philosophy

[Section titled Design Philosophy](https://pydantic.dev/docs/ai/evals/evals/#design-philosophy)

## Quick Navigation

[Section titled Quick Navigation](https://pydantic.dev/docs/ai/evals/evals/#quick-navigation)

**Getting Started:**

- [Installation](https://pydantic.dev/docs/ai/evals/evals/#installation)
- [Quick Start](https://pydantic.dev/docs/ai/evals/getting-started/quick-start/)
- [Core Concepts](https://pydantic.dev/docs/ai/evals/getting-started/core-concepts/)

**Evaluators:**

- [Evaluators Overview](https://pydantic.dev/docs/ai/evals/evaluators/overview/) \- Compare evaluator types and learn when to use each approach
- [Built-in Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/built-in/) \- Complete reference for exact match, instance checks, and other ready-to-use evaluators
- [LLM as a Judge](https://pydantic.dev/docs/ai/evals/evaluators/llm-judge/) \- Use LLMs to evaluate subjective qualities, complex criteria, and natural language outputs
- [Custom Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/custom/) \- Implement domain-specific scoring logic and custom evaluation metrics
- [Span-Based Evaluation](https://pydantic.dev/docs/ai/evals/evaluators/span-based/) \- Evaluate internal agent behavior (tool calls, execution flow) using OpenTelemetry traces. Essential for complex agents where correctness depends on _how_ the answer was reached, not just the final output. Also ensures eval assertions align with production telemetry.
- [Agentic Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/agentic/) \- Grade an agent’s _trajectory_, the sequence and arguments of its tool calls, not just the final output

**Online Evaluation:**

- [Online Evaluation](https://pydantic.dev/docs/ai/evals/online-evaluation/) \- Attach evaluators to production or staging traffic so every call, or a sampled subset, is graded in the background

**How-To Guides:**

- [Logfire Integration](https://pydantic.dev/docs/ai/evals/how-to/logfire-integration/) \- Visualize results
- [Dataset Management](https://pydantic.dev/docs/ai/evals/how-to/dataset-management/) \- Save, load, generate
- [Concurrency & Performance](https://pydantic.dev/docs/ai/evals/how-to/concurrency/) \- Control parallel execution
- [Retry Strategies](https://pydantic.dev/docs/ai/evals/how-to/retry-strategies/) \- Handle transient failures
- [Metrics & Attributes](https://pydantic.dev/docs/ai/evals/how-to/metrics-attributes/) \- Track custom data
- [Case Lifecycle Hooks](https://pydantic.dev/docs/ai/evals/how-to/lifecycle/) \- Per-case setup, teardown, and context enrichment

**Examples:**

- [Simple Validation](https://pydantic.dev/docs/ai/evals/examples/simple-validation/) \- Basic example

**Reference:**

- [API Documentation](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/)

## Code-First Evaluation

[Section titled Code-First Evaluation](https://pydantic.dev/docs/ai/evals/evals/#code-first-evaluation)

Pydantic Evals follows a **code-first approach** where you define all evaluation components (datasets, experiments, tasks, cases and evaluators) in Python code, or as serialized data loaded by Python code. This differs from platforms with fully web-based configuration.

When you run an _Experiment_, you’ll see a progress indicator and can print the results wherever you run your Python code (IDE, terminal, etc.). You also get a report object back that you can serialize and store or send to a notebook or other application for further visualization and analysis.

If you are using [Pydantic Logfire](https://logfire.pydantic.dev/docs/guides/web-ui/evals/?pydev_distinct_id=01a1eec2-79b6-7878-b0cf-29efced90779&pydev_session_id=01a1eec2-79b7-754f-b2e2-af3772191e01&pydev_first_touch_at=2026-11-18T13%3A04%3A44.977Z&pydev_referrer=www.google.com&pydev_landing=%2Fdocs%2Fai%2Fevals%2Fevals%2F), your experiment results automatically appear in the Logfire web interface for visualization, comparison, and collaborative analysis. Logfire serves as an observability layer: you write and run evals in code, then view and analyze the results in the web UI.

## Installation

[Section titled Installation](https://pydantic.dev/docs/ai/evals/evals/#installation)

To install the Pydantic Evals package, run:

- [pip](https://pydantic.dev/docs/ai/evals/evals/#tab-panel-0-0)
- [uv](https://pydantic.dev/docs/ai/evals/evals/#tab-panel-0-1)

Terminal

```bash
pip install pydantic-evals




```

Terminal

```bash
uv add pydantic-evals




```

`pydantic-evals` does not depend on `pydantic-ai`, but has an optional dependency on `logfire` if you’d like to
use OpenTelemetry traces in your evals, or send evaluation results to [logfire](https://pydantic.dev/logfire).

- [pip](https://pydantic.dev/docs/ai/evals/evals/#tab-panel-1-0)
- [uv](https://pydantic.dev/docs/ai/evals/evals/#tab-panel-1-1)

Terminal

```bash
pip install 'pydantic-evals[logfire]'




```

Terminal

```bash
uv add 'pydantic-evals[logfire]'




```

## Pydantic Evals Data Model

[Section titled Pydantic Evals Data Model](https://pydantic.dev/docs/ai/evals/evals/#pydantic-evals-data-model)

Pydantic Evals is built around a simple data model:

### Data Model Diagram

[Section titled Data Model Diagram](https://pydantic.dev/docs/ai/evals/evals/#data-model-diagram)

```plaintext
Dataset (1) ──────────── (Many) Case│                        ││                        │└─── (Many) Experiment ──┴─── (Many) Case results     │     └─── (1) Task     │     └─── (Many) Evaluator




```

### Key Relationships

[Section titled Key Relationships](https://pydantic.dev/docs/ai/evals/evals/#key-relationships)

1. **Dataset → Cases**: One Dataset contains many Cases
2. **Dataset → Experiments**: One Dataset can be used across many Experiments over time
3. **Experiment → Case results**: One Experiment generates results by executing each Case
4. **Experiment → Task**: One Experiment evaluates one defined Task
5. **Experiment → Evaluators**: One Experiment uses multiple Evaluators. Dataset-wide Evaluators are run against all Cases, and Case-specific Evaluators against their respective Cases

### Data Flow

[Section titled Data Flow](https://pydantic.dev/docs/ai/evals/evals/#data-flow)

1. **Dataset creation**: Define cases and evaluators in YAML/JSON, or directly in Python
2. **Experiment execution**: Run `dataset.evaluate_sync(task_function)`
3. **Cases run**: Each Case is executed against the Task
4. **Evaluation**: Evaluators score the Task outputs for each Case
5. **Results**: All Case results are collected into a summary report

For a deeper understanding, see [Core Concepts](https://pydantic.dev/docs/ai/evals/getting-started/core-concepts/).

## Datasets and Cases

[Section titled Datasets and Cases](https://pydantic.dev/docs/ai/evals/evals/#datasets-and-cases)

In Pydantic Evals, everything begins with [`Dataset`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset) s and [`Case`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case) s:

- **[`Dataset`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset)**: A collection of test Cases designed for the evaluation of a specific task or function
- **[`Case`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case)**: A single test scenario corresponding to Task inputs, with optional expected outputs, metadata, and case-specific evaluators

simple\_eval\_dataset.py

```python
from pydantic_evals import Case, Datasetcase1 = Case(    name='simple_case',    inputs='What is the capital of France?',    expected_output='Paris',    metadata={'difficulty': 'easy'},)dataset = Dataset(name='capital_quiz', cases=[case1])




```

_(This example is complete, it can be run “as is”)_

See [Dataset Management](https://pydantic.dev/docs/ai/evals/how-to/dataset-management/) to learn about saving, loading, and generating datasets.

## Evaluators

[Section titled Evaluators](https://pydantic.dev/docs/ai/evals/evals/#evaluators)

[`Evaluator`](https://pydantic.dev/docs/ai/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator) s analyze and score the results of your Task when tested against a Case.

These can be deterministic, code-based checks (such as testing model output format with a regex, or checking for the appearance of PII or sensitive data), or they can assess non-deterministic model outputs for qualities like accuracy, precision/recall, hallucinations, or instruction-following.

While both kinds of testing are useful in LLM systems, classical code-based tests are cheaper and easier than tests which require either human or machine review of model outputs.

Pydantic Evals includes several [built-in evaluators](https://pydantic.dev/docs/ai/evals/evaluators/built-in/) and allows you to define [custom evaluators](https://pydantic.dev/docs/ai/evals/evaluators/custom/):

simple\_eval\_evaluator.py

```python
from dataclasses import dataclassfrom pydantic_evals.evaluators import Evaluator, EvaluatorContextfrom pydantic_evals.evaluators.common import IsInstancefrom simple_eval_dataset import datasetdataset.add_evaluator(IsInstance(type_name='str'))  @dataclassclass MyEvaluator(Evaluator):    async def evaluate(self, ctx: EvaluatorContext[str, str]) -> float:          if ctx.output == ctx.expected_output:            return 1.0        elif (            ctx.expected_output is not None            and ctx.expected_output.lower() in ctx.output.lower()        ):            return 0.8        else:            return 0.0dataset.add_evaluator(MyEvaluator())




```

You can add built-in evaluators to a dataset using the [`add_evaluator`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset.add_evaluator) method.

This custom evaluator returns a simple score based on whether the output matches the expected output.

_(This example is complete, it can be run “as is”)_

Learn more:

- [Evaluators Overview](https://pydantic.dev/docs/ai/evals/evaluators/overview/) \- When to use different types
- [Built-in Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/built-in/) \- Complete reference
- [LLM Judge](https://pydantic.dev/docs/ai/evals/evaluators/llm-judge/) \- Using LLMs as evaluators
- [Custom Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/custom/) \- Write your own logic
- [Span-Based Evaluation](https://pydantic.dev/docs/ai/evals/evaluators/span-based/) \- Analyze execution traces
- [Agentic Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/agentic/) \- Grade an agent’s trajectory

## Running Experiments

[Section titled Running Experiments](https://pydantic.dev/docs/ai/evals/evals/#running-experiments)

Performing evaluations involves running a task against all cases in a dataset, also known as running an “experiment”.

Putting the above two examples together and using the more declarative `evaluators` kwarg to [`Dataset`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset):

simple\_eval\_complete.py

```python
from pydantic_evals import Case, Datasetfrom pydantic_evals.evaluators import Evaluator, EvaluatorContext, IsInstancecase1 = Case(      name='simple_case',    inputs='What is the capital of France?',    expected_output='Paris',    metadata={'difficulty': 'easy'},)class MyEvaluator(Evaluator[str, str]):    def evaluate(self, ctx: EvaluatorContext[str, str]) -> float:        if ctx.output == ctx.expected_output:            return 1.0        elif (            ctx.expected_output is not None            and ctx.expected_output.lower() in ctx.output.lower()        ):            return 0.8        else:            return 0.0dataset = Dataset(    name='capital_quiz',    cases=[case1],    evaluators=[IsInstance(type_name='str'), MyEvaluator()],  )async def guess_city(question: str) -> str:      return 'Paris'report = dataset.evaluate_sync(guess_city)  report.print(include_input=True, include_output=True, include_durations=False)  """                              Evaluation Summary: guess_city┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓┃ Case ID     ┃ Inputs                         ┃ Outputs ┃ Scores            ┃ Assertions ┃┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩│ simple_case │ What is the capital of France? │ Paris   │ MyEvaluator: 1.00 │ ✔          │├─────────────┼────────────────────────────────┼─────────┼───────────────────┼────────────┤│ Averages    │                                │         │ MyEvaluator: 1.00 │ 100.0% ✔   │└─────────────┴────────────────────────────────┴─────────┴───────────────────┴────────────┘"""




```

Create a [test case](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case) as above

Create a [`Dataset`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset) with test cases and [`evaluators`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset.evaluators)

Our function to evaluate.

Run the evaluation with [`evaluate_sync`](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset.evaluate_sync), which runs the function against all test cases in the dataset, and returns an [`EvaluationReport`](https://pydantic.dev/docs/ai/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport) object.

Print the report with [`print`](https://pydantic.dev/docs/ai/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport.print), which shows the results of the evaluation. We have omitted duration here just to keep the printed output from changing from run to run.

_(This example is complete, it can be run “as is”)_

See [Quick Start](https://pydantic.dev/docs/ai/evals/getting-started/quick-start/) for more examples and [Concurrency & Performance](https://pydantic.dev/docs/ai/evals/how-to/concurrency/) to learn about controlling parallel execution.

To evaluate an agent at batch prices, add [`BatchModelRequests`](https://pydantic.dev/docs/ai/core-concepts/batch/) to it: cases run concurrently, so their model requests share batches, and the evaluation takes as long as its batches do.

## API Reference

[Section titled API Reference](https://pydantic.dev/docs/ai/evals/evals/#api-reference)

For comprehensive coverage of all classes, methods, and configuration options, see the detailed [API Reference documentation](https://pydantic.dev/docs/ai/api/pydantic_evals/dataset/).

## Next Steps

[Section titled Next Steps](https://pydantic.dev/docs/ai/evals/evals/#next-steps)

1. **Start with simple evaluations** using [Quick Start](https://pydantic.dev/docs/ai/evals/getting-started/quick-start/)
2. **Understand the data model** with [Core Concepts](https://pydantic.dev/docs/ai/evals/getting-started/core-concepts/)
3. **Explore built-in evaluators** in [Built-in Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/built-in/)
4. **Integrate with Logfire** for visualization: [Logfire Integration](https://pydantic.dev/docs/ai/evals/how-to/logfire-integration/)
5. **Build comprehensive test suites** with [Dataset Management](https://pydantic.dev/docs/ai/evals/how-to/dataset-management/)
6. **Implement custom evaluators** for domain-specific metrics: [Custom Evaluators](https://pydantic.dev/docs/ai/evals/evaluators/custom/)

Was this page helpful?

Thanks for your feedback!