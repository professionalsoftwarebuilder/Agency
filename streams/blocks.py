"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(max_length=45, required=True)),
            ('text', blocks.TextBlock(required=False, max_length=300)),
            ('button_page', blocks.PageChooserBlock(required=False)),
            ('button_url', blocks.URLBlock(required=False,
                                           help_text='If the button page above is selected, that wil be user first')),
        ]))

    class Meta:
        template = 'streams/card_block.html'
        icon = 'placeholder'
        label = 'Staff cards'


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothin else"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=False, help_text='Add additional text')

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'


class RichTextBlock(blocks.RichTextBlock):
    """Richtekst with all the features"""

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full rich text'


class SimpleRichTextBlock(blocks.RichTextBlock):
    """Richtekst with all the features"""

    def __init__(
            self,
            required=True,
            help_text=None,
            editor="default",
            features=None,
            validators=(),
            **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = ['bold', 'italic', 'link']

    class Meta:
        # let op we gebuiken dezelfde html file (geen simple_richtext... kan wel maar hoeft niet)
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple rich text'


class MileStone(blocks.StructBlock):
    """Cards with image and text and button"""

    switch = blocks.BooleanBlock(required=True, help_text='Switch milestones on or off')
    caption = blocks.CharBlock(required=True, max_length=300, help_text='Opschrift boven mijlpalen')
    milestone = blocks.ListBlock(
        blocks.StructBlock([
            ('date', blocks.CharBlock(required=True, max_length=65, help_text='Datum of periode aanduiding, (Kan ook "gewoon" eerste regel van kop zijn)')),
            ('title', blocks.CharBlock(max_length=85, required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('text', blocks.TextBlock(required=False)),
        ]))

    class Meta:
        template = 'streams/milestone_block.html'
        icon = 'placeholder'
        label = 'Milestones'


class Service(blocks.StructBlock):
    """Cards with image and text and button"""

    #switch = blocks.BooleanBlock(required=True, help_text='Switch services on or off on page')
    #caption = blocks.CharBlock(required=True, max_length=300, help_text='Opschrift boven diensten')
    service = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(max_length=85, required=True)),
            ('fa_classes', blocks.CharBlock(max_length=300, required=False, help_text='Eventuele font awesome icon classes, wanneer deze worden gebruikt, vervangt het de image op de pagina')),
            ('image', ImageChooserBlock(required=False, help_text='Wordt getoond wanneer er geen font awesome icon classes opgegeven zijn')),
            ('text', blocks.TextBlock(required=False)),
        ]))

    class Meta:
        template = 'streams/service_block.html'
        icon = 'placeholder'
        label = 'Diensten'

