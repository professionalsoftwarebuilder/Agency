# Generated by Django 4.0.8 on 2022-11-03 22:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsvg', '0005_alter_svg_file'),
        ('home', '0010_homepage_switch_diensten_homepage_switch_milestones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='milestones',
            field=wagtail.fields.StreamField([('milestones', wagtail.blocks.StructBlock([('switch', wagtail.blocks.BooleanBlock(help_text='Switch milestones on or off', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='Opschrift boven mijlpalen', max_length=300, required=True)), ('milestone', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.CharBlock(help_text='Datum of periode aanduiding, (Kan ook "gewoon" eerste regel van kop zijn)', max_length=65, required=True)), ('title', wagtail.blocks.CharBlock(max_length=85, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.StreamField([('services', wagtail.blocks.StructBlock([('service', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=85, required=True)), ('fa_classes', wagtail.blocks.CharBlock(help_text='Eventuele font awesome icon classes, wanneer deze worden gebruikt, vervangt het de image op de pagina', max_length=300, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Wordt getoond wanneer er geen font awesome icon classes opgegeven zijn', required=False)), ('text', wagtail.blocks.TextBlock(required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]