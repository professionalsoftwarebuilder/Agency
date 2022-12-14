# Generated by Django 4.0.8 on 2022-10-31 16:28

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_milestones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='milestones',
            field=wagtail.fields.StreamField([('milestones', wagtail.blocks.StructBlock([('switch', wagtail.blocks.BooleanBlock(help_text='Switch milestones on or off', required=True)), ('milestone', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(format='%d %B %Y', required=True)), ('title', wagtail.blocks.CharBlock(max_length=45, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.blocks.TextBlock(max_length=1000, required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
