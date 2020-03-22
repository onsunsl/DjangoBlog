from jd.api.base import RestApi

class DspCpdReportGetEffectReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.pageNo = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.cpd.report.getEffectReport'






