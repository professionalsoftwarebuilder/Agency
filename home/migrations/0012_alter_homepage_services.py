# Generated by Django 4.0.8 on 2022-11-05 17:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_logo_alter_homepage_milestones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.StreamField([('services', wagtail.blocks.StructBlock([('service', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=85, required=True)), ('svg_img', wagtailsvg.blocks.SvgChooserBlock(required=False)), ('fa_classes', wagtail.blocks.CharBlock(help_text='Eventuele font awesome icon classes, wanneer deze worden gebruikt, vervangt het de image op de pagina', max_length=300, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Wordt getoond wanneer er geen font awesome icon classes opgegeven zijn', required=False)), ('text', wagtail.blocks.TextBlock(required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
