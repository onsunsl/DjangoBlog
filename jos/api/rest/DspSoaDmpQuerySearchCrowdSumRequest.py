from jd.api.base import RestApi

class DspSoaDmpQuerySearchCrowdSumRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.groupId = None
			self.campaignId = None
			self.startDay = None
			self.endDay = None
			self.isOrderOrClick = None
			self.isTodayOr15Days = None
			self.orderStatusCategory = None

		def getapiname(self):
			return 'jingdong.dsp.soa.dmp.querySearchCrowdSum'






