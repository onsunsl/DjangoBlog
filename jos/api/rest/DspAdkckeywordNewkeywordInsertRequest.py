from jd.api.base import RestApi

class DspAdkckeywordNewkeywordInsertRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.price = None
			self.type = None
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.newkeyword.insert'






