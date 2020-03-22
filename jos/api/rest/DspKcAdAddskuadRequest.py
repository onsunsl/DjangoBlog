from jd.api.base import RestApi

class DspKcAdAddskuadRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.adGroupId = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.dsp.kc.ad.addskuad'






