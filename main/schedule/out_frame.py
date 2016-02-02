__author__ = 'Stepan'

from main.schedule.costs import *

out_frame_weekday = {
    0: {
        "time": "15:00",
        "cost": middle_cost,
    },
    1: {
        "time": "16:30",
        "cost": middle_cost,
        "order": 1
    },
    2: {
        "time": "18:00",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "19:30",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "21:00",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "22:30",
        "cost": high_cost,
        "order": 5
    }
}

out_frame_weekend = {
    0: {
        "time": "11:30",
        "cost": high_cost,
        "order": 0
    },
    1: {
        "time": "13:00",
        "cost": high_cost,
        "order": 1
    },
    2: {
        "time": "14:30",
        "cost": high_cost,
        "order": 2
    },
    3: {
        "time": "16:00",
        "cost": high_cost,
        "order": 3
    },
    4: {
        "time": "17:30",
        "cost": high_cost,
        "order": 4
    },
    5: {
        "time": "19:00",
        "cost": high_cost,
        "order": 5
    },
    6: {
        "time": "20:30",
        "cost": high_cost,
        "order": 6
    },
    7: {
        "time": "22:00",
        "cost": high_cost,
        "order": 7
    },
    8: {
        "time": "22:30",
        "cost": high_cost,
        "order": 8
    }
}