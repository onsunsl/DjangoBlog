from jd.api.base import RestApi

class DspAdunitAdgroupDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.dsp.adunit.adgroup.delete'






