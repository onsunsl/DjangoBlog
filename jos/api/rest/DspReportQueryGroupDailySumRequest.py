from jd.api.base import RestApi

class DspReportQueryGroupDailySumRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.isDaily = None
			self.campaignId = None
			self.groupId = None
			self.startDay = None
			self.endDay = None
			self.isOrderOrClick = None
			self.isTodayOr15Days = None
			self.orderStatusCategory = None
			self.platform = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.report.queryGroupDailySum'






