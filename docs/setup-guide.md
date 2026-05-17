# Setup Guide

## Run The Local Demo

From the project folder:

```bash
python3 -m leadflow_agent.cli examples/demo-leads.csv sample-output/demo-output.jsonl
```

## Input Format

The demo expects a CSV with these columns:

- `name`
- `email`
- `business`
- `need`
- `timeline`
- `budget`
- `source`

## Output Format

Each processed lead is written as one JSON line with:

- original lead fields
- summary
- score
- priority
- next action
- scoring reason
- reply draft

## Adapting To A Real Workflow

1. Export a small sample of real leads.
2. Map the real columns to the demo fields.
3. Adjust scoring terms in `leadflow_agent/scoring.py`.
4. Adjust tone and reply style in `leadflow_agent/drafts.py`.
5. Send output to the business's preferred handoff tool.

## Recommended Live Safety

Keep human review in the first version. Drafting replies is useful and safe; automatically sending replies should only be added after the business confirms approval rules, tone, and compliance boundaries.

