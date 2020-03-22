from jd.api.base import RestApi

class DspKcAdAddshopadRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.skuId = None
			self.imgUrl = None
			self.adGroupId = None
			self.url = None
			self.showSalesWord = None

		def getapiname(self):
			return 'jingdong.dsp.kc.ad.addshopad'






