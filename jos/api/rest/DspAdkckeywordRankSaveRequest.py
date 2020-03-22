from jd.api.base import RestApi

class DspAdkckeywordRankSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.searchPromoteRankEnable = None
			self.searchPromoteRankType = None
			self.searchPromoteRankCoef = None
			self.ids = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.rank.save'






