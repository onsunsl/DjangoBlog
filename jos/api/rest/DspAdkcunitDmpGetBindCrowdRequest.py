from jd.api.base import RestApi

class DspAdkcunitDmpGetBindCrowdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.displayType = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.dmp.getBindCrowd'






