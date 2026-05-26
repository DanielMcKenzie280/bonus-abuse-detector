def repeated_bonus_claims(player):
    return player.bonus_claims >= 5


def low_deposit_high_bonus(player):
    return player.deposits <= 1 and player.bonus_claims >= 4


def fast_withdrawal_pattern(player):
    return player.withdrawals >= 3 and player.total_bets <= 10


def short_risky_session(player):
    return player.session_minutes <= 30 and player.bonus_claims >= 4


def duplicate_ip(players, player):
    same_ip = [p for p in players if p.ip_address == player.ip_address]
    return len(same_ip) > 1


def duplicate_device(players, player):
    same_device = [p for p in players if p.device_id == player.device_id]
    return len(same_device) > 1
