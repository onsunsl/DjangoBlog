from jd.api.base import RestApi

class DspKcAdDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None

		def getapiname(self):
			return 'jingdong.dsp.kc.ad.delete'






