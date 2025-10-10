class Employee:
    vacation_days = 28

    def __generate_employee_id(self, conc):
        # Приватный метод для генерации ID
        return hash(conc)

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

        # Защищённый атрибут (одно подчёркивание)
        conc = f"{first_name}{second_name}{gender}"
        self._employee_id = self.__generate_employee_id(conc)

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender, salary):
        super().__init__(first_name, second_name, gender)
        # Приватный атрибут (два подчёркивания)
        self.__salary = salary

    def __get_vacation_salary(self):
        # Приватный метод для расчёта отпускных
        return self.__salary * 0.8

    def get_vacation_details(self):
        # Демонстрация работы с приватными атрибутами и методами
        vacation_pay = self.__get_vacation_salary()
        return (
            f"Остаток отпускных дней: {self.remaining_vacation_days}. "
            f"Отпускные: {vacation_pay:.2f}"
        )

    def get_unpaid_vacation(self, start_date, days):
        return f"Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней."


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# Пример использования:
full_time_employee = FullTimeEmployee("Иван", "Иванов", "м", 50000)
print(f"ID сотрудника (защищённый атрибут): {full_time_employee._employee_id}")
print(full_time_employee.get_unpaid_vacation("2023-07-01", 5))
print(full_time_employee.get_vacation_details())

# Попытка доступа к приватным атрибутам (вызовет ошибку)
# print(full_time_employee.__salary)  # AttributeError
# print(full_time_employee.__get_vacation_salary())  # AttributeError

part_time_employee = PartTimeEmployee("Анна", "Петрова", "ж")
print(f"ID сотрудника (защищённый атрибут): {part_time_employee._employee_id}")
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
