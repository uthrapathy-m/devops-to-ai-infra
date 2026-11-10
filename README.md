# DevOps to AI Infrastructure

A 26-week, hands-on roadmap for DevOps, SRE and cloud engineers who want to run AI workloads in production: GPU clusters, model serving, LLM gateways, RAG and AI cost control.

**[Read the roadmap](https://uthrapathy-m.github.io/devops-to-ai-infra/)** · [Download the PDF (A4)](docs/devops-to-ai-infra-roadmap.pdf) · [Code examples](examples/)

## Who it's for

- You have 1–5 years in DevOps, SRE or cloud engineering.
- You deploy to Kubernetes but haven't operated clusters in depth.
- You know little or no Python, and no machine learning.
- You can spend 8–10 hours a week and about $25–60 a month on cloud resources.

You don't need a GPU at home or a background in data science. The plan builds on infrastructure skills you already have.

## Why AI infrastructure

There are three AI lanes open to a DevOps engineer:

| Lane | What you run | Fit for DevOps |
|---|---|---|
| **AI infrastructure** (focus of this plan) | GPU clusters, vLLM/KServe serving, autoscaling, GPU cost | Highest: it builds on Kubernetes, IaC and cloud |
| **LLMOps** (second skill) | LLM gateways, RAG, evals, tracing, guardrails | High: every company calling LLM APIs needs it |
| **MLOps** (awareness only) | Training pipelines, feature stores, model registries | Medium: tooling is consolidating into managed platforms |

## The roadmap

| Phase | Weeks | Focus | You finish with |
|---|---|---|---|
| 1 | 1–4 | Python and LLM basics | A FastAPI log summarizer on kind, and a VRAM calculator |
| 2 | 5–8 | Kubernetes operations | CKA certification and solid knowledge of scheduling |
| 3 | 9–12 | LLM gateway (LiteLLM) | Keys and budgets per team, fallbacks, cost dashboards |
| 4 | 13–18 | GPU model serving (flagship) | vLLM on EKS spot GPUs with Karpenter and KEDA, benchmarked |
| 5 | 19–22 | RAG, evals and security | A RAG assistant with evals in CI and a threat model |
| 6 | 23–26 | Platform polish and job market | GitOps for models, GPU FinOps, portfolio, interviews |

Each phase in the [full roadmap](https://uthrapathy-m.github.io/devops-to-ai-infra/) has a week-by-week table, architecture diagrams and a "done when" checklist. Starter code lives separately in [`examples/`](examples/). It also covers:

- GPU memory sizing and cost per 1M tokens, with the formulas
- How to build in public: a post plan with one measured result per post
- A budget with a cost-control setup (AWS Budgets in Terraform)
- Certifications worth getting, and which to skip
- AI infrastructure interview questions and what a strong answer covers
- A "top 1%" checklist and curated resources

## Code examples

| Path | What it is |
|---|---|
| [`examples/phase-1-python/restarts.py`](examples/phase-1-python/restarts.py) | First Python script: find pods that restart often |
| [`examples/phase-1-python/log_summarizer_app.py`](examples/phase-1-python/log_summarizer_app.py) | FastAPI service that summarizes logs with an LLM |
| [`examples/phase-3-llm-gateway/`](examples/phase-3-llm-gateway/) | LiteLLM proxy config, Helm install and per-team keys |
| [`examples/phase-4-gpu-serving/`](examples/phase-4-gpu-serving/) | Karpenter GPU NodePool, vLLM Deployment, KEDA autoscaling, async benchmark |
| [`examples/cost-control/budget.tf`](examples/cost-control/budget.tf) | AWS monthly budget alarm. Apply it before any GPU work. |

The examples are starting points for learning, not production-hardened manifests. Pin image tags and model IDs you have tested, and check current cloud prices before running anything on GPUs.

```bash
pip install -r examples/requirements.txt
python examples/phase-1-python/restarts.py
uvicorn log_summarizer_app:app --app-dir examples/phase-1-python --reload
```

## How to use this repo

1. Read section 01 of the roadmap and adjust the plan to your starting point: skip phases you've already covered.
2. Fork the repo and track your progress with one GitHub issue per phase.
3. Publish what you build with your own numbers. Measured results are what make a portfolio stand out.

## Contributing

Corrections and improvements are welcome, especially updated prices, versions and links. Open an issue or a pull request.

## License

[MIT](LICENSE)
