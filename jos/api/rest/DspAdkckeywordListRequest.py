from jd.api.base import RestApi

class DspAdkckeywordListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.platform = None
			self.valType = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.list'






