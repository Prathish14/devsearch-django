# Generated by Django 4.2.5 on 2023-11-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
