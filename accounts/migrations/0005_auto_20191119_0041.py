# Generated by Django 2.2.7 on 2019-11-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191118_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='accounts',
        ),
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.EmailField(default='noemail@gmail.com', max_length=254),
        ),
    ]
