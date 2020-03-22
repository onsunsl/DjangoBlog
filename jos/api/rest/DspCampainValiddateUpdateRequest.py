from jd.api.base import RestApi

class DspCampainValiddateUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.startTime = None
			self.endTime = None
			self.timeRange = None

		def getapiname(self):
			return 'jingdong.dsp.campain.validdate.update'






