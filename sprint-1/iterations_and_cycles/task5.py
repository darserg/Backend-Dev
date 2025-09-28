def get_competition_data(data):
    teams = set()
    scores = {}  # Словарь для накопления общего счёта по командам

    # Собираем команды и суммируем баллы
    for race in data:
        for team, score in race.items():
            teams.add(team)

            # Инициализируем счёт команды, если ещё не было
            if team not in scores:
                scores[team] = 0
            scores[team] += score

    # Выводим список команд в алфавитном порядке
    sorted_teams = sorted(teams)
    print("Команды, участвовавшие в гонке:", ", ".join(sorted_teams))

    # Определяем победителя
    winner_team = None
    winner_score = 0

    for team, total_score in scores.items():
        if total_score > winner_score:
            winner_score = total_score
            winner_team = team

    # Выводим победителя
    print(f"В гонке победила команда {winner_team} с результатом {winner_score} баллов")


# Данные о результатах заездов
races_data = [
    {"Ferrari": 20, "Mercedes": 5, "Aston Martin": 10, "Williams": 15},
    {"Mercedes": 15, "Aston Martin": 20, "Ferrari": 10, "Williams": 0},
    {"Ferrari": 20, "Williams": 15, "Aston Martin": 10, "Mercedes": 5},
]

# Вызов функции
get_competition_data(races_data)
