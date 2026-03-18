request_count = {}

def check_limit(user):
    if user not in request_count:
        request_count[user] = 1
    else:
        request_count[user] += 1

    if request_count[user] > 5:
        return False
    return True