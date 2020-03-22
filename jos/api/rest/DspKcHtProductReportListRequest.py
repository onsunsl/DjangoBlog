from jd.api.base import RestApi

class DspKcHtProductReportListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuBrandId = None
			self.skuCid3 = None
			self.startDay = None
			self.endDay = None
			self.isOrderOrClick = None
			self.isTodayOr15Days = None
			self.orderStatusCategory = None
			self.platform = None
			self.val = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.kc.ht.product.report.list'






