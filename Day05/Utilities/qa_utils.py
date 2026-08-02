def validate_status_code(actual, expected):
    return actual == expected


def validate_transaction(actual, expected):
    return actual == expected

def validate_response_time(actual, max_time):
    if actual<=max_time:
        return "PASS"
    else:
        return "FAIL"