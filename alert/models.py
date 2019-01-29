from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class Alert(Page):
	statement = models.CharField(max_length=250)
	sitewide = models.BooleanField()
	startdate = models.DateField()
	enddate = models.DateField()

	content_panels = Page.content_panels + [
		FieldPanel('statement'),
		FieldPanel('sitewide'),
		FieldPanel('startdate'),
		FieldPanel('enddate'),
	]
