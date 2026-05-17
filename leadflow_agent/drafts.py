from __future__ import annotations

from typing import Mapping


def summarize_lead(lead: Mapping[str, str]) -> str:
    name = lead.get("name", "Unknown lead")
    business = lead.get("business", "their business")
    need = lead.get("need", "a service request")
    timeline = lead.get("timeline", "unspecified timing")
    budget = lead.get("budget", "unspecified budget")
    return f"{name} from {business} needs {need}. Timeline: {timeline}. Budget: {budget}."


def build_reply_draft(lead: Mapping[str, str], priority: str) -> str:
    name = lead.get("name", "there").split()[0]
    need = lead.get("need", "your request")

    if priority == "hot":
        opener = "Thanks for reaching out. This sounds ready to move, so I can help you map the next step quickly."
        close = "If you send one or two preferred times, I can confirm the best next step today."
    elif priority == "warm":
        opener = "Thanks for the details. I can help you turn this into a clear next step."
        close = "Could you share your target launch date and the main outcome you want from this project?"
    else:
        opener = "Thanks for reaching out. I have enough context to point you in a useful direction."
        close = "If you can share the timeline, budget range, and must-have result, I can suggest the simplest path."

    return (
        f"Hi {name},\n\n"
        f"{opener}\n\n"
        f"From your note, the main need is: {need}.\n\n"
        f"{close}\n\n"
        "Best,\n"
        "LeadFlow Agent"
    )

