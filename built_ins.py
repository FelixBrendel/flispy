

def plus(env, *params):
    params = eval_params(env, params)
    result = 0
    for param in params:
        assert_number(param)
        result += param
    return result

def minus(env, *params):
    params = eval_params(env, params)

    if (len(params) == 0):
        return 0

    assert_number(params[0])

    if (len(params) == 1):
        return -params[0]

    result = params[0]
    for param in params[1:]:
        assert_number(param)
        result -= param
    return result

built_ins = {
    "+" : plus,
    "-" : minus,
}
