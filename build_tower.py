def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        tower.append(("*" * (i * 2 + 1)).center(n_floors * 2 - 1))
    return tower
