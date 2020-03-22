from jd.api.base import RestApi

class DspKcEffectLocationReportListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.platform = None
			self.startDay = None
			self.endDay = None
			self.isOrderOrClick = None
			self.isTodayOr15Days = None
			self.orderStatusCategory = None

		def getapiname(self):
			return 'jingdong.dsp.kc.effect.location.report.list'






