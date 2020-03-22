from jd.api.base import RestApi

class DspAdkckeywordKeywordDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.keyWordsName = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.keyword.delete'






