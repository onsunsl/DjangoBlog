from jd.api.base import RestApi

class DspAdreportMinuteconcreteGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.dimension = None
			self.id = None
			self.putType = None
			self.startMinute = None
			self.endMinute = None
			self.days = None
			self.granularity = None

		def getapiname(self):
			return 'jingdong.dsp.adreport.minuteconcrete.get'






