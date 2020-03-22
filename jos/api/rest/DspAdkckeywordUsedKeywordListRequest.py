from jd.api.base import RestApi

class DspAdkckeywordUsedKeywordListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.groupId = None
			self.campaignId = None
			self.platform = None
			self.valType = None
			self.clickOrOrderDay = None
			self.isOrderOrClick = None
			self.pageIndex = None
			self.pageSize = None
			self.orderStatusCategory = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.usedKeyword.list'






