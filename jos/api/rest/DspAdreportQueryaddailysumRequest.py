from jd.api.base import RestApi

class DspAdreportQueryaddailysumRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.groupId = None
			self.adId = None
			self.platform = None
			self.startDay = None
			self.endDay = None
			self.OrderStatusCategory = None
			self.isTodayOr15Days = None
			self.isOrderOrClick = None
			self.isDaily = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.adreport.queryaddailysum'






