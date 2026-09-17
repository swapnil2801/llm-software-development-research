# Methodology

## Design

This project uses a structured narrative literature review informed by systematic-review practice. The review maps LLM use across seven SDLC phases: requirements, design, implementation, testing, deployment/operations, maintenance, and security.

## Search strategy

Searches were conducted using combinations of:

- `large language model` OR `LLM` OR `generative AI`
- `software engineering` OR `software development lifecycle` OR `developer productivity`
- `code generation`, `program repair`, `testing`, `requirements`, `security`, `maintenance`

Priority sources were peer-reviewed journal/conference papers, official technical reports, and openly available preprints with clear methods. Search results were screened by title, abstract, relevance, methodological clarity, and direct connection to software development.

## Inclusion criteria

- Studies published from 2017 onward, with emphasis on 2023–2025 evidence.
- Work that evaluates or synthesizes LLM use in software engineering.
- Studies reporting a method, benchmark, experiment, survey, or systematic review.
- Sources with enough information to identify the population, task, metric, or limitation discussed.

## Exclusion criteria

- Marketing claims without a described method or attributable evidence.
- General LLM studies unrelated to software development.
- Duplicate versions where a more complete publication was available.
- Unsupported claims copied from secondary summaries.

## Data extraction

For each source, record publication details, SDLC phase, task, model/tool, study design, participants or dataset, metric, result, limitation, and relevance to the research questions. The extraction template is in `data/evidence-matrix.csv`.

## Synthesis approach

Evidence is grouped thematically rather than combined through a meta-analysis because the included studies use different tasks, participants, tools, metrics, and comparison conditions. Quantitative results are quoted with their study context and are not treated as a universal effect size.

## Limitations

The review is bounded by accessible sources and search coverage. LLM tools change quickly, many studies are preprints, and productivity measurements can differ from perceived productivity. The review therefore supports cautious conclusions, not a claim that every developer or project will receive the same benefit.
