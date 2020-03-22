__atuthor__ = 'xzeu <admin@xzeu.com>'

from .api.base import sign, appinfo, getDefaultAppInfo, setDefaultAppInfo


# class appinfo(object):
#     def __init__(self, appkey, secret):
#         self.appkey = appkey
#         self.secret = secret
#
#
# def getDefaultAppInfo():
#     pass
#
#
# def setDefaultAppInfo(appkey, secret):
#     default = appinfo(appkey, secret)
#     global getDefaultAppInfo
#     getDefaultAppInfo = lambda: default
