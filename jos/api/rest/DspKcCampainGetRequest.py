from jd.api.base import RestApi

class DspKcCampainGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.campaignId = None

		def getapiname(self):
			return 'jingdong.dsp.kc.campain.get'






