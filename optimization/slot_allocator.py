def recommend_slot(occupancy):
    for index, slot in enumerate(occupancy):
        if slot == 0:
            return index + 1
    return None
