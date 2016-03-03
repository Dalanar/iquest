__author__ = 'Stepan'


import calendar
import datetime


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
        [5, 1], [5, 2], [5, 3], [5, 9],
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


def fill_calendar(schedule, year, month, current_day, amount_days):
    '''
    Заполняем расписание днями
    '''
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


def get_shifted_date():
    '''
    Получаем дату отчета со двигом в два дня, т.к. если сегодня понедельник,
    а в субботу был праздник, то понедельник должен быть выходной
    '''
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


def create_schedule_obj(times):
    obj = []
    arr_times = times.split()
    for time in arr_times:
        time_cost = time.split('=')
        if len(time_cost) != 2:
            continue
        obj.append({
            'time': time_cost[0].strip(),
            'cost': time_cost[1].strip()
        })
    return obj


def create_schedule_form_template(template, quests):
    '''
    Создает расписание для квестов с различными ценами
    '''
    schedule_arr = {}
    for quest in quests:
        try:
            schedule = quest.schedule
        except:
            continue
        if template == "weekday":
            schedule_arr[quest.id] = create_schedule_obj(schedule.weekday)
        elif template == "before_weekend":
            schedule_arr[quest.id] = \
                create_schedule_obj(schedule.weekday_before_weekend)
        elif template == "weekend":
            schedule_arr[quest.id] = \
                create_schedule_obj(schedule.weekend)
        else:
            schedule_arr[quest.id] = \
                create_schedule_obj(schedule.weekend_before_weekday)
    return schedule_arr


def add_times(quest_calendar, quests):
    '''
    Добавляем время с учетом следующего дня
    '''
    for i in range(len(quest_calendar) - 1):
        day = quest_calendar[i]
        next_day = quest_calendar[i + 1]
        if not day[3] and not next_day[3]:
            day_type = "weekday"
        elif not day[3] and next_day[3]:
            day_type = "before_weekend"
        elif day[3] and next_day[3]:
            day_type = "weekend"
        else:
            # elif day[3] and not next_day[3]:
            day_type = "weekend_before_weekday"
        quest_calendar[i].append(
            create_schedule_form_template(day_type, quests)
        )
    return quest_calendar


def change_bool_to_int(schedule):
    for i in range(len(schedule)):
        schedule[i][3] = int(schedule[i][3])
    return schedule


def get_schedule(quests):
    '''
    Генерация расписания
    Берем 34 дня, но возвращаем 30, чтобы на грницах расписания были
    правильные времена бронирования и цены
    '''
    shifted = 2
    amount_days = 34
    [year, month, day] = get_shifted_date()
    quest_calendar = []
    [quest_calendar, amount_days] = \
        fill_calendar(
            quest_calendar,
            year,
            month,
            day,
            amount_days
        )
    while amount_days > 0:
        [year, month] = \
            increment_month(year, month)
        [quest_calendar, amount_days] = \
            fill_calendar(
                quest_calendar,
                year,
                month,
                1,
                amount_days
            )
    quest_calendar = set_holidays(quest_calendar)
    schedule = add_times(quest_calendar, quests)
    schedule = change_bool_to_int(schedule)
    return schedule[shifted:32]


def check_time_in_schedule(date, time, cost, quest_id, quests):
    schedule = get_schedule(quests)
    order_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    for schedule_date in schedule:
        if schedule_date[0] == order_date.year and \
                schedule_date[1] == order_date.month and \
                schedule_date[2] == order_date.day:
            for key in schedule_date[4][quest_id]:
                if key["time"] == time and \
                    key["cost"] == str(cost):
                    return True
    return False