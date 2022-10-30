from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page


class HomePage(Page):

    template = 'home/index.html'
    max_count = 1

    epigraph = models.CharField(max_length=85, blank=False, null=True, help_text='company name or site name or brand or etc.')
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'])
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('epigraph', ),
        FieldPanel('banner_title', ),
        FieldPanel('banner_subtitle', ),
        ImageChooserPanel('banner_image'),
    ]

    class Meta:
        verbose_name = 'Home page'
        verbose_name_plural = 'Home pages'