__author__ = 'Stepan'


from main.schedule.costs import *

# понедельник, вторник, среда, четверг
hospital_weekday = {
    0: {
        "time": "10:30",
        "cost": low_cost,
    },
    1: {
        "time": "12:30",
        "cost": low_cost,
        "order": 1
    },
    2: {
        "time": "14:30",
        "cost": low_cost,
        "order": 2
    },
    3: {
        "time": "16:30",
        "cost": middle_cost,
        "order": 3
    },
    4: {
        "time": "18:30",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "20:30",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "22:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "00:30",
        "cost": high_cost,
        "order": 7
    }
}


# before_weekend = {
#     # пятница, день перед выходным
#     0: {
#         "time": "12:00",
#         "cost": low_cost,
#     },
#     1: {
#         "time": "13:15",
#         "cost": low_cost,
#         "order": 1
#     },
#     2: {
#         "time": "14:30",
#         "cost": low_cost,
#         "order": 2
#     },
#     3: {
#         "time": "15:45",
#         "cost": middle_cost,
#         "order": 3
#     },
#     4: {
#         "time": "17:00",
#         "cost": middle_cost,
#         "order": 4
#     },
#     5: {
#         "time": "18:15",
#         "cost": high_cost,
#         "order": 5
#     },
#     6: {
#         "time": "19:30",
#         "cost": high_cost,
#         "order": 6
#     },
#     7: {
#         "time": "20:45",
#         "cost": high_cost,
#         "order": 7
#     },
#     8: {
#         "time": "22:00",
#         "cost": high_cost,
#         "order": 8
#     },
#     9: {
#         "time": "23:15",
#         "cost": high_cost,
#         "order": 9
#     },
#     10: {
#         "time": "0:30",
#         "cost": high_cost,
#         "order": 10
#     }
# }


# суббота или выходной, после которого выходной
hospital_weekend = {
    0: {
        "time": "10:30",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "12:30",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "14:30",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "16:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "18:30",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "20:30",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "22:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "00:30",
        "cost": high_cost,
        "order": 7
    }
}


# # воскресенье или выходной после которого рабочий день
# weekend_before_weekday = {
#     0: {
#         "time": "10:45",
#         "cost": middle_cost,
#         "order": 0
#     },
#     1: {
#         "time": "12:00",
#         "cost": middle_cost,
#         "order": 1
#     },
#     2: {
#         "time": "13:15",
#         "cost": high_cost,
#         "order": 2
#     },
#     3: {
#         "time": "14:30",
#         "cost": high_cost,
#         "order": 3
#     },
#     4: {
#         "time": "15:45",
#         "cost": high_cost,
#         "order": 4
#     },
#     5: {
#         "time": "17:00",
#         "cost": high_cost,
#         "order": 5
#     },
#     6: {
#         "time": "18:15",
#         "cost": high_cost,
#         "order": 6
#     },
#     7: {
#         "time": "19:30",
#         "cost": high_cost,
#         "order": 7
#     },
#     8: {
#         "time": "20:45",
#         "cost": high_cost,
#         "order": 8
#     },
#     9: {
#         "time": "22:00",
#         "cost": high_cost,
#         "order": 9
#     },
#     10: {
#         "time": "23:15",
#         "cost": high_cost,
#         "order": 10
#     },
#     11: {
#         "time": "0:30",
#         "cost": high_cost,
#         "order": 11
#     }
# }