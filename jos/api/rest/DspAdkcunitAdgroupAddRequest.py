from jd.api.base import RestApi

class DspAdkcunitAdgroupAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.campaignId = None
			self.newAreaId = None
			self.feeStr = None
			self.inSearchFeeStr = None
			self.mobilePriceCoef = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.adgroup.add'






