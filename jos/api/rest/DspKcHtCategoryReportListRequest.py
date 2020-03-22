from jd.api.base import RestApi

class DspKcHtCategoryReportListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
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
			return 'jingdong.dsp.kc.ht.category.report.list'






