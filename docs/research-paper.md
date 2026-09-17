# The Role of Large Language Models in Automating Software Development Processes

## Abstract

Large language models (LLMs) are increasingly embedded in software development tools that generate code, explain unfamiliar systems, write tests, summarize changes, and assist with debugging. This paper reviews how these systems affect the software development life cycle (SDLC), what evidence supports productivity and quality claims, and which risks limit dependable automation. A structured literature review was used to organize evidence across requirements engineering, design, implementation, testing, deployment, maintenance, and security. The literature indicates that LLMs are particularly valuable for bounded, repetitive, and language-heavy tasks. Controlled evidence also reports meaningful reductions in completion time for selected programming tasks. However, benefits are task- and context-dependent. LLMs can produce incorrect code, insecure suggestions, fabricated APIs or packages, privacy risks, and maintenance problems. The central conclusion is that LLMs should be treated as supervised engineering instruments rather than autonomous replacements for developers. Effective adoption combines human judgment, automated tests, security and dependency checks, documentation, and clear accountability.

**Keywords:** large language models, software engineering, code generation, developer productivity, software development life cycle, AI-assisted programming, responsible AI

## 1. Introduction

Software development contains both creative and repetitive work. Engineers interpret requirements, design systems, implement features, test behavior, maintain code, and communicate decisions. LLM-based assistants can now participate in many of these activities through natural-language prompts and contextual code completion. This creates an opportunity to automate parts of the SDLC, but it also creates a risk of accepting plausible output without sufficient verification.

The phrase “automating software development” should therefore be used precisely. An LLM does not independently guarantee a production-ready system. It generates predictions based on learned patterns and available context. Automation is useful when a task has a clear specification, observable output, and reliable validation. A human remains responsible for defining the problem, evaluating trade-offs, and approving changes.

This paper addresses five questions:

1. Which SDLC activities can LLMs support or automate?
2. What benefits have controlled studies and surveys reported?
3. What risks and limitations affect dependable adoption?
4. What human oversight and evaluation practices are required?
5. Which research gaps remain open?

## 2. Methodology

This project uses a structured literature review and thematic evidence synthesis. Searches combined terms such as “large language model,” “LLM,” “software engineering,” “code generation,” “testing,” “program repair,” “developer productivity,” and “security.” Priority was given to peer-reviewed publications, systematic reviews, official research reports, and open preprints with clear methods.

Sources were included when they evaluated or synthesized LLM use in software engineering and reported a method, benchmark, experiment, survey, or review protocol. General LLM papers unrelated to software development, unsupported marketing claims, duplicates, and sources without attributable evidence were excluded. The review does not perform a statistical meta-analysis because the studies differ substantially in tasks, populations, tools, and metrics. The extraction matrix records each source’s task, evidence, result, and limitation.

## 3. LLMs Across the SDLC

### 3.1 Requirements engineering

LLMs can transform stakeholder statements into user stories, acceptance criteria, requirement summaries, interview questions, and traceability candidates. They can identify ambiguous wording and propose edge cases. These uses are assistive: requirements still require discussion with stakeholders because an elegant rewrite can preserve an incorrect assumption.

### 3.2 Software design

An LLM can compare architectural alternatives, produce interface drafts, explain design patterns, and generate diagrams or design-document templates. It may help teams explore options quickly, but architectural decisions depend on constraints that may not be present in the prompt: operational cost, organizational skills, latency, compliance, legacy integration, and failure modes. Human review is essential.

### 3.3 Implementation

Code completion and code generation are the most visible uses. Assistants can draft functions, convert code between languages, explain errors, generate boilerplate, and suggest refactorings. These capabilities are strongest when the requested change is small and the repository context is clear. Generated code must still be compiled, tested, reviewed, and checked for dependency and security issues.

### 3.4 Testing and quality assurance

LLMs can generate unit-test cases, test data, assertions, mocks, bug reports, and test explanations. They can increase coverage of routine paths and help developers begin testing unfamiliar code. Generated tests can reproduce the same assumptions as the implementation, however, producing tests that pass without detecting the intended defect. Independent test design and mutation or property-based testing can reduce this risk.

### 3.5 Deployment and operations

LLMs can explain logs, draft CI configurations, generate infrastructure snippets, summarize incidents, and suggest runbook steps. Operational automation has a high blast radius: a wrong command can delete data, expose a service, or cause downtime. Production actions should use least privilege, dry runs, approval gates, and auditable execution rather than unrestricted conversational control.

### 3.6 Maintenance

Maintenance tasks such as documentation updates, code search, migration drafts, bug triage, and localized program repair are good candidates for assistance. Long-lived systems create context challenges. An LLM may miss implicit contracts, historical decisions, or behavior that is not captured in tests. Maintainers must validate changes against regression suites and system-level expectations.

### 3.7 Security

