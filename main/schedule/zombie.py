__author__ = 'Stepan'


from main.schedule.costs import *

zombie_weekday = {
    0: {
        "time": "11:30",
        "cost": low_cost,
    },
    1: {
        "time": "12:50",
        "cost": low_cost,
        "order": 1
    },
    2: {
        "time": "14:10",
        "cost": low_cost,
        "order": 2
    },
    3: {
        "time": "15:30",
        "cost": middle_cost,
        "order": 3
    },
    4: {
        "time": "16:50",
        "cost": middle_cost,
        "order": 4
    },
    5: {
        "time": "18:10",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "19:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "20:50",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:10",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "23:30",
        "cost": high_cost,
        "order": 9
    }
}

zombie_weekend = {
    0: {
        "time": "10:10",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "11:30",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "12:50",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "14:10",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "15:30",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "16:50",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "18:10",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "19:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "20:50",
        "cost": high_cost,
        "order": 8
    },
    9: {
        "time": "22:10",
        "cost": high_cost,
        "order": 9
    },
    10: {
        "time": "23:30",
        "cost": high_cost,
        "order": 10
    }
}