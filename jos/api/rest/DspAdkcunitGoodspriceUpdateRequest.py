from jd.api.base import RestApi

class DspAdkcunitGoodspriceUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.feeStr = None
			self.inSearchFeeStr = None
			self.mobilePriceCoef = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.goodsprice.update'






