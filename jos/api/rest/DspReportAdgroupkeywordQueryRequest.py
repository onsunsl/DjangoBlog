from jd.api.base import RestApi

class DspReportAdgroupkeywordQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.groupId = None
			self.platform = None
			self.valType = None
			self.val = None
			self.clickOrOrderDay = None
			self.isOrderOrClick = None
			self.orderStatusCategory = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.report.adgroupkeyword.query'






