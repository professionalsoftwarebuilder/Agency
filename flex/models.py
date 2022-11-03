"""Flexible page"""
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks

class FlexPage(Page):
    """Flexible page class"""

    templates = 'flex/flex_page.html'

    content = StreamField([
        ('title_and_text', blocks.TitleAndTextBlock()),
        ('full_rich_text', blocks.RichTextBlock()),
        ('simple_rich_text', blocks.SimpleRichTextBlock()),
        ('cards', blocks.CardBlock()),

        ],
        null=True,
        blank=True,
        use_json_field=True
        )

    subtitle = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Flex page'
        verbose_name_plural = 'Flex pages'