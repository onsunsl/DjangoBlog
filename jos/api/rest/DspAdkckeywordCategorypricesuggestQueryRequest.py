from jd.api.base import RestApi

class DspAdkckeywordCategorypricesuggestQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.key = None
			self.mobileType = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.categorypricesuggest.query'






