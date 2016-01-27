__author__ = 'Stepan'


import calendar
import datetime

from copy import deepcopy
from main.schedule.hospital import *
from main.schedule.zombie import *
from main.schedule.enemy import *
from main.schedule.genius import *


def increment_month(year, month):
    """
    Функция для инкремента месяца, если месяц - декабрь,
    то инкремент года + месяц = 1
    """
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return [year, month]


def is_holiday(month, day):
    """
    Праздничный ли день
    """
    holidays = [
        [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8],
        [2, 23],
        [3, 8],
        [5, 1], [5, 9],
        [6, 12],
        [11, 4]
    ]
    for date in holidays:
        if date[0] == month and date[1] == day:
            return True
    return False


def is_weekend(year, month, day):
    """
    Является ли день выходным
    """
    weekends = [5, 6]
    date = datetime.datetime(year, month, day)
    if date.weekday() in weekends:
        return True
    return False


# Заполняем расписание
def fill_schedule(schedule, year, month, current_day, amount_days):
    days_in_month = calendar.monthrange(year, month)[1]
    for day in range(current_day, days_in_month + 1):
        amount_days -= 1
        schedule.append([
            year,
            month,
            day,
            is_weekend(year, month, day)
        ])
        if amount_days == 0:
            return [schedule, amount_days]
    return [schedule, amount_days]


# Устанавливаем праздники с переносом, если праздник выпал на выходной
def set_holidays(schedule):
    next_holiday = False
    january = 1
    for i in range(len(schedule)):
        date = schedule[i]
        if is_weekend(date[0], date[1], date[2]) and \
                is_holiday(date[1], date[2]) and \
                        date[1] != january:
            next_holiday = True
        elif is_holiday(date[1], date[2]):
            schedule[i][3] = True
        elif next_holiday and not is_weekend(date[0], date[1], date[2]):
            schedule[i][3] = True
            next_holiday = False
    return schedule


# Получаем дату со двигом в два дня, т.к. если сегодня понедельник, а в субботу
# был праздник, то понедельник должен быть выходной
def get_shifted_date():
    today = datetime.date.today()
    day = today.day
    month = today.month
    year = today.year
    if day > 3:
        return [year, month, day - 2]
    else:
        if month > 1:
            days_in_month = calendar.monthrange(year, month - 1)[1]
            return [year, month - 1, days_in_month + day - 2]
        else:
            month = 12
            year -= 1
            days_in_month = calendar.monthrange(year, month)[1]
            return [year, month, days_in_month]


# Заполняет шаблон расписания ценами для соответствующего квеста
def to_form_costs(template, quest):
    clone = deepcopy(template)
    for i in clone.keys():
        cost = clone[i]["cost"]
        clone[i]["cost"] = costs[quest][cost]
    return clone


# Создает расписание для двух квестов с различными ценами
def create_schedule_form_template(template):
    schedule = []
    if template == "weekday" or template == "before_weekend":
        schedule.append(to_form_costs(hospital_weekday, "quest1"))
        schedule.append(to_form_costs(zombie_weekday, "quest2"))
        schedule.append(to_form_costs(enemy_weekday, "quest3"))
        schedule.append(to_form_costs(genius_weekday, "quest4"))
    else:
        schedule.append(to_form_costs(hospital_weekend, "quest1"))
        schedule.append(to_form_costs(zombie_weekend, "quest2"))
        schedule.append(to_form_costs(enemy_weekend, "quest3"))
        schedule.append(to_form_costs(genius_weekend, "quest4"))
    return schedule


# Добавляем время с учетом следующего дня
def add_times(schedule):
    for i in range(len(schedule) - 1):
        day = schedule[i]
        next_day = schedule[i + 1]
        if not day[3] and not next_day[3]:
            schedule[i].append(create_schedule_form_template("weekday"))
        elif not day[3] and next_day[3]:
            schedule[i].append(create_schedule_form_template("before_weekend"))
        elif day[3] and next_day[3]:
            schedule[i].append(create_schedule_form_template("weekend"))
        elif day[3] and not next_day[3]:
            schedule[i].append(create_schedule_form_template("weekend_before_weekday"))
    return schedule


def change_bool_to_int(schedule):
    for i in range(len(schedule)):
        schedule[i][3] = int(schedule[i][3])
    return schedule


# Создаем расписание
def get_schedule():
    shifted = 2
    # Берем 34 дня, но возвращаем 30, чтобы на грницах расписания были
    # правильные времена бронирования и цены
    amount_days = 34
    [year, month, day] = get_shifted_date()
    schedule = []
    [schedule, amount_days] = \
        fill_schedule(
            schedule,
            year,
            month,
            day,
            amount_days
        )
    while amount_days > 0:
        [year, month] = \
            increment_month(year, month)
        [schedule, amount_days] = \
            fill_schedule(
                schedule,
                year,
                month,
                1,
                amount_days
            )
    schedule = set_holidays(schedule)
    schedule = add_times(schedule)
    schedule = change_bool_to_int(schedule)
    schedule = work_around_genius(schedule)
    return schedule[shifted:32]

def work_around_genius(schedule):
    for i in range(len(schedule)):
        if schedule[i][1] < 2:
            for j in range(len(schedule[i][4][3])):
                schedule[i][4][3][j]['cost'] = 1500

    return schedule