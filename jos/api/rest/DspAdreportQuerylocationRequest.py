from jd.api.base import RestApi

class DspAdreportQuerylocationRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.platform = None
			self.startDay = None
			self.endDay = None
			self.OrderStatusCategory = None
			self.isTodayOr15Days = None
			self.isOrderOrClick = None

		def getapiname(self):
			return 'jingdong.dsp.adreport.querylocation'






