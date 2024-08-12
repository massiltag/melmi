from datetime import datetime, timedelta
from collections import defaultdict

def parse_time_ranges(time_ranges_str):
    time_ranges = time_ranges_str.split(',')
    parsed_ranges = []
    for time_range in time_ranges:
        parsed_ranges.append(datetime.strptime(time_range.strip(), '%Y-%m-%d'))
    return parsed_ranges

def find_best_time(availabilities):
    if not availabilities:
        return [], 0

    # Initialiser un dictionnaire pour compter les disponibilités pour chaque date
    time_slots = defaultdict(int)
    total_participants = len(availabilities)

    # Analyser toutes les plages de disponibilité
    for availability in availabilities:
        time_ranges = parse_time_ranges(availability.available_times)
        for date in time_ranges:
            time_slots[date] += 1

    # Sélectionner uniquement les dates où tous les participants sont disponibles
    best_times = [date for date, count in time_slots.items() if count == total_participants]

    # Retourner les dates où tous les participants sont disponibles
    best_time_slots = [(time, time) for time in best_times]

    return best_time_slots, total_participants
