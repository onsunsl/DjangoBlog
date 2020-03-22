from jd.api.base import RestApi

class DspAdkcunitDmpBatchBindCrowdRefRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.adGroupId = None
			self.adGroupType = None
			self.opt = None
			self.crowdId = None
			self.isUsed = None
			self.adGroupPrice = None

		def getapiname(self):
			return 'jingdong.dsp.adkcunit.dmp.batchBindCrowdRef'






