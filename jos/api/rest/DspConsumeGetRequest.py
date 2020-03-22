from jd.api.base import RestApi

class DspConsumeGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.endDate = None
			self.pageIndex = None
			self.pageSize = None
			self.type = None

		def getapiname(self):
			return 'jingdong.dsp.consume.get'






