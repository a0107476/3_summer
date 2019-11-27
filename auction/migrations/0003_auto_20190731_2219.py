# Generated by Django 2.2.3 on 2019-07-31 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0002_delete_addsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('writerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.Write')),
            ],
        ),
        migrations.CreateModel(
            name='Addsale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('salesperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='write',
            name='biddings',
            field=models.ManyToManyField(through='auction.Bid', to=settings.AUTH_USER_MODEL),
        ),
    ]
