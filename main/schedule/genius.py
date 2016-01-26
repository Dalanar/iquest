__author__ = 'Stepan'

from main.schedule.costs import *

genius_weekday = {
    0: {
        "time": "10:00",
        "cost": low_cost,
        "order": 3
    },
    1: {
        "time": "12:00",
        "cost": low_cost,
        "order": 4
    },
    2: {
        "time": "14:00",
        "cost": middle_cost,
        "order": 5
    },
    3: {
        "time": "16:00",
        "cost": middle_cost,
        "order": 6
    },
    4: {
        "time": "18:00",
        "cost": high_cost,
        "order": 7
    },
    5: {
        "time": "20:00",
        "cost": high_cost,
        "order": 7
    },
    6: {
        "time": "22:00",
        "cost": high_cost,
        "order": 7
    }
}

genius_weekend = {
    0: {
        "time": "10:00",
        "cost": middle_cost,
        "order": 3
    },
    1: {
        "time": "12:00",
        "cost": high_cost,
        "order": 4
    },
    2: {
        "time": "14:00",
        "cost": high_cost,
        "order": 5
    },
    3: {
        "time": "16:00",
        "cost": high_cost,
        "order": 6
    },
    4: {
        "time": "18:00",
        "cost": high_cost,
        "order": 7
    },
    5: {
        "time": "20:00",
        "cost": high_cost,
        "order": 7
    },
    6: {
        "time": "22:00",
        "cost": high_cost,
        "order": 7
    }
}