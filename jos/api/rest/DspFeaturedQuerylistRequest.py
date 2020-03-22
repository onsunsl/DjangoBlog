from jd.api.base import RestApi

class DspFeaturedQuerylistRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.pageNum = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.featured.querylist'






