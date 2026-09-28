#!/usr/bin/env python3
"""
Build polished college-submission documents (DOCX + PDF) for the
"Role of Large Language Models in Automating Software Development
Processes" research project.

Single source of content -> both formats, so the Word and PDF copies
stay identical. Run: python build_docs.py
Outputs: docs/LLM-Software-Development-Research.docx
         docs/LLM-Software-Development-Research.pdf
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")
DOCX_OUT = os.path.join(DOCS, "LLM-Software-Development-Research.docx")
PDF_OUT = os.path.join(DOCS, "LLM-Software-Development-Research.pdf")

TITLE = "The Role of Large Language Models in Automating Software Development Processes"
SUBTITLE = "A Structured Literature Review and Evidence Synthesis"

# --- Title-page fields: fill these in before final submission ---
META = [
    ("Submitted by", "________________________"),
    ("Roll / Enrollment No.", "________________________"),
    ("Course / Programme", "________________________"),
    ("Institution", "________________________"),
    ("Supervisor / Guide", "________________________"),
    ("Submission Date", "________________________"),
]

ABSTRACT = (
    "Large language models (LLMs) are increasingly embedded in software development "
    "tools that generate code, explain unfamiliar systems, write tests, summarize "
    "changes, and assist with debugging. This paper reviews how these systems affect "
    "the software development life cycle (SDLC), what evidence supports productivity "
    "and quality claims, and which risks limit dependable automation. A structured "
    "literature review was used to organize evidence across requirements engineering, "
    "design, implementation, testing, deployment, maintenance, and security. The "
    "literature indicates that LLMs are particularly valuable for bounded, repetitive, "
    "and language-heavy tasks. Controlled evidence also reports meaningful reductions "
    "in completion time for selected programming tasks. However, benefits are task- and "
    "context-dependent. LLMs can produce incorrect code, insecure suggestions, "
    "fabricated APIs or packages, privacy risks, and maintenance problems. The central "
    "conclusion is that LLMs should be treated as supervised engineering instruments "
    "rather than autonomous replacements for developers. Effective adoption combines "
    "human judgment, automated tests, security and dependency checks, documentation, "
    "and clear accountability."
)

KEYWORDS = (
    "large language models, software engineering, code generation, developer "
    "productivity, software development life cycle, AI-assisted programming, "
    "responsible AI"
)

# Content model: list of blocks.
# ("h1", text) ("h2", text) ("p", text) ("bullets", [..]) ("numbers", [..])
# ("table", {"header":[...], "rows":[[...],...]})
SECTIONS = [
    ("h1", "1. Introduction"),
    ("p", "Software development contains both creative and repetitive work. Engineers interpret requirements, design systems, implement features, test behavior, maintain code, and communicate decisions. LLM-based assistants can now participate in many of these activities through natural-language prompts and contextual code completion. This creates an opportunity to automate parts of the SDLC, but it also creates a risk of accepting plausible output without sufficient verification."),
    ("p", "The phrase \u201cautomating software development\u201d should therefore be used precisely. An LLM does not independently guarantee a production-ready system. It generates predictions based on learned patterns and available context. Automation is useful when a task has a clear specification, observable output, and reliable validation. A human remains responsible for defining the problem, evaluating trade-offs, and approving changes."),
    ("p", "This paper addresses five questions:"),
    ("numbers", [
        "Which SDLC activities can LLMs support or automate?",
        "What benefits have controlled studies and surveys reported?",
        "What risks and limitations affect dependable adoption?",
        "What human oversight and evaluation practices are required?",
        "Which research gaps remain open?",
    ]),

    ("h1", "2. Methodology"),
    ("p", "This project uses a structured literature review and thematic evidence synthesis. Searches combined terms such as \u201clarge language model,\u201d \u201cLLM,\u201d \u201csoftware engineering,\u201d \u201ccode generation,\u201d \u201ctesting,\u201d \u201cprogram repair,\u201d \u201cdeveloper productivity,\u201d and \u201csecurity.\u201d Priority was given to peer-reviewed publications, systematic reviews, official research reports, and open preprints with clear methods."),
    ("p", "Sources were included when they evaluated or synthesized LLM use in software engineering and reported a method, benchmark, experiment, survey, or review protocol. General LLM papers unrelated to software development, unsupported marketing claims, duplicates, and sources without attributable evidence were excluded. The review does not perform a statistical meta-analysis because the studies differ substantially in tasks, populations, tools, and metrics. The extraction matrix records each source\u2019s task, evidence, result, and limitation."),

    ("h1", "3. LLMs Across the SDLC"),
    ("h2", "3.1 Requirements engineering"),
    ("p", "LLMs can transform stakeholder statements into user stories, acceptance criteria, requirement summaries, interview questions, and traceability candidates. They can identify ambiguous wording and propose edge cases. These uses are assistive: requirements still require discussion with stakeholders because an elegant rewrite can preserve an incorrect assumption."),
    ("h2", "3.2 Software design"),
    ("p", "An LLM can compare architectural alternatives, produce interface drafts, explain design patterns, and generate diagrams or design-document templates. It may help teams explore options quickly, but architectural decisions depend on constraints that may not be present in the prompt: operational cost, organizational skills, latency, compliance, legacy integration, and failure modes. Human review is essential."),
    ("h2", "3.3 Implementation"),
    ("p", "Code completion and code generation are the most visible uses. Assistants can draft functions, convert code between languages, explain errors, generate boilerplate, and suggest refactorings. These capabilities are strongest when the requested change is small and the repository context is clear. Generated code must still be compiled, tested, reviewed, and checked for dependency and security issues."),
    ("h2", "3.4 Testing and quality assurance"),
    ("p", "LLMs can generate unit-test cases, test data, assertions, mocks, bug reports, and test explanations. They can increase coverage of routine paths and help developers begin testing unfamiliar code. Generated tests can reproduce the same assumptions as the implementation, however, producing tests that pass without detecting the intended defect. Independent test design and mutation or property-based testing can reduce this risk."),
    ("h2", "3.5 Deployment and operations"),
    ("p", "LLMs can explain logs, draft CI configurations, generate infrastructure snippets, summarize incidents, and suggest runbook steps. Operational automation has a high blast radius: a wrong command can delete data, expose a service, or cause downtime. Production actions should use least privilege, dry runs, approval gates, and auditable execution rather than unrestricted conversational control."),
    ("h2", "3.6 Maintenance"),
    ("p", "Maintenance tasks such as documentation updates, code search, migration drafts, bug triage, and localized program repair are good candidates for assistance. Long-lived systems create context challenges. An LLM may miss implicit contracts, historical decisions, or behavior that is not captured in tests. Maintainers must validate changes against regression suites and system-level expectations."),
    ("h2", "3.7 Security"),
    ("p", "Security work includes vulnerability explanation, secure coding suggestions, threat-model prompts, and review assistance. LLMs can also generate vulnerable code or recommend unsafe packages. Security use must be evidence-based: run static analysis, dependency scanning, secret scanning, tests, and manual review. Sensitive source code and credentials must not be sent to a model without an approved data-governance process."),

    ("h1", "4. Evidence of Benefits"),
    ("p", "The literature supports benefits, but not a single universal productivity multiplier. Peng et al. reported a controlled experiment in which 95 professional developers implemented a JavaScript HTTP server. Participants with GitHub Copilot completed the task 55.8% faster than the control group. This is important evidence of task-level productivity improvement, but the result came from a specific task and controlled setting; it should not be presented as a guarantee for all software projects."),
    ("p", "Broader systematic reviews map a large and diverse research field. Hou et al. reviewed 395 articles and identified applications across numerous software-engineering tasks, including requirements, design, development, quality assurance, maintenance, and management. This breadth suggests that LLM assistance is not limited to code completion. It also makes comparison difficult because \u201csuccess\u201d can mean speed, correctness, coverage, perceived usefulness, maintainability, or reduced cognitive load."),
    ("p", "Reported benefits generally fall into four groups:"),
    ("bullets", [
        "Efficiency: faster drafting, search, explanation, and routine transformation.",
        "Accessibility: assistance for learners and developers entering an unfamiliar codebase or language.",
        "Quality support: additional tests, documentation, review prompts, and alternative implementations.",
        "Knowledge work: summarizing changes, translating technical language, and preserving context in project artifacts.",
    ]),
    ("p", "These benefits are most credible when the task has a clear acceptance test and the developer can quickly inspect the result."),

    ("h1", "5. Risks and Limitations"),
    ("h2", "5.1 Incorrect or incomplete output"),
    ("p", "LLMs can produce code that looks reasonable but fails edge cases, violates requirements, or uses an incorrect API. Fluent language increases the danger because confidence in presentation is not evidence of correctness."),
    ("h2", "5.2 Hallucinated dependencies and supply-chain risk"),
    ("p", "Research on package hallucination shows that models may invent package names or recommend unsuitable dependencies. A developer who installs a fabricated package can waste time; a malicious actor could register a plausible name and create a supply-chain attack. Package existence, provenance, maintenance activity, licensing, and security advisories must be checked independently."),
    ("h2", "5.3 Security vulnerabilities"),
    ("p", "Generated code may contain weak authentication, injection vulnerabilities, insecure defaults, improper error handling, or exposed secrets. Security cannot be delegated solely to the generator. Automated scanning and human threat modeling are required."),
    ("h2", "5.4 Privacy, copyright, and governance"),
    ("p", "Prompts can contain proprietary code, personal data, credentials, or confidential business logic. Organizations need clear rules for approved models, retention, access, training use, licensing, and attribution. Developers should remove secrets and minimize sensitive context."),
    ("h2", "5.5 Maintainability and architectural consistency"),
    ("p", "A locally correct snippet may conflict with project conventions, introduce duplication, or increase technical debt. The larger the codebase, the more important repository-aware context, design documentation, and review become."),
    ("h2", "5.6 Over-reliance and skill effects"),
    ("p", "If developers accept suggestions without understanding them, short-term speed can reduce long-term expertise and ownership. Education should emphasize verification, debugging, reading code, and explaining design decisions\u2014not just prompt writing."),

    ("h1", "6. Responsible Human-in-the-Loop Workflow"),
    ("p", "A practical workflow is:"),
    ("numbers", [
        "Define a small task and measurable acceptance criteria.",
        "Provide only the context necessary for the model to help.",
        "Ask for assumptions and alternative approaches where ambiguity exists.",
        "Inspect every generated change and verify dependencies from official sources.",
        "Run formatting, type checks, tests, static analysis, secret scanning, and dependency auditing.",
        "Perform human review for correctness, security, maintainability, and licensing.",
        "Record meaningful AI assistance when the institution or organization requires it.",
        "Monitor the change after integration and update tests or documentation.",
    ]),
    ("p", "This workflow turns the LLM into a high-speed drafting and reasoning aid while preserving engineering accountability."),

    ("h1", "7. Comparative Analysis of Automation Levels"),
    ("p", "Not all software-development tasks have the same suitability for LLM automation. A useful distinction is between drafting, verification, and execution:"),
    ("table", {
        "header": ["Automation level", "Example", "Main control required"],
        "rows": [
            ["Drafting assistance", "Generate a function, test case, or documentation paragraph", "Developer inspection and local tests"],
            ["Review assistance", "Explain a diff, identify edge cases, or suggest vulnerabilities", "Independent review and static analysis"],
            ["Guided transformation", "Refactor a bounded module or migrate an API", "Small commits, regression tests, and rollback"],
            ["Operational execution", "Modify production infrastructure or deploy a release", "Least privilege, approval gates, audit logs, and rollback"],
        ],
    }),
    ("p", "This classification explains why a model can be useful without being trusted with unrestricted autonomy. The cost of an error rises as the task moves from drafting to execution. A generated comment is usually easy to correct; an incorrect production migration can cause data loss. Therefore, organizations should match autonomy to risk rather than treating an LLM as either completely safe or completely unsafe."),
    ("p", "Benchmark evidence also shows why simple code-generation results do not fully represent software engineering. SWE-bench evaluates whether a model can resolve real GitHub issues by editing an existing repository and passing tests. Its original evaluation found that even strong models solved only a small fraction of issues, with the best reported result in that study at 1.96%. Real issues require repository navigation, interpretation of incomplete requirements, coordination across files, and regression reasoning. This is a substantially harder problem than producing an isolated function from a short prompt."),

    ("h1", "8. Measuring Productivity and Quality Together"),
    ("p", "Productivity should not be measured only by lines of code or time to first output. A faster first draft can create additional review and debugging work. A more complete evaluation should measure:"),
    ("bullets", [
        "Speed: task completion time and time to first working draft.",
        "Correctness: acceptance-test pass rate, defect rate, and issue resolution rate.",
        "Quality: maintainability, readability, architectural consistency, and test coverage.",
        "Rework: number of revisions, reverted changes, and post-review fixes.",
        "Security: vulnerabilities, dependency risk, secret exposure, and policy violations.",
        "Developer experience: cognitive load, confidence, learning, and perceived usefulness.",
        "Team outcomes: review latency, handoff quality, documentation completeness, and operational incidents.",
    ]),
    ("p", "Recent field evidence illustrates the importance of context. A pooled analysis of three workplace experiments involving 4,867 developers reported a 26.08% increase in completed tasks for developers given access to Copilot. A separate randomized enterprise study with 96 Google software engineers reported an estimated reduction of approximately 21% in time spent on a complex enterprise task, while noting a wide confidence interval. These findings complement the earlier 55.8% result from a focused HTTP-server task, but they should not be combined as if they were one universal effect size. The studies use different environments, tasks, outcome definitions, tools, and levels of researcher control."),
    ("p", "The appropriate conclusion is conditional: LLM assistance can improve throughput for some developers and tasks, particularly where context is available and output can be checked. The benefit may be offset when the tool produces nearly-correct output that requires substantial debugging. Evaluation should therefore include the total time from task assignment to accepted, maintainable, and secure change."),

    ("h1", "9. Educational and Organizational Implications"),
    ("p", "LLM-assisted development changes the skills expected of students and professional developers. Syntax recall becomes less central for some tasks, while problem decomposition, specification writing, testing, source evaluation, debugging, security reasoning, and communication become more important. Students should be assessed on whether they can explain and verify a solution, not merely whether they can obtain a working-looking output from a chatbot."),
    ("p", "Organizations should introduce LLM tools through bounded pilots. A pilot can begin with documentation, test scaffolding, code explanation, and low-risk refactoring. Teams can then compare baseline and assisted work using a consistent scorecard. Policies should define approved tools, prohibited data, code-review responsibilities, attribution expectations, incident reporting, and criteria for expanding use. Usage volume alone is not proof of value; trust, quality, and rework must be monitored alongside adoption."),

    ("h1", "10. Governance and Secure Adoption Framework"),
    ("p", "NIST\u2019s Generative AI Profile recommends governing, mapping, measuring, and managing risks across the AI lifecycle. Applied to software development, this framework can become a practical control loop:"),
    ("numbers", [
        "Govern: define ownership, acceptable use, data rules, review responsibilities, and escalation paths.",
        "Map: identify where the model enters the SDLC, what data it receives, what tools it can call, and who may be affected by failure.",
        "Measure: evaluate accuracy, security, privacy, robustness, maintainability, cost, and developer outcomes before and after adoption.",
        "Manage: apply safeguards proportional to risk, including access controls, test gates, dependency verification, monitoring, incident response, and periodic reassessment.",
    ]),
    ("p", "For software teams, governance should be connected to ordinary engineering controls rather than treated as a separate document. Pull requests, branch protection, CI, secret scanning, software-composition analysis, static analysis, and release approvals can provide evidence that generated changes were evaluated. Generated code should be held to the same quality and security standards as human-written code; the origin of a line does not determine whether it is safe."),

    ("h1", "11. Research Gaps"),
    ("p", "Future research should improve ecological validity by measuring complete development tasks in real repositories rather than isolated benchmark prompts. Studies should report correctness, maintainability, security, review time, rework, and long-term outcomes alongside completion time. More evidence is needed for requirements, architecture, deployment, maintenance, and diverse programming communities. Research should also evaluate multi-agent systems, model drift, data governance, package hallucination, energy use, and the effect of AI assistance on developer learning."),
    ("p", "Additional open questions include whether AI-generated changes accumulate technical debt over months, how much repository context is actually useful, how junior and senior developers differ in verification behavior, and how organizations can audit model-assisted decisions without creating excessive process overhead. Benchmarks should include realistic incomplete requirements, hidden tests, security constraints, dependency updates, and maintenance tasks. This would better reflect the conditions under which software teams make decisions."),

    ("h1", "12. Conclusion"),
    ("p", "LLMs are changing software development by automating portions of code production and knowledge work throughout the SDLC. Evidence supports meaningful assistance for bounded tasks, and controlled studies show that some developers can complete selected tasks faster with coding assistants. Nevertheless, LLMs remain probabilistic systems that can be wrong, insecure, or inconsistent. The most defensible position is neither unrestricted automation nor rejection of the technology. LLMs should be integrated as supervised tools within an engineering process that includes clear requirements, independent validation, secure dependency practices, human review, and accountability. Their role is best understood as augmenting developers while shifting their effort toward specification, evaluation, architecture, and responsible decision-making."),
]

REFERENCES = [
    "Peng, S. et al. (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. Controlled experiment with 95 professional developers completing a JavaScript HTTP-server task; reports a 55.8% faster completion time for the treatment group. arXiv:2302.06590.",
    "Hou, X. et al. (2024). Large Language Models for Software Engineering: A Systematic Literature Review. ACM Transactions on Software Engineering and Methodology. Review of 395 articles. DOI: 10.1145/3695988.",
    "He, J., Treude, C., and Lo, D. (2024). LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead. arXiv:2404.04834.",
    "Krishna, A. et al. (2025). Importing Phantoms: Measuring LLM Package Hallucination Vulnerabilities. arXiv:2501.19012.",
    "Microsoft Research / MIT / Princeton / Wharton authors (2024). Dear Diary: A Randomized Controlled Trial of Generative AI Coding Tools in the Workplace. arXiv:2410.18334.",
    "Zhang, Q. et al. (2025). A Survey on Large Language Models for Software Engineering. Science China Information Sciences. DOI: 10.1007/s11432-025-4670-0.",
    "Jimenez, C. E. et al. (2024). SWE-bench: Can Language Models Resolve Real-world GitHub Issues? ICLR 2024. arXiv:2310.06770.",
    "Cui, M. et al. (2025). The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers. Pooled analysis of 4,867 developers. MIT working paper.",
    "Peng, S. et al. (2024). How Much Does AI Impact Development Speed? An Enterprise-based Randomized Controlled Trial. 96 Google software engineers. arXiv:2410.12944.",
    "Autio, C. et al. (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. DOI: 10.6028/NIST.AI.600-1.",
    "NIST (2024). Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile. NIST SP 800-218A.",
    "Stack Overflow (2025). 2025 Stack Overflow Developer Survey \u2014 AI. Developer survey, not controlled causal evidence.",
]

NOTE = ("Scope and academic integrity: This project is a structured literature review and "
        "evidence synthesis. It does not claim that an original human-subject experiment was "
        "conducted; reported numerical findings are attributed to the cited studies and are "
        "not presented as universal guarantees. Convert the bibliography to the citation "
        "style required by your institution (IEEE, APA, or MLA) and complete the title-page "
        "fields before submission.")


def build_docx():
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT

    doc = Document()

    # Base style
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    NAVY = RGBColor(0x1F, 0x2A, 0x44)
    for hstyle, size in (("Heading 1", 15), ("Heading 2", 12), ("Title", 24)):
        st = doc.styles[hstyle]
        st.font.color.rgb = NAVY
        st.font.name = "Calibri"

    # ---- Title page ----
    doc.add_paragraph()
    doc.add_paragraph()
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(TITLE)
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = NAVY

    st = doc.add_paragraph()
    st.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = st.add_run(SUBTITLE)
    sr.italic = True
    sr.font.size = Pt(13)

    doc.add_paragraph()
    doc.add_paragraph()

    meta_tbl = doc.add_table(rows=0, cols=2)
    meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for label, value in META:
        row = meta_tbl.add_row().cells
        lp = row[0].paragraphs[0]
        lr = lp.add_run(label)
        lr.bold = True
        lr.font.size = Pt(11)
        row[1].paragraphs[0].add_run(value).font.size = Pt(11)

    doc.add_page_break()

    # ---- Abstract ----
    doc.add_heading("Abstract", level=1)
    doc.add_paragraph(ABSTRACT)
    kp = doc.add_paragraph()
    kr = kp.add_run("Keywords: ")
    kr.bold = True
    kp.add_run(KEYWORDS)

    doc.add_paragraph()
    note = doc.add_paragraph()
    nr = note.add_run(NOTE)
    nr.italic = True
    nr.font.size = Pt(9.5)

    doc.add_page_break()

    # ---- Table of contents (field; Word populates on open) ----
    doc.add_heading("Contents", level=1)
    _add_toc_field(doc)
    doc.add_page_break()

    # ---- Body ----
    for kind, payload in SECTIONS:
        if kind == "h1":
            doc.add_heading(payload, level=1)
        elif kind == "h2":
            doc.add_heading(payload, level=2)
        elif kind == "p":
            doc.add_paragraph(payload)
        elif kind == "bullets":
            for item in payload:
                doc.add_paragraph(item, style="List Bullet")
        elif kind == "numbers":
            for item in payload:
                doc.add_paragraph(item, style="List Number")
        elif kind == "table":
            _docx_table(doc, payload)

    # ---- References ----
    doc.add_heading("References", level=1)
    for i, ref in enumerate(REFERENCES, 1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.first_line_indent = Inches(-0.3)
        p.add_run(f"[{i}] ").bold = True
        p.add_run(ref)

    # ---- Footer page numbers ----
    _add_page_numbers(doc)

    doc.save(DOCX_OUT)


def _docx_table(doc, spec):
    from docx.shared import Pt, RGBColor
    from docx.enum.table import WD_TABLE_ALIGNMENT
    header = spec["header"]
    rows = spec["rows"]
    tbl = doc.add_table(rows=1, cols=len(header))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, h in enumerate(header):
        p = hdr[i].paragraphs[0]
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(10.5)
        _shade_cell(hdr[i], "1F2A44")
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for r in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(r):
            cells[i].paragraphs[0].add_run(val).font.size = Pt(10)
    doc.add_paragraph()


def _shade_cell(cell, hex_color):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def _add_toc_field(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    p = doc.add_paragraph()
    run = p.add_run()
    fldBegin = OxmlElement("w:fldChar")
    fldBegin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-2" \\h \\z \\u'
    fldSep = OxmlElement("w:fldChar")
    fldSep.set(qn("w:fldCharType"), "separate")
    hint = OxmlElement("w:t")
    hint.text = "Right-click and choose \u201cUpdate Field\u201d to build the table of contents."
    fldEnd = OxmlElement("w:fldChar")
    fldEnd.set(qn("w:fldCharType"), "end")
    for el in (fldBegin, instr, fldSep, hint, fldEnd):
        run._r.append(el)


def _add_page_numbers(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    section = doc.sections[0]
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = "PAGE"
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    run._r.append(b); run._r.append(instr); run._r.append(e)


def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from reportlab.platypus import (
        BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
        Table, TableStyle, PageBreak, ListFlowable, ListItem,
    )

    NAVY = colors.HexColor("#1F2A44")
    styles = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica",
                          fontSize=10.5, leading=15, alignment=TA_JUSTIFY, spaceAfter=6)
    h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                        fontSize=15, textColor=NAVY, spaceBefore=12, spaceAfter=6)
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                        fontSize=12, textColor=NAVY, spaceBefore=8, spaceAfter=4)
    title = ParagraphStyle("TitleBig", parent=styles["Title"], fontName="Helvetica-Bold",
                          fontSize=22, textColor=NAVY, alignment=TA_CENTER, leading=27)
    subtitle = ParagraphStyle("Sub", parent=styles["Normal"], fontName="Helvetica-Oblique",
                             fontSize=13, alignment=TA_CENTER, spaceBefore=8)
    note_style = ParagraphStyle("Note", parent=body, fontName="Helvetica-Oblique",
                               fontSize=9, textColor=colors.HexColor("#444444"))
    ref_style = ParagraphStyle("Ref", parent=body, leftIndent=16, firstLineIndent=-16, spaceAfter=5)
    meta_style = ParagraphStyle("Meta", parent=styles["Normal"], fontSize=11, leading=20)

    story = []

    # ---- Title page ----
    story.append(Spacer(1, 55 * mm))
    story.append(Paragraph(TITLE, title))
    story.append(Paragraph(SUBTITLE, subtitle))
    story.append(Spacer(1, 24 * mm))
    meta_rows = [[Paragraph(f"<b>{l}</b>", meta_style), Paragraph(v, meta_style)] for l, v in META]
    mt = Table(meta_rows, colWidths=[55 * mm, 90 * mm], hAlign="CENTER")
    mt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(mt)
    story.append(PageBreak())

    # ---- Abstract ----
    story.append(Paragraph("Abstract", h1))
    story.append(Paragraph(ABSTRACT, body))
    story.append(Paragraph(f"<b>Keywords:</b> {KEYWORDS}", body))
    story.append(Spacer(1, 6))
    story.append(Paragraph(NOTE, note_style))
    story.append(PageBreak())

    # ---- Body ----
    for kind, payload in SECTIONS:
        if kind == "h1":
            story.append(Paragraph(payload, h1))
        elif kind == "h2":
            story.append(Paragraph(payload, h2))
        elif kind == "p":
            story.append(Paragraph(payload, body))
        elif kind == "bullets":
            items = [ListItem(Paragraph(x, body), leftIndent=14) for x in payload]
            story.append(ListFlowable(items, bulletType="bullet", start="\u2022"))
            story.append(Spacer(1, 4))
        elif kind == "numbers":
            items = [ListItem(Paragraph(x, body), leftIndent=14) for x in payload]
            story.append(ListFlowable(items, bulletType="1"))
            story.append(Spacer(1, 4))
        elif kind == "table":
            _pdf_table(story, payload, body, NAVY, colors)

    # ---- References ----
    story.append(Paragraph("References", h1))
    for i, ref in enumerate(REFERENCES, 1):
        story.append(Paragraph(f"<b>[{i}]</b> {ref}", ref_style))

    # ---- Doc template with page numbers ----
    def footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawCentredString(A4[0] / 2, 12 * mm, str(doc_.page))
        canvas.restoreState()

    doc = BaseDocTemplate(PDF_OUT, pagesize=A4,
                          leftMargin=22 * mm, rightMargin=22 * mm,
                          topMargin=20 * mm, bottomMargin=20 * mm,
                          title=TITLE, author="LLM Software Development Research")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
    doc.build(story)


def _pdf_table(story, spec, body, navy, colors):
    from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    cell = ParagraphStyle("Cell", parent=body, fontSize=9.5, leading=12, alignment=0, spaceAfter=0)
    hcell = ParagraphStyle("HCell", parent=cell, textColor=colors.white, fontName="Helvetica-Bold")
    header = [Paragraph(h, hcell) for h in spec["header"]]
    data = [header] + [[Paragraph(c, cell) for c in row] for row in spec["rows"]]
    t = Table(data, colWidths=[38 * mm, 68 * mm, 60 * mm], hAlign="CENTER", repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), navy),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#AAAAAA")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F4F8")]),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))


if __name__ == "__main__":
    build_docx()
    print("DOCX ->", DOCX_OUT)
    build_pdf()
    print("PDF  ->", PDF_OUT)
