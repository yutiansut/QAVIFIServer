

import pymongo

coll = pymongo.MongoClient().quantaxis.indicator_plot
buy_icon = '\ue616'
sell_icon = '\ue618'


class QAIndicatorPlot_AREA():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, start, end):
        self.data.append({
            'type': 'area',
            'id': self.uniid,
            'Date': end,
            "code": self.code,
            'data': [
                {
                    'Start': {'Date': start, 'Time': None},
                    'End': {'Date': end, 'Time': None},
                    'Color': 'rgba(250,128,144,0.5)'
                }
            ]
        })

    def to_json(self):
        return self.data

    def save(self):
        coll.insert_many(self.data)


class QAIndicatorPlot_DOT():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, time, price, icon, color='rgb(0,0,0)'):
        self.data.append({
            'type': 'dot',
            'id': self.uniid,
            'Date': time,
            "code": self.code,
            'data': [
                {
                    'Date': time,
                    'Value': price,
                    'Symbol': sell_icon,
                    'Color': color,
                    'Baseline': 0}
            ]
        })

    def to_json(self):
        return self.data

    def save(self):
        coll.insert_many(self.data)


class QAIndicatorPlot_PLOYGON():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, array=[
        {'Date': 20200327, 'Value': 16.0},
        {'Date': 20200416, 'Value': 16.0},
        {'Date': 20200416, 'Value': 14.0},
        {'Date': 20200327, 'Value': 14.0}
    ], color='rgb(0,0,0)', bgcolor='rgba(255,0,0,0.5)'):
        self.data.append({
            'type': 'polygon',
            'id': self.uniid,
            'Date': array[-1]['Date'],
            "code": self.code,
            'data': [
                # 例如：矩型
                {
                    'Color': color,
                    'BGColor': bgcolor,
                    'Point': array
                },
            ]
        })

    def to_json(self):
        return self.data

    def save(self):
        coll.insert_many(self.data)


class QAIndicatorPlot_LINE():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, array=[
        {'Date': 20200327, 'Value': 16.0},
        {'Date': 20200416, 'Value': 16.0},
        {'Date': 20200416, 'Value': 14.0},
        {'Date': 20200327, 'Value': 14.0}
    ], color='rgb(0,0,0)', bgcolor='rgba(255,0,0,0.5)'):
        self.data.append({
            'type': 'line',
            'id': self.uniid,
            'Date': array[-1]['Date'],
            "code": self.code,
            'data': [
                {
                    'Color': color,  # 直线颜色
                    # 一条直线这一项可不写
                    'BGColor': bgcolor,
                    'Point': array
                },
            ]})

    def to_json(self):
        return self.data

    def save(self):
        coll.insert_many(self.data)
