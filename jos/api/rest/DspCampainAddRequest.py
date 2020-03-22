from jd.api.base import RestApi

class DspCampainAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.startTime = None
			self.endTime = None
			self.timeRange = None
			self.dayBudget = None
			self.uniformSpeed = None

		def getapiname(self):
			return 'jingdong.dsp.campain.add'






