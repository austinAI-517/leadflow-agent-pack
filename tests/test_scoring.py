from leadflow_agent.scoring import score_lead


def test_hot_lead_has_high_priority() -> None:
    lead = {
        "need": "Need a quote and booking this week",
        "timeline": "asap",
        "budget": "$8000",
    }

    scored = score_lead(lead)

    assert scored.priority == "hot"
    assert scored.score >= 80


def test_low_intent_lead_is_not_hot() -> None:
    lead = {
        "need": "Just looking and maybe curious",
        "timeline": "next quarter",
        "budget": "$300",
    }

    scored = score_lead(lead)

    assert scored.priority in {"low", "nurture"}
    assert scored.score < 60

