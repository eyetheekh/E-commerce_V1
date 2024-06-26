# Generated by Django 4.2.10 on 2024-04-05 07:02

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('core', '0002_product_vendor_alter_category_cid_alter_product_pid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_vendor', to='core.vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact',
            field=models.CharField(default='+91 9999955555', max_length=20),
        ),
    ]
