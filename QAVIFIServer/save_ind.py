

import pymongo

from webcolors import name_to_rgb

coll = pymongo.MongoClient().quantaxis.indicator_plot

buy_icon = "buy"
sell_icon = "sell"


def convert_color(color, tran=1):
    """
    color =>color
    """

    if color.startswith('rgb') or color.startswith('#'):
        pass
    else:
        try:
            color = name_to_rgb(color)
        except:
            color = name_to_rgb('black')

        tran = 1 if abs(tran) >= 1 else abs(tran)
        color = "rgba({},{},{},{})".format(
            color.red, color.green, color.blue, tran)

    return color


class QAIndicatorPlot_AREA():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, start, end, color="rgba(250,128,144,0.5)"):
        self.data.append({
            'type': 'area',
            'id': self.uniid,
            'Date': end,
            "code": self.code,
            'data': [
                {
                    'Start': {'Date': start, 'Time': None},
                    'End': {'Date': end, 'Time': None},
                    'Color': convert_color(color)
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


class QAIndicatorPlot_TEXT():
    def __init__(self, code, uniid):
        self.code = code
        self.uniid = uniid
        self.data = []

    def add_datapoint(self, date, time, value, text, color="rgba(250,128,144,0.5)"):
        self.data.append({
            'type': 'text',
            'id': self.uniid,
            'Date': date,
            "code": self.code,
            'data': [
                {'Date': date, 'Time': time, 'Value': value,
                    'Text': text, 'Color': convert_color(color)}
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

        color = convert_color(color)
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
                    'Color': convert_color(color),
                    'BGColor': convert_color(bgcolor, 0.5),
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
                    'Color': convert_color(color),
                    'BGColor': convert_color(bgcolor, 0.5),
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
    area1 = QAIndicatorPlot_AREA('000001', 'ax3')
    area1.add_datapoint(20200202, 20200302, convert_color('green', 0.5))
    area1.add_datapoint(20200322, 20200328, convert_color('red', 0.5))
    area1.add_datapoint(20190812, 20190905, convert_color('yellow', 0.3))
    area1.save()

    line1 = QAIndicatorPlot_LINE('000001', 'ax3')
    line1.add_datapoint(array=[{'Date': 20190918, 'Value': 14.24}, {
                        'Date': 20191014, 'Value': 17.6}], color=convert_color('pink'))
    line1.save()

    ploy1 = QAIndicatorPlot_PLOYGON('000001', 'ax3')
    ploy1.add_datapoint(array=[
        {'Date': 20191227, 'Value': 16.0},
        {'Date': 20200116, 'Value': 16.0},
        {'Date': 20200116, 'Value': 14.0},
        {'Date': 20191227, 'Value': 14.0}],
        bgcolor=convert_color('pink', 0.5))
    ploy1.save()

    dot1 = QAIndicatorPlot_DOT('000001', 'ax3')
    dot1.add_datapoint(20200325, 30, 'buy', 'blue')
    dot1.save()
