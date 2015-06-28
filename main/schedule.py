__author__ = 'Stepan'


import calendar
import datetime

from copy import deepcopy

costs = {
    "quest1": {
        "low_cost": 1500,
        "middle_cost": 2000,
        "high_cost": 2500
    },
    "quest2": {
        "low_cost": 2000,
        "middle_cost": 2500,
        "high_cost": 3000
    }
}

low_cost = "low_cost"
middle_cost = "middle_cost"
high_cost = "high_cost"


# понедельник, вторник, среда, четверг
weekday = {
    0: {
        "time": "12:00",
        "cost": low_cost,
    },
    1: {
        "time": "13:15",
        "cost": low_cost,
        "order": 1
    },
    2: {
        "time": "14:30",
        "cost": low_cost,
        "order": 2
    },
    3: {
        "time": "15:45",
        "cost": middle_cost,
        "order": 3
    },
    4: {
        "time": "17:00",
        "cost": middle_cost,
        "order": 4
    },
    5: {
        "time": "18:15",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "19:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "20:45",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:00",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "23:15",
        "cost": high_cost,
        "order": 9
    }
}


before_weekend = {
    # пятница, день перед выходным
    0: {
        "time": "12:00",
        "cost": low_cost,
    },
    1: {
        "time": "13:15",
        "cost": low_cost,
        "order": 1
    },
    2: {
        "time": "14:30",
        "cost": low_cost,
        "order": 2
    },
    3: {
        "time": "15:45",
        "cost": middle_cost,
        "order": 3
    },
    4: {
        "time": "17:00",
        "cost": middle_cost,
        "order": 4
    },
    5: {
        "time": "18:15",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "19:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "20:45",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:00",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "23:15",
        "cost": high_cost,
        "order": 9
    },
    10: {
        "time": "0:30",
        "cost": high_cost,
        "order": 10
    }
}


# суббота или выходной, после которого выходной
weekend = {
    0: {
        "time": "10:45",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "12:00",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "13:15",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "14:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "15:45",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "17:00",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "18:15",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "19:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "20:45",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "22:00",
        "cost": high_cost,
        "order": 9
    },
    10: {
        "time": "23:15",
        "cost": high_cost,
        "order": 10
    },
    11: {
        "time": "0:30",
        "cost": high_cost,
        "order": 11
    }
}


# воскресенье или выходной после которого рабочий день
weekend_before_weekday = {
    0: {
        "time": "10:45",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "12:00",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "13:15",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "14:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "15:45",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "17:00",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "18:15",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "19:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "20:45",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "22:00",
        "cost": high_cost,
        "order": 9
    },
    10: {
        "time": "23:15",
        "cost": high_cost,
        "order": 10
    },
    11: {
        "time": "0:30",
        "cost": high_cost,
        "order": 11
    }
}


def increment_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return [year, month]


def is_holiday(month, day):
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
    schedule.append(to_form_costs(template, "quest1"))
    schedule.append(to_form_costs(template, "quest2"))
    return schedule


# Добавляем время с учетом следующего дня
def add_times(schedule):
    for i in range(len(schedule) - 1):
        day = schedule[i]
        next_day = schedule[i + 1]
        if not day[3] and not next_day[3]:
            schedule[i].append(create_schedule_form_template(weekday))
        elif not day[3] and next_day[3]:
            schedule[i].append(create_schedule_form_template(before_weekend))
        elif day[3] and next_day[3]:
            schedule[i].append(create_schedule_form_template(weekend))
        elif day[3] and not next_day[3]:
            schedule[i].append(create_schedule_form_template(weekend_before_weekday))
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
    return schedule[shifted:32]