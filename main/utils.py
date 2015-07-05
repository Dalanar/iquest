__author__ = 'Stepan'

import re


def phone_validate(phone):
    phone = re.sub(r'[^\d]', '', phone)
    if len(phone) > 0:
        if phone[0] == "8":
            return "7" + phone[1:]
        elif phone[0] == "9":
            return "7" + phone
        else:
            return phone
    return ""