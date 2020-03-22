from jd.api.base import RestApi

class DspAdkcunitAdgroupListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pageNum = None
			self.pageSize = None
			self.campaignId = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.adgroup.list'






