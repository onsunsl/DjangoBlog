from jd.api.base import RestApi

class DspAdreportTrendChartGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDay = None
			self.endDay = None
			self.businessType = None
			self.granularity = None
			self.campaignId = None
			self.groupId = None
			self.adId = None

		def getapiname(self):
			return 'jingdong.dsp.adreport.trendChart.get'






