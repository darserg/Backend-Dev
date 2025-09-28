def get_competition_data(data):
    teams = set()  # Используем множество, чтобы избежать дубликатов

    for race in data:
        for team in race.keys():
            teams.add(team)

    sorted_teams = sorted(teams)  # Сортируем по алфавиту
    print("Команды, участвовавшие в гонке:", ", ".join(sorted_teams))


races_data = [
    {"Ferrari": 20, "Mercedes": 5, "Aston Martin": 10, "Williams": 15},
    {"Mercedes": 15, "Aston Martin": 20, "Ferrari": 10, "Williams": 0},
    {"Ferrari": 20, "Williams": 15, "Aston Martin": 10, "Mercedes": 5},
]

get_competition_data(races_data)
