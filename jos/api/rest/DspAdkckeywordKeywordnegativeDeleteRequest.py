from jd.api.base import RestApi

class DspAdkckeywordKeywordnegativeDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.keywordName = None
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.keywordnegative.delete'






