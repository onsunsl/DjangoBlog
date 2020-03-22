from jd.api.base import RestApi

class DspReportQueryAccountKeywordReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDay = None
			self.endDay = None
			self.isDaily = None
			self.platform = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.orderStatusCategory = None
			self.campaignId = None
			self.groupId = None
			self.valType = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.report.queryAccountKeywordReport'






