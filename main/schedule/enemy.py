__author__ = 'Stepan'

from main.schedule.costs import *


enemy_weekday = {
    0: {
        "time": "14:30",
        "cost": low_cost,
        "order": 3
    },
    1: {
        "time": "16:00",
        "cost": middle_cost,
        "order": 4
    },
    2: {
        "time": "17:30",
        "cost": middle_cost,
        "order": 5
    },
    3: {
        "time": "19:00",
        "cost": middle_cost,
        "order": 6
    },
    4: {
        "time": "20:30",
        "cost": middle_cost,
        "order": 7
    },
    5: {
        "time": "22:00",
        "cost": middle_cost,
        "order": 7
    }
}

enemy_weekend = {
    0: {
        "time": "11:00",
        "cost": high_cost,
        "order": 0
    },
    1: {
        "time": "12:30",
        "cost": high_cost,
        "order": 1
    },
    2: {
        "time": "14:00",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "15:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "17:00",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "18:30",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "20:00",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "21:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "23:00",
        "cost": high_cost,
        "order": 8
    }
}