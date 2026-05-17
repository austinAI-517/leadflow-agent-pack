from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


HIGH_INTENT_TERMS = (
    "urgent",
    "asap",
    "this week",
    "ready",
    "quote",
    "proposal",
    "book",
    "call",
    "pricing",
    "hire",
)

LOW_INTENT_TERMS = (
    "curious",
    "maybe",
    "someday",
    "research",
    "just looking",
    "not sure",
)


@dataclass(frozen=True)
class LeadScore:
    score: int
    priority: str
    next_action: str
    reason: str


def score_lead(lead: Mapping[str, str]) -> LeadScore:
    text = " ".join(str(value or "").lower() for value in lead.values())
    budget = _parse_budget(lead.get("budget", ""))
    score = 40
    reasons: list[str] = []

    if any(term in text for term in HIGH_INTENT_TERMS):
        score += 25
        reasons.append("high-intent language")

    if any(term in text for term in LOW_INTENT_TERMS):
        score -= 15
        reasons.append("low-intent language")

    if budget >= 5000:
        score += 20
        reasons.append("strong budget")
    elif budget >= 1500:
        score += 10
        reasons.append("workable budget")
    elif budget and budget < 500:
        score -= 10
        reasons.append("low budget")

    timeline = str(lead.get("timeline", "")).lower()
    if any(term in timeline for term in ("today", "this week", "asap", "urgent")):
        score += 15
        reasons.append("near-term timeline")
    elif any(term in timeline for term in ("next quarter", "later", "not sure")):
        score -= 10
        reasons.append("unclear timeline")

    score = max(0, min(100, score))
    priority, next_action = _priority_for_score(score)
    return LeadScore(
        score=score,
        priority=priority,
        next_action=next_action,
        reason=", ".join(reasons) if reasons else "standard lead profile",
    )


def _priority_for_score(score: int) -> tuple[str, str]:
    if score >= 80:
        return "hot", "Reply within 1 hour and offer a booking link."
    if score >= 60:
        return "warm", "Reply today with 2-3 qualifying questions."
    if score >= 40:
        return "nurture", "Send a helpful reply and ask for missing details."
    return "low", "Add to follow-up list unless capacity is open."


def _parse_budget(value: str | None) -> int:
    if not value:
        return 0
    digits = "".join(char for char in str(value) if char.isdigit())
    return int(digits) if digits else 0

