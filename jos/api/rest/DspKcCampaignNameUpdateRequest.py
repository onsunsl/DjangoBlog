from jd.api.base import RestApi

class DspKcCampaignNameUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.name = None

		def getapiname(self):
			return 'jingdong.dsp.kc.campaign.name.update'






