from jd.api.base import RestApi

class DspKcEffectKeywordReportListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDay = None
			self.endDay = None
			self.isDaily = None
			self.clickOrOrderDay = None
			self.areaId = None
			self.campaignId = None
			self.groupId = None
			self.adId = None
			self.keywords = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.kc.effect.keyword.report.list'