Security work includes vulnerability explanation, secure coding suggestions, threat-model prompts, and review assistance. LLMs can also generate vulnerable code or recommend unsafe packages. Security use must be evidence-based: run static analysis, dependency scanning, secret scanning, tests, and manual review. Sensitive source code and credentials must not be sent to a model without an approved data-governance process.

## 4. Evidence of Benefits

The literature supports benefits, but not a single universal productivity multiplier. Peng et al. reported a controlled experiment in which 95 professional developers implemented a JavaScript HTTP server. Participants with GitHub Copilot completed the task 55.8% faster than the control group. This is important evidence of task-level productivity improvement, but the result came from a specific task and controlled setting; it should not be presented as a guarantee for all software projects.

Broader systematic reviews map a large and diverse research field. Hou et al. reviewed 395 articles and identified applications across numerous software-engineering tasks, including requirements, design, development, quality assurance, maintenance, and management. This breadth suggests that LLM assistance is not limited to code completion. It also makes comparison difficult because “success” can mean speed, correctness, coverage, perceived usefulness, maintainability, or reduced cognitive load.

Reported benefits generally fall into four groups:

- **Efficiency:** faster drafting, search, explanation, and routine transformation.
- **Accessibility:** assistance for learners and developers entering an unfamiliar codebase or language.
- **Quality support:** additional tests, documentation, review prompts, and alternative implementations.
- **Knowledge work:** summarizing changes, translating technical language, and preserving context in project artifacts.

These benefits are most credible when the task has a clear acceptance test and the developer can quickly inspect the result.

## 5. Risks and Limitations

### 5.1 Incorrect or incomplete output

LLMs can produce code that looks reasonable but fails edge cases, violates requirements, or uses an incorrect API. Fluent language increases the danger because confidence in presentation is not evidence of correctness.

### 5.2 Hallucinated dependencies and supply-chain risk

Research on package hallucination shows that models may invent package names or recommend unsuitable dependencies. A developer who installs a fabricated package can waste time; a malicious actor could register a plausible name and create a supply-chain attack. Package existence, provenance, maintenance activity, licensing, and security advisories must be checked independently.

### 5.3 Security vulnerabilities

Generated code may contain weak authentication, injection vulnerabilities, insecure defaults, improper error handling, or exposed secrets. Security cannot be delegated solely to the generator. Automated scanning and human threat modeling are required.

### 5.4 Privacy, copyright, and governance

Prompts can contain proprietary code, personal data, credentials, or confidential business logic. Organizations need clear rules for approved models, retention, access, training use, licensing, and attribution. Developers should remove secrets and minimize sensitive context.

### 5.5 Maintainability and architectural consistency

A locally correct snippet may conflict with project conventions, introduce duplication, or increase technical debt. The larger the codebase, the more important repository-aware context, design documentation, and review become.

### 5.6 Over-reliance and skill effects

If developers accept suggestions without understanding them, short-term speed can reduce long-term expertise and ownership. Education should emphasize verification, debugging, reading code, and explaining design decisions—not just prompt writing.

## 6. Responsible Human-in-the-Loop Workflow

A practical workflow is:

1. Define a small task and measurable acceptance criteria.
2. Provide only the context necessary for the model to help.
3. Ask for assumptions and alternative approaches where ambiguity exists.
4. Inspect every generated change and verify dependencies from official sources.
5. Run formatting, type checks, tests, static analysis, secret scanning, and dependency auditing.
6. Perform human review for correctness, security, maintainability, and licensing.
7. Record meaningful AI assistance when the institution or organization requires it.
8. Monitor the change after integration and update tests or documentation.

This workflow turns the LLM into a high-speed drafting and reasoning aid while preserving engineering accountability.

## 7. Comparative Analysis of Automation Levels

Not all software-development tasks have the same suitability for LLM automation. A useful distinction is between **drafting**, **verification**, and **execution**:

| Automation level | Example | Main control required |
|---|---|---|
| Drafting assistance | Generate a function, test case, or documentation paragraph | Developer inspection and local tests |
| Review assistance | Explain a diff, identify edge cases, or suggest vulnerabilities | Independent review and static analysis |
| Guided transformation | Refactor a bounded module or migrate an API | Small commits, regression tests, and rollback |
| Operational execution | Modify production infrastructure or deploy a release | Least privilege, approval gates, audit logs, and rollback |

This classification explains why a model can be useful without being trusted with unrestricted autonomy. The cost of an error rises as the task moves from drafting to execution. A generated comment is usually easy to correct; an incorrect production migration can cause data loss. Therefore, organizations should match autonomy to risk rather than treating an LLM as either completely safe or completely unsafe.

Benchmark evidence also shows why simple code-generation results do not fully represent software engineering. SWE-bench evaluates whether a model can resolve real GitHub issues by editing an existing repository and passing tests. Its original evaluation found that even strong models solved only a small fraction of issues, with the best reported result in that study at 1.96%. Real issues require repository navigation, interpretation of incomplete requirements, coordination across files, and regression reasoning. This is a substantially harder problem than producing an isolated function from a short prompt.

