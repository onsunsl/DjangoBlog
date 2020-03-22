from jd.api.base import RestApi

class DspAdunitPriceUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.inFee = None
			self.outFee = None
			self.adxFee = None

		def getapiname(self):
			return 'jingdong.dsp.adunit.price.update'






