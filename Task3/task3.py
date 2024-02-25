import json
import sys


def fill_report(values, r):
    if isinstance(values, str):
        with open(values, 'r') as f:
            values = json.load(f)
    for test in r:
        if 'values' in test:
            test['values'] = fill_report(values, test['values'])

        for i, item in enumerate(values['values']):
            if item['id'] == test['id']:
                test['value'] = values['values'][i]['value']
                break
    return r


def generate_report(values_path, tests_path, report_path):
    # чтение данных из файлов
    with open(values_path, 'r') as f:
        values = json.load(f)
    with open(tests_path, 'r') as f:
        tests = json.load(f)

    # заполнение данных в отчете
    r = tests.copy()
    r = r['tests']
    report = fill_report(values, r)

    # запись отчета в файл
    with open(report_path, 'w') as f:
        json.dump(report, f)

# values_path = 'values.json'
# tests_path = 'tests.json'
# report_path = 'report.json'


values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]
generate_report(values_path, tests_path, report_path)