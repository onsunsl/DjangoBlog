from jd.api.base import RestApi

class DspKcCampainListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pageNum = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.kc.campain.list'






