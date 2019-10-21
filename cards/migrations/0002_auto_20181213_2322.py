# Generated by Django 2.1.4 on 2018-12-13 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Publication'),
        ),
    ]