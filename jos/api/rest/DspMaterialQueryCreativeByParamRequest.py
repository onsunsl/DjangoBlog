from jd.api.base import RestApi

class DspMaterialQueryCreativeByParamRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pagesize = None

		def getapiname(self):
			return 'jingdong.dsp.material.queryCreativeByParam'