## 8. Measuring Productivity and Quality Together

Productivity should not be measured only by lines of code or time to first output. A faster first draft can create additional review and debugging work. A more complete evaluation should measure:

- **Speed:** task completion time and time to first working draft.
- **Correctness:** acceptance-test pass rate, defect rate, and issue resolution rate.
- **Quality:** maintainability, readability, architectural consistency, and test coverage.
- **Rework:** number of revisions, reverted changes, and post-review fixes.
- **Security:** vulnerabilities, dependency risk, secret exposure, and policy violations.
- **Developer experience:** cognitive load, confidence, learning, and perceived usefulness.
- **Team outcomes:** review latency, handoff quality, documentation completeness, and operational incidents.

Recent field evidence illustrates the importance of context. A pooled analysis of three workplace experiments involving 4,867 developers reported a 26.08% increase in completed tasks for developers given access to Copilot. A separate randomized enterprise study with 96 Google software engineers reported an estimated reduction of approximately 21% in time spent on a complex enterprise task, while noting a wide confidence interval. These findings complement the earlier 55.8% result from a focused HTTP-server task, but they should not be combined as if they were one universal effect size. The studies use different environments, tasks, outcome definitions, tools, and levels of researcher control.

The appropriate conclusion is conditional: LLM assistance can improve throughput for some developers and tasks, particularly where context is available and output can be checked. The benefit may be offset when the tool produces nearly-correct output that requires substantial debugging. Evaluation should therefore include the total time from task assignment to accepted, maintainable, and secure change.

## 9. Educational and Organizational Implications

LLM-assisted development changes the skills expected of students and professional developers. Syntax recall becomes less central for some tasks, while problem decomposition, specification writing, testing, source evaluation, debugging, security reasoning, and communication become more important. Students should be assessed on whether they can explain and verify a solution, not merely whether they can obtain a working-looking output from a chatbot.

Organizations should introduce LLM tools through bounded pilots. A pilot can begin with documentation, test scaffolding, code explanation, and low-risk refactoring. Teams can then compare baseline and assisted work using a consistent scorecard. Policies should define approved tools, prohibited data, code-review responsibilities, attribution expectations, incident reporting, and criteria for expanding use. Usage volume alone is not proof of value; trust, quality, and rework must be monitored alongside adoption.

## 10. Governance and Secure Adoption Framework

NIST's Generative AI Profile recommends governing, mapping, measuring, and managing risks across the AI lifecycle. Applied to software development, this framework can become a practical control loop:

1. **Govern:** define ownership, acceptable use, data rules, review responsibilities, and escalation paths.
2. **Map:** identify where the model enters the SDLC, what data it receives, what tools it can call, and who may be affected by failure.
3. **Measure:** evaluate accuracy, security, privacy, robustness, maintainability, cost, and developer outcomes before and after adoption.
4. **Manage:** apply safeguards proportional to risk, including access controls, test gates, dependency verification, monitoring, incident response, and periodic reassessment.

For software teams, governance should be connected to ordinary engineering controls rather than treated as a separate document. Pull requests, branch protection, CI, secret scanning, software-composition analysis, static analysis, and release approvals can provide evidence that generated changes were evaluated. Generated code should be held to the same quality and security standards as human-written code; the origin of a line does not determine whether it is safe.

## 11. Research Gaps

Future research should improve ecological validity by measuring complete development tasks in real repositories rather than isolated benchmark prompts. Studies should report correctness, maintainability, security, review time, rework, and long-term outcomes alongside completion time. More evidence is needed for requirements, architecture, deployment, maintenance, and diverse programming communities. Research should also evaluate multi-agent systems, model drift, data governance, package hallucination, energy use, and the effect of AI assistance on developer learning.

Additional open questions include whether AI-generated changes accumulate technical debt over months, how much repository context is actually useful, how junior and senior developers differ in verification behavior, and how organizations can audit model-assisted decisions without creating excessive process overhead. Benchmarks should include realistic incomplete requirements, hidden tests, security constraints, dependency updates, and maintenance tasks. This would better reflect the conditions under which software teams make decisions.

## 12. Conclusion

LLMs are changing software development by automating portions of code production and knowledge work throughout the SDLC. Evidence supports meaningful assistance for bounded tasks, and controlled studies show that some developers can complete selected tasks faster with coding assistants. Nevertheless, LLMs remain probabilistic systems that can be wrong, insecure, or inconsistent. The most defensible position is neither unrestricted automation nor rejection of the technology. LLMs should be integrated as supervised tools within an engineering process that includes clear requirements, independent validation, secure dependency practices, human review, and accountability. Their role is best understood as augmenting developers while shifting their effort toward specification, evaluation, architecture, and responsible decision-making.

## References

See [`references.md`](references.md) for the linked bibliography and evidence notes.
