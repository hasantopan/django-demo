# Generated by Django 4.0.4 on 2022-04-30 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_alter_yazilarmodel_icerik'),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now=True)),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='yorum', to=settings.AUTH_USER_MODEL)),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='yorumlar', to='blog.yazilarmodel')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'yorum',
            },
        ),
    ]
