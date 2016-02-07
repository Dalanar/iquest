__author__ = 'Stepan'

from main.schedule.costs import *

genius_weekday = {
    0: {
        "time": "10:00",
        "cost": low_cost,
        "order": 3
    },
    1: {
        "time": "11:30",
        "cost": low_cost,
        "order": 4
    },
    2: {
        "time": "13:00",
        "cost": middle_cost,
        "order": 5
    },
    3: {
        "time": "14:30",
        "cost": middle_cost,
        "order": 6
    },
    4: {
        "time": "16:00",
        "cost": middle_cost,
        "order": 7
    },
    5: {
        "time": "17:30",
        "cost": high_cost,
        "order": 7
    },
    6: {
        "time": "19:00",
        "cost": high_cost,
        "order": 7
    },
    7: {
        "time": "20:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:00",
        "cost": high_cost,
        "order": 8
    }
}

genius_weekend = {
    0: {
        "time": "10:00",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "11:30",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "13:00",
        "cost": middle_cost,
        "order": 2
    },
    3: {
        "time": "14:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "16:00",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "17:30",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "19:00",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "20:30",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:00",
        "cost": high_cost,
        "order": 8
    }
}