from jd.api.base import RestApi

class DspMaterialAddMaterialRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.materialName = None
			self.effectiveDate = None
			self.expirationDate = None
			self.skuId = None
			self.mediaId = None
			self.creativeId = None
			self.imgSrc = None
			self.url = None
			self.width = None
			self.height = None

		def getapiname(self):
			return 'jingdong.dsp.material.addMaterial'






