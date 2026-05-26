from app.rules import (
    repeated_bonus_claims,
    low_deposit_high_bonus,
    fast_withdrawal_pattern,
    short_risky_session,
    duplicate_ip,
    duplicate_device,
)


def calculate_risk_score(players, player):
    score = 0
    reasons = []

    if repeated_bonus_claims(player):
        score += 25
        reasons.append("Repeated bonus claims")

    if low_deposit_high_bonus(player):
        score += 20
        reasons.append("Low deposit with high bonus usage")

    if fast_withdrawal_pattern(player):
        score += 20
        reasons.append("Fast withdrawal pattern")

    if short_risky_session(player):
        score += 15
        reasons.append("Short risky session")

    if duplicate_ip(players, player):
        score += 10
        reasons.append("Duplicate IP address")

    if duplicate_device(players, player):
        score += 10
        reasons.append("Duplicate device ID")

    if score >= 60:
        risk_level = "High"
    elif score >= 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "player_id": player.player_id,
        "risk_score": score,
        "risk_level": risk_level,
        "reasons": ", ".join(reasons) if reasons else "No suspicious activity"
    }


def analyze_players(players):
    return [calculate_risk_score(players, player) for player in players]
