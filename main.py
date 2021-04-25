import json

from matplotlib import pyplot as plt


def get_data():
    _rules = []

    with open('config.json') as json_file:
        data = json.load(json_file)

        for rule in data['rules']:
            _rules.append({
                'conditions': rule['conditions'],
                'conclusion': rule['conclusion']
            })

    return _rules


def attendance_membership(x_value):
    # 0-30 20-50 40-70 60-90 80-100
    result = []
    if x_value <= 30:
        value = (30 - x_value) / 30
        result.append({
            'term': 'rare',
            'membership': round(value, 2)
        })

    if 20 <= x_value <= 50:
        if x_value <= 35:
            value = (x_value - 20) / 15
        else:
            value = (50 - x_value) / 15
        result.append({
            'term': 'inconsistent',
            'membership': round(value, 2)
        })
    if 40 <= x_value <= 70:
        if x_value < 55:
            value = (x_value - 40) / 15
        else:
            value = (70 - x_value) / 15
        result.append({
            'term': 'usual',
            'membership': round(value, 2)
        })
    if 60 <= x_value <= 90:
        if x_value < 75:
            value = (x_value - 60) / 15
        else:
            value = (90 - x_value) / 15
        result.append({
            'term': 'regular',
            'membership': round(value, 2)
        })
    if x_value >= 80:
        value = (x_value - 80) / 20
        result.append({
            'term': 'constant',
            'membership': round(value, 2)
        })

    return result


def grades_membership(x_value):
    # 0-20 10-50 40-80 70-90 85-100
    result = []
    if x_value <= 20:
        value = (20 - x_value) / 20
        result.append({
            'term': 'terrible',
            'membership': round(value, 2)
        })
    if 10 <= x_value <= 50:
        if x_value <= 30:
            value = (x_value - 10) / 20
        else:
            value = (50 - x_value) / 20
        result.append({
            'term': 'bad',
            'membership': round(value, 2)
        })
    if 40 <= x_value <= 80:
        if x_value <= 60:
            value = (x_value - 40) / 20
        else:
            value = (80 - x_value) / 20
        result.append({
            'term': 'average',
            'membership': round(value, 2)
        })
    if 70 <= x_value <= 90:
        if x_value <= 80:
            value = (x_value - 70) / 10
        else:
            value = (90 - x_value) / 10
        result.append({
            'term': 'good',
            'membership': round(value, 2)
        })
    if x_value >= 85:
        value = (x_value - 85) / 15
        result.append({
            'term': 'excellent',
            'membership': round(value, 2)
        })

    return result


def performance_membership(x_value):
    # 0-20 10-50 40-80 70-90 85-100
    result = []
    if x_value <= 20:
        value = (20 - x_value) / 20
        result.append({
            'term': 'terrible',
            'membership': round(value, 2)
        })
    if 10 <= x_value <= 40:
        if x_value <= 25:
            value = (x_value - 10) / 15
        else:
            value = (40 - x_value) / 15
        result.append({
            'term': 'poor',
            'membership': round(value, 2)
        })
    if 30 <= x_value <= 70:
        if x_value <= 50:
            value = (x_value - 30) / 20
        else:
            value = (70 - x_value) / 20
        result.append({
            'term': 'mediocre',
            'membership': round(value, 2)
        })
    if 60 <= x_value <= 90:
        if x_value <= 75:
            value = (x_value - 60) / 15
        else:
            value = (90 - x_value) / 15
        result.append({
            'term': 'normal',
            'membership': round(value, 2)
        })
    if x_value >= 80:
        value = (x_value - 80) / 20
        result.append({
            'term': 'excellent',
            'membership': round(value, 2)
        })

    return result


def crisp_performance(term, score):
    print('Started calculating Crisp Value for inserted data...')
    if term == 'terrible':
        result = 20 - (20 * score)
        return result
    elif term == 'poor':
        result_1 = 10 + (15 * score)
        result_2 = 40 - (15 * score)
        return (result_1 + result_2) / 2
    elif term == 'mediocre':
        result_1 = 30 + (20 * score)
        result_2 = 70 - (25 * score)
        return (result_1 + result_2) / 2
    elif term == 'normal':
        result_1 = 60 + (15 * score)
        result_2 = 90 - (15 * score)
        return (result_1 + result_2) / 2
    elif term == 'excellent':
        result = 80 + (20 * score)
        return result


def crisp_conclusion(score):
    result = performance_membership(score)
    print('> After using all the rules obtained for the research, the following is obtained:')
    print('Crisp Score: {0}'.format(score))
    for i, conclusion in enumerate(result):
        print('Crisp Term #{0}: {1} with {2} accuracy'.format(i + 1, conclusion['term'], conclusion['membership']))


