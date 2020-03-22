from jd.api.base import RestApi

class DspFeaturedorderdetailOrdereffectdetailRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.groupId = None
			self.mySelf = None
			self.province = None
			self.mediaId = None
			self.unionid = None
			self.orderStatus = None
			self.clickStartDay = None
			self.clickEndDay = None
			self.orderStartDay = None
			self.orderEndDay = None
			self.realTime = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.featuredorderdetail.ordereffectdetail'






