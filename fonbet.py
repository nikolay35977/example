import requests
import json
import csv

#html asks
def get_request(url,headers):
    session = requests.session()
    request = session.get(url, headers=headers)
    return request

#write csv
def write_csv(data):
    with open('fonbet.XLS', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name_of_match'],
                         data['w1'],
                         data['draw'],
                         data['w2'],
                         data['w1x'],
                         data['w12'],
                         data['w2x'],
                         data['total'],
                         data['s_total'],
                         data['fora'],
                         data['s_fora1'],
                         data['s_fora2'],
                         ))

def main():
    url = 'https://line51.bkfon-resource.ru/line/topEvents3?place=line&sysId=1&lang=ru&salt=vqfimyf6mfk232rcwh'
    url2 = 'https://line36a.bkfon-resource.ru/line/topEvents3?place=live&sysId=1&lang=ru&salt=dz9mtw3i8vsk232rf7s'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    result = get_request(url,headers)
    json_string = result.json()
    s1 = json.dumps(json_string)
    d2 = json.loads(s1)
    for i in d2['events']:
        try: #Name of match
            name_of_match = i['markets'][0]['rows'][1]['cells'][1]['cartEventName']
            #name_of_match = i['eventName']
        except:
            name_of_match = i['markets'][0]['rows'][0]['cells'][1]['cartEventName']
            #name_of_match = i['eventName']

        try: #1
            w1 = i['markets'][0]['rows'][1]['cells'][1]['value']
        except:
            w1 = None

        try: #X
            draw = i['markets'][0]['rows'][1]['cells'][2]['value']
        except:
            draw = None

        try:  #2
            w2 = i['markets'][0]['rows'][1]['cells'][3]['value']
        except:
            w2 = None

        try:  #1X
            w1x = i['markets'][1]['rows'][0]['cells'][1]['value']
        except:
            w1x = None

        try:  #12
            w12 = i['markets'][1]['rows'][0]['cells'][2]['value']
        except:
            w12 = None

        try:  #2X
            w2x = i['markets'][1]['rows'][0]['cells'][3]['value']
        except:
            w2x = None

        try:  #totalB
            s_total = i['markets'][1]['rows'][0]['cells'][3]['value']
        except:
            s_total = None

        try: #total
            total = i['markets'][2]['rows'][0]['cells'][1]['paramText']
        except:
            total = None

        try:  #fora1
            s_fora1 = i['markets'][3]['rows'][0]['cells'][1]['value']
        except:
            try:
                s_fora1 = i['markets'][2]['rows'][0]['cells'][0]['value']
            except:
                s_fora1 = None

        try: #fora
            fora = i['markets'][3]['rows'][0]['cells'][1]['paramText']
        except:
            try:
                fora = i['markets'][2]['rows'][0]['cells'][0]['paramText']
            except:
                fora = None
        try:  #fora2
            s_fora2 = i['markets'][3]['rows'][0]['cells'][1]['value']
        except:
            try:
                s_fora2 = i['markets'][2]['rows'][0]['cells'][0]['value']
            except:
                s_fora2 = None
        data = {
            'name_of_match':name_of_match,
            'w1': w1,
            'draw': draw,
            'w2': w2,
            'w1x': w1x,
            'w12': w12,
            'w2x':w2x,
            'total':total,
            's_total':s_total,
            'fora':fora,
            's_fora1':s_fora1,
            's_fora2':s_fora2}
        write_csv(data)


if __name__ == '__main__':
    main()
