__author__ = 'Stepan'

low_cost = 1500
middle_cost = 2000
high_cost = 2500

schedule = [
    {
        # понедельник
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
    },
    {
        # вторник
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
    },
    {
        # среда
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
    },
    {
        # четверг
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
    },
    {
        # пятница
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
        },
        11: {
            "time": "1:45",
            "cost": middle_cost,
            "order": 11
        }
    },
    {
        # суббота
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
        },
        12: {
            "time": "1:45",
            "cost": middle_cost,
            "order": 12
        }
    },
    {
        # воскресенье
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
        },
    }
]