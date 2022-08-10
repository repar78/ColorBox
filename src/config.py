# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-08-09 10:07:32
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-08-10 20:27:49

import os
from pathlib import Path
import json

SETTING = {
    "actions": {
        "exit": ["enter", "return"],
        "maximize": ["up"],
        "minimize": ["Down"]
    },
    "window": {
        "background": "rgb(0, 0, 0)",
        "size": "500"
    },
    "analogClock": {
        "hourHand": {
            "color": "yellow",
            "width": 10,
            "size": 0.75
        },
        "minuteHand": {
            "color": "green",
            "width": 5,
            "size": 1
        },
        "secondHand": {
            "color": "red",
            "width": 1,
            "size": 1
        },
        "sign": {
            "color": "green",
            "size": 2
        }
    },
    "digitalClock": {
        "fontColor": "white",
        "fontSize": "20px"
    },
    "dateLabel": {
        "fontColor": "white",
        "fontSize": "15px"
    },
    "weekdayLabel": {
        "fontColor": "white",
        "fontSize": "15px"
    }
}

BASEDIR = Path(__file__).parent.parent

if os.path.exists(BASEDIR / "config/setting.json"):
    with open(BASEDIR / "config/setting.json") as jfile:
        SETTING.update(json.load(jfile))
