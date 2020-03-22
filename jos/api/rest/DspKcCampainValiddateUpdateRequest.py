from jd.api.base import RestApi

class DspKcCampainValiddateUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.startTime = None
			self.endTime = None
			self.timeRange = None

		def getapiname(self):
			return 'jingdong.dsp.kc.campain.validdate.update'






