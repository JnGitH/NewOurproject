# import datetime
# import jwt
# import time
# from functools import wraps
# from flask import request, json
#
# SECRECT_KEY = 'lvyoooo.com'
#
#
# # 签发token
# def jwtEncoding(telephone):
#     datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
#     option = {
#         'iss': 'lvyoooo.com',
#         'exp': datetimeInt,
#         'aud': 'webkit',
#         'telephone': telephone
#     }
#     encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256').decode()
#     print("签发token" + encoded2)
#     return encoded2
#
#
# # 解析jwt 信息
# def jwtDecoding():
#     decoded = None
#     try:
#         decoded = jwt.decode(request.headers["token"], SECRECT_KEY, audience='webkit', algorithms=['HS256'])
#
#         # now_time = int(time.mktime(datetime.datetime.utcnow().timetuple()))
#         # if decoded['exp'] - now_time > 0:
#         #     return decoded
#         # else:
#         #     decoded = None
#     except jwt.ExpiredSignatureError:
#         print("here1")
#         decoded = {"error_msg": "is timeout !!", "token": None}
#     except Exception:
#         decoded = {"error_msg": "noknow exception!!", "token": None}
#         print("here2")
#     return decoded
#
#
# def checkLogin(*req):
#     def decorated(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             decoded = None
#             try:
#                 token = request.headers['token']
#                 print(token)
#                 decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])
#
#             except jwt.ExpiredSignatureError:
#                 decoded = {"error_msg": "is timeout !!", "token": None}
#                 return json.jsonify(decoded)
#             except Exception:
#                 decoded = {"error_msg": "noknow exception!!", "token": None}
#                 return json.jsonify(decoded)
#             return func()
#
#         return wrapper
#
#     return decorated
