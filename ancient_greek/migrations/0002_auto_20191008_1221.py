# Generated by Django 2.2.4 on 2019-10-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ancient_greek', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='brothers',
            field=models.ManyToManyField(blank=True, related_name='_character_brothers_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='_character_children_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='father',
            field=models.ManyToManyField(blank=True, related_name='_character_father_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='linked_to',
            field=models.ManyToManyField(blank=True, related_name='_character_linked_to_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='mother',
            field=models.ManyToManyField(blank=True, related_name='_character_mother_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='nature',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ancient_greek.Nature'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sisters',
            field=models.ManyToManyField(blank=True, related_name='_character_sisters_+', to='ancient_greek.Character'),
        ),
        migrations.AlterField(
            model_name='nature',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
