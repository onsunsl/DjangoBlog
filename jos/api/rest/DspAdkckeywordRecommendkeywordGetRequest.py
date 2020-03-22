from jd.api.base import RestApi

class DspAdkckeywordRecommendkeywordGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.searchType = None
			self.order = None
			self.sortType = None
			self.keyWordType = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.recommendkeyword.get'






