import pymongo


def QA_fetch_indicator_id(id, coll):
    """

    id start with code


    rb2010_start_end_uniid
    """

    [code, start, end, uniid] = id.split('_')

    res = list(coll.find({"code": code, "time": {"$gte": start, "$lte": end}, "id": uniid}, {'_id':0}))