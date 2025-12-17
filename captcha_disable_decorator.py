from captcha.conf import settings as captcha_settings
from django.test.utils import TestContextDecorator

class ignore_captcha_errors(TestContextDecorator):

	# sacado de
	# https://github.com/mbi/django-simple-captcha/issues/84#issuecomment-2097785929

	def __init__(self):
		super().__init__()
		self.captcha_test_mode = captcha_settings.CAPTCHA_TEST_MODE

	def enable(self):
		captcha_settings.CAPTCHA_TEST_MODE = True

	def disable(self):
		captcha_settings.CAPTCHA_TEST_MODE = self.captcha_test_mode

	def decorate_class(self, cls):
		from django.test import SimpleTestCase
		if not issubclass(cls, SimpleTestCase):
			raise ValueError(
				"Only subclasses of Django SimpleTestCase can be decorated "
				"with ignore_captcha_errors"
			)
		self.captcha_test_mode = captcha_settings.CAPTCHA_TEST_MODE
		return cls
