from jd.api.base import RestApi

class AdsDspRtbFeaturedBindMaterialRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.materialIds = None
			self.adGroupIds = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.bindMaterial'






