from ..base import RestApi


class jdUnionOpenPromotionCommonGet(RestApi):
    '''
    获取推广连接
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.promotion.common.get'
