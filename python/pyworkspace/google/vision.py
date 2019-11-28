from .google_base import *

class GoogleVision(GoogleBase):
	"""
	Google Face Detect SDK: <https://cloud.google.com/vision/docs/detecting-faces#vision_face_detection-python>
	"""

	yaml_tag = u'!google.vision'
	pip_package = 'google-cloud-vision'

	def get_client_lazy(self, **kwargs):
		from google.cloud import vision
		return vision.ImageAnnotatorClient(credentials=self.get_credential())
