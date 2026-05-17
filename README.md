# LeadFlow Agent Pack

LeadFlow Agent Pack is a practical demo and starter kit for AI-assisted lead intake.

It turns raw lead rows into:

- a short buyer summary
- a lead score from 0 to 100
- a priority bucket
- a recommended next action
- a ready-to-edit follow-up draft

The demo is intentionally lightweight: it runs locally, uses no paid API, and keeps the default workflow human-reviewed instead of auto-sending messages.

## Who It Helps

LeadFlow is designed for small service businesses that receive leads from forms, ads, email exports, spreadsheets, or CRM exports and need a faster way to decide who to follow up with first.

Good first use cases:

- real estate buyer or seller inquiries
- renovation and home service requests
- agency discovery-call requests
- legal or consulting intake triage
- local business quote requests

## Quick Start

```bash
python3 -m leadflow_agent.cli examples/demo-leads.csv sample-output/demo-output.jsonl
```

Open `sample-output/demo-output.jsonl` to inspect the generated lead summaries, scores, priorities, next actions, and reply drafts.

## Example Output

```json
{
  "summary": "Maya Chen from Northside Renovations needs quote follow-up automation for website leads. Timeline: this week. Budget: $3500.",
  "score": 90,
  "priority": "hot",
  "next_action": "Reply within 1 hour and offer a booking link."
}
```

## Package Structure

```text
leadflow_agent/
  cli.py        # CSV processor
  scoring.py    # lead scoring and priority rules
  drafts.py     # buyer summaries and reply drafts
examples/
  demo-leads.csv
sample-output/
  demo-output.jsonl
tests/
  test_scoring.py
```

## Customization Ideas

- Connect output to Airtable, Notion, Google Sheets, HubSpot, or another CRM.
- Replace rule-based scoring with model-assisted classification.
- Add niche-specific scoring for real estate, home services, legal intake, or agencies.
- Generate different follow-up drafts for hot, warm, nurture, and low-priority leads.
- Add an approval step before any outbound message is sent.

## Safety Defaults

- The demo drafts replies only; it does not send email.
- It does not include customer data.
- It does not require API keys.
- It is meant to be customized before live business use.

