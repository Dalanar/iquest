__author__ = 'Stepan'


from main.schedule.costs import *

zombie_weekday = {
    0: {
        "time": "10:00",
        "cost": low_cost,
    },
    1: {
        "time": "12:00",
        "cost": low_cost,
        "order": 1
    },
    2: {
        "time": "14:00",
        "cost": low_cost,
        "order": 2
    },
    3: {
        "time": "16:00",
        "cost": middle_cost,
        "order": 3
    },
    4: {
        "time": "18:00",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "20:00",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "22:00",
        "cost": high_cost,
        "order": 6
    }
}

zombie_weekend = {
    0: {
        "time": "10:00",
        "cost": middle_cost,
        "order": 0
    },
    1: {
        "time": "12:00",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "14:00",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "16:00",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "18:00",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "20:00",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "22:00",
        "cost": high_cost,
        "order": 6
    }
}