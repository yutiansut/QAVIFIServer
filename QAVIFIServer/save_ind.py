

import pymongo

from webcolors import name_to_hex

coll = pymongo.MongoClient().quantaxis.indicator_plot

buy_icon = "buy"
sell_icon = "sell"


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
        try:
            coll.insert_many(self.data, ordered=False)
        except:
            pass


class QAIndicatorPlot_DOT():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, time, price, icon, color='rgb(0,0,0)'):

        if color.startswith('rgb') or color.startswith('#'):
            pass
        else:
            try:
                color = name_to_hex(color)
            except:
                color =  'rgb(0,0,0)'
        self.data.append({
            'type': 'dot',
            'id': self.uniid,
            'Date': time,
            "code": self.code,
            'data': [
                {
                    'Date': time,
                    'Value': price,
                    'Symbol': icon,
                    'Color': color,
                    'Baseline': 0}
            ]
        })

    def to_json(self):
        return self.data

    def save(self):
        try:
            coll.insert_many(self.data, ordered=False)
        except:
            pass


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
        try:
            coll.insert_many(self.data, ordered=False)
        except:
            pass


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
        try:
            coll.insert_many(self.data, ordered=False)
        except:
            pass


if __name__ == "__main__":
    # area1 = QAIndicatorPlot_AREA('000002', 'ax2')
    # area1.add_datapoint(20200202, 20200302)
    # area1.add_datapoint(20200322, 20200328)
    # area1.save()

    # line1 = QAIndicatorPlot_LINE('000002', 'ax2')
    # line1.add_datapoint(array=[{'Date': 20200220, 'Value': 10}, {
    #                     'Date': 20200320, 'Value': 20}])
    # line1.save()

    # ploy1 = QAIndicatorPlot_PLOYGON('000002', 'ax2')
    # ploy1.add_datapoint(array=[
    #     {'Date': 20191227, 'Value': 16.0},
    #     {'Date': 20200116, 'Value': 16.0},
    #     {'Date': 20200116, 'Value': 14.0},
    #     {'Date': 20191227, 'Value': 14.0}],
    #     bgcolor='rgba(255,255,0,0.5)')
    # ploy1.save()

    dot1 = QAIndicatorPlot_DOT('000002', 'ax2')
    dot1.add_datapoint(20200325, 30, 'buy', 'blue')
    dot1.save()