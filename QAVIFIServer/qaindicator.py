
"""
a python api for hqchart api
"""
from QAWebServer.basehandles import QABaseHandler
import QUANTAXIS as QA
import pandas as pd
import datetime
import pymongo

stocklist = QA.QA_fetch_stock_list_adv()

buy_icon = '\ue616'
sell_icon = '\ue618'


def plot_dot():

    return {
        'type': 'dot',
        'data': [
                {
                    'Date': 20200220,
                    'Value': 15.62,
                    'Symbol': sell_icon,
                    'Color': 'rgb(0,0,0)',
                    'Baseline': 0
                },
            {
                    'Date': 20200318,
                    'Value': 13.5,
                    'Symbol': buy_icon,
                    'Color': 'rgb(0,0,0)',
                    'Baseline': 0
            }
        ]
    }


def plot_area():
    return {
        'type': 'area',
        'data': [
            {
                'Start': {'Date': 20200220, 'Time': None},
                'End': {'Date': 20200318, 'Time': None},
                'Color': 'rgba(250,128,144,0.5)'
            }
        ]
    }


def plot_line():
    return {
        'type': 'line',
        'data': [
            {
                'Color': 'rgb(255,0,0)',  # 直线颜色
                # 一条直线这一项可不写
                'BGColor': 'rgba(255,0,0,0.5)',
                'Point': [
                    {'Date': 20200220, 'Value': 16.5},
                    {'Date': 20200318, 'Value': 13.5}
                ]
            },
            {
                'Color': 'rgb(255,0,0)',  # 直线颜色
                # 一条直线这一项可不写
                'BGColor': 'rgba(255,0,0,0.5)',
                'Point': [
                    {'Date': 20200220, 'Value': 13.5},
                    {'Date': 20200318, 'Value': 16.5}
                ]
            }
        ]
    }


def plot_polygon():
    return {
        # 至少三个点坐标
        'type': 'polygon',
        'data': [
                # 例如：矩型
                {
                    'Color': 'rgba(52,46,37,0)',
                    'BGColor': 'rgba(0,0,0,0.5)',
                    'Point': [
                        {'Date': 20200108, 'Value': 16.0},
                        {'Date': 20200213, 'Value': 16.0},
                        {'Date': 20200213, 'Value': 14.0},
                        {'Date': 20200108, 'Value': 14.0}
                    ]
                },
        ]
    }


def plot_polygon2():
    return {
        # 至少三个点坐标
        'type': 'polygon',
        'data': [
                # 例如：矩型
                {
                    'Color': 'rgba(52,46,37,0)',
                    'BGColor': 'rgba(255,0,0,0.5)',
                    'Point': [
                        {'Date': 20200327, 'Value': 16.0},
                        {'Date': 20200416, 'Value': 16.0},
                        {'Date': 20200416, 'Value': 14.0},
                        {'Date': 20200327, 'Value': 14.0}
                    ]
                },
        ]
    }


class polygon():
    def __init__(self):
        pass

    def xx(self):
        pass


class QAIndicatorHandler(QABaseHandler):
    coll = pymongo.MongoClient().quantaxis.indicator_plot

    def get(self):
        """
        {
        type: 'dot',
        data: [
          {
            Date: 20200220,
            Value: 16.5,
            Symbol: '\ue616', // \ue616(买) \ue618（卖）
            Color: 'rgb(240,0,0)',
            Baseline: 0 // 0 居中 1 上 2 下
          },
          {
            Date: 20200318,
            Value: 13.5,
            Symbol: '\ue618', // \ue616(买) \ue618（卖）
            Color: 'rgb(240,240,0)',
            Baseline: 0// 0 居中 1 上 2 下
          }
        ]
        },
        """

        indicator_id = self.get_argument('indicator', "000001_20200101_20200420_1122")
        print(indicator_id)
        [code, start, end, uniid] = indicator_id.split('_')

        self.write({
            'code': 0,
            'indicator': QA.QA_util_to_json_from_pandas(pd.DataFrame(list(self.coll.find({"code": code, "Date": {"$gte": int(start), "$lte": int(end)}, "id": uniid}, {'_id': 0}))).groupby('type', as_index=True).data.sum().reset_index()) 

        })


if __name__ == "__main__":
    import tornado
    from tornado.web import Application, RequestHandler, authenticated
    from tornado.websocket import WebSocketHandler

    app = Application(
        handlers=[
            (r"/testQ",  QAIndicatorHandler),

        ],
        debug=True
    )
    app.listen(8030)
    tornado.ioloop.IOLoop.current().start()