def build_semantic_graphs():
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(10)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    fig.suptitle('Семантические графики термов')

    attendance_semantics = {
        'rare': {'x': [], 'y': [], 'color': 'purple'},
        'inconsistent': {'x': [], 'y': [], 'color': 'red'},
        'usual': {'x': [], 'y': [], 'color': 'orange'},
        'regular': {'x': [], 'y': [], 'color': 'blue'},
        'constant': {'x': [], 'y': [], 'color': 'green'},
    }
    _x = 0

    while _x <= 100:
        x = attendance_membership(_x)
        for term in x:
            attendance_semantics[term['term']]['x'].append(_x)
            attendance_semantics[term['term']]['y'].append(round(term['membership'] * 100, 2))
            # print('{0}: {1} - {2}'.format(_x, term['term'], round(term['membership'] * 100, 0)))
        _x = _x + 1

    for key, value in attendance_semantics.items():
        ax1.plot(value['x'], value['y'], '-p', color=value['color'])

    grades_semantics = {
        'terrible': {'x': [], 'y': [], 'color': 'purple'},
        'bad': {'x': [], 'y': [], 'color': 'red'},
        'average': {'x': [], 'y': [], 'color': 'orange'},
        'good': {'x': [], 'y': [], 'color': 'blue'},
        'excellent': {'x': [], 'y': [], 'color': 'green'},
    }
    _x = 0

    while _x <= 100:
        x = grades_membership(_x)
        for term in x:
            grades_semantics[term['term']]['x'].append(_x)
            grades_semantics[term['term']]['y'].append(round(term['membership'] * 100, 2))
            # print('{0}: {1} - {2}'.format(_x, term['term'], round(term['membership'] * 100, 0)))
        _x = _x + 1

    for key, value in grades_semantics.items():
        ax2.plot(value['x'], value['y'], '-p', color=value['color'])

    performance_semantics = {
        'terrible': {'x': [], 'y': [], 'color': 'purple'},
        'poor': {'x': [], 'y': [], 'color': 'red'},
        'mediocre': {'x': [], 'y': [], 'color': 'orange'},
        'normal': {'x': [], 'y': [], 'color': 'blue'},
        'excellent': {'x': [], 'y': [], 'color': 'green'},
    }
    _x = 0

    while _x <= 100:
        x = performance_membership(_x)
        for term in x:
            performance_semantics[term['term']]['x'].append(_x)
            performance_semantics[term['term']]['y'].append(round(term['membership'] * 100, 2))
            # print('{0}: {1} - {2}'.format(_x, term['term'], round(term['membership'] * 100, 0)))
        _x = _x + 1

    for key, value in performance_semantics.items():
        ax3.plot(value['x'], value['y'], '-p', color=value['color'])

    ax1.legend(["Rare", "Inconsistent", "Usual", "Regular", "Constant"])
    ax2.legend(["Terrible", "Bad", "Average", "Good", "Excellent"])
    ax3.legend(["Terrible", "Poor", "Mediocre", "Normal", "Excellent"])
    return fig


def input_evaluation_mamdani(_input_attendance, _input_grades):
    a_membership = attendance_membership(_input_attendance)
    g_membership = grades_membership(_input_grades)
    print('> Membership for input values are: \n{0}\n{1}'.format(a_membership, g_membership))

    all_memberships = a_membership + g_membership

    print('> After assumption evaluation {0} MF(s) remain: \n{1}'.format(len(all_memberships), all_memberships))

    results = []
    if len(a_membership) == 2:
        if len(g_membership) == 2:
            print('Creating 4 new Rules from 4 MFs...')
            results.append({'result': min(a_membership[0]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[0]['term']})
            results.append({'result': min(a_membership[0]['membership'], g_membership[1]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[1]['term']})
            results.append({'result': min(a_membership[1]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[1]['term'],
                            'second_term': g_membership[0]['term']})
            results.append({'result': min(a_membership[1]['membership'], g_membership[1]['membership']),
                            'first_term': a_membership[1]['term'],
                            'second_term': g_membership[1]['term']})
        elif len(g_membership) == 1:
            print('Creating 2 new Rules from 3 MFs...')
            results.append({'result': min(a_membership[0]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[0]['term']})
            results.append({'result': min(a_membership[1]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[1]['term'],
                            'second_term': g_membership[0]['term']})
    elif len(a_membership) == 1:
        if len(g_membership) == 2:
            print('Creating 2 new Rules from 3 MFs...')
            results.append({'result': min(a_membership[0]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[0]['term']})
            results.append({'result': min(a_membership[0]['membership'], g_membership[1]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[1]['term']})
        elif len(g_membership) == 1:
            print('Creating 1 new Rules from 2 MFs...')
            results.append({'result': min(a_membership[0]['membership'], g_membership[0]['membership']),
                            'first_term': a_membership[0]['term'],
                            'second_term': g_membership[0]['term']})

    print('> After defuzzification {0} Rules remain: \n{1}'.format(len(results), results))
    result = max(list(map(lambda x: x['result'], results)))

    resulting_rule = next(item for item in results if item["result"] == result)
    print(
        '> Further defuzzification according to new Rules confirms next Rule most powerful: \n{0}'.format(
            resulting_rule))
    # print(performance_membership(resulting_rule['result'] * 100))
    print('Checking already accumulated Rules from JSON...')
    rules = get_data()
    power_rule = next(
        item for item in rules if item["conditions"] == [resulting_rule['first_term'], resulting_rule['second_term']])

    print(
        '> Found Accumulated Rule(s) matching requested parameters: \nInitial Rule: {0}\nAccumulated Rule: {1}'.format(
            resulting_rule, power_rule))
    print('> Calculations resulted PERFORMANCE term "{0}" with {1} evaluation score. '.format(power_rule['conclusion'],
                                                                                              resulting_rule['result']))

    return power_rule['conclusion'], resulting_rule['result']


def input_evaluation_sugeno(_input_attendance, _input_grades):
    pass


if __name__ == '__main__':
    plt = build_semantic_graphs()
    plt.show()

    print('Enter attendance score (0-100):')
    input_attendance = input()

    print('Enter grades score (0-100):')
    input_grades = input()

    conclusion_term, evaluated_score = input_evaluation_mamdani(float(input_attendance), float(input_grades))
    crisp_conclusion(crisp_performance(conclusion_term, evaluated_score))
