from jd.api.base import RestApi

class DspAdkcunitTcpaStatusUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.tcpaBidStr = None
			self.automatedBiddingType = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.tcpa.status.update'






