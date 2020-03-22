from jd.api.base import RestApi

class DspFeaturedUpdatestatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.status = None
			self.id = None

		def getapiname(self):
			return 'jingdong.dsp.featured.updatestatus'






