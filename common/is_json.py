#写一个函数判断请求的响应是否是json格式响应
def IsJson(res):
    try:
        res=res.json()

    except Exception as e:
        print("响应值不是json{0}  ".format(e))

        # raise e
        #不raise就不会报错
    return res