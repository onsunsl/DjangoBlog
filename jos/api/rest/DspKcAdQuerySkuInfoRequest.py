from jd.api.base import RestApi

class DspKcAdQuerySkuInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.dsp.kc.ad.querySkuInfo'






