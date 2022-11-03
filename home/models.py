from django.db import models
from wagtail.admin.panels import StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.models import Page
from streams import blocks
from wagtail.core.fields import StreamField

class HomePage(Page):

    template = 'home/index.html'
    max_count = 1

    epigraph = models.CharField(max_length=85, blank=False, null=True, help_text='company name or site name or brand or etc.')
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'], blank=False, null=True)
    about_text = RichTextField(features=['bold', 'italic'], blank=True, null=True, help_text='short introduction to yourself or your company or etc')
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    switch_diensten = models.BooleanField('Diensten aan/uit', blank=False, default=True)
    switch_over = models.BooleanField('Over aan/uit', blank=False, default=True)
    switch_portfolio = models.BooleanField('Portfolio aan/uit', blank=False, default=True)
    switch_team = models.BooleanField('Team aan/uit', blank=False, default=True)
    switch_milestones = models.BooleanField('Mijlpalen aan/uit', blank=False, default=True)
    milestones = StreamField([
        ('milestones', blocks.MileStone()),
        ],
        blank=True,
        null=True,
        use_json_field=True
    )

    services = StreamField([
        ('services', blocks.Service()),
        ],
        blank=True,
        null=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('epigraph', ),
        FieldPanel('banner_title', ),
        FieldPanel('banner_subtitle', ),
        FieldPanel('about_text', ),
        FieldPanel('banner_image'),
        FieldPanel('switch_diensten'),
        FieldPanel('switch_over'),
        FieldPanel('switch_portfolio'),
        FieldPanel('switch_team'),
        FieldPanel('switch_milestones'),
        FieldPanel('milestones'),
        FieldPanel('services'),
    ]

    class Meta:
        verbose_name = 'Home page'
        verbose_name_plural = 'Home pages'