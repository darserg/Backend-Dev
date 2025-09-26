# Пропишите нужные импорты.
from datetime import datetime, timedelta


# Напишите код функции, следуя плану из задания.
def get_results(leader_time_str, participant_time_str):
    leader_time = datetime.strptime(leader_time_str, "%H:%M:%S")
    participant_time = datetime.strptime(participant_time_str, "%H:%M:%S")
    delta_str = participant_time - leader_time

    if leader_time == participant_time:
        print("Вы пробежали за " + participant_time_str + " и победили!")
    else:
        print(
            "Вы пробежали за "
            + participant_time_str
            + " с отставанием от лидера "
            + str(delta_str)
        )


# Проверьте работу программы, можете подставить свои значения.
get_results("02:02:02", "02:02:02")
get_results("02:02:02", "03:04:05")
