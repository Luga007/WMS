# Generated by Django 5.2.1 on 2025-05-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(choices=[('Amir Temur', 'Amir Temur Street'), ('Buyuk Ipak Yuli', 'Buyuk Ipak Yuli Street'), ('Mustaqillik', 'Mustaqillik Street')], max_length=100)),
                ('district', models.CharField(choices=[('Shaykhontohur', 'Shaykhontohur'), ('Yunusabad', 'Yunusabad'), ('Chilonzor', 'Chilonzor'), ('Mirzo Ulugbek', 'Mirzo Ulugbek'), ('Yakkasaroy', 'Yakkasaroy')], max_length=100)),
            ],
        ),
    ]
