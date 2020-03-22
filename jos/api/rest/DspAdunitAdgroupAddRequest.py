from jd.api.base import RestApi

class DspAdunitAdgroupAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.name = None
			self.campaignId = None
			self.position = None
			self.inFee = None
			self.outFee = None
			self.adOptimize = None
			self.adDevice = None

		def getapiname(self):
			return 'jingdong.dsp.adunit.adgroup.add'






