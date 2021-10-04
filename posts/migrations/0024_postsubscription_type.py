# Generated by Django 3.2 on 2021-10-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20210929_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsubscription',
            name='type',
            field=models.CharField(choices=[('all', 'Все комментарии'), ('top', 'Только комментарии первого уровня')], default='top', max_length=32),
        ),
        # for all post authors set type = all
        migrations.RunSQL(
            """update post_subscriptions set type = 'all' where (post_id, user_id) in (select id, author_id from posts)"""
        ),
    ]