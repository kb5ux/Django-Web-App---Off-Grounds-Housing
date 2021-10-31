import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
                ('zipcode', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('square_feet', models.IntegerField()),

                ('demo_image', models.ImageField(upload_to='')),

                ('is_available', models.BooleanField(default=True)),
                ('listing_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(

            name='RentalCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(

            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('review_description', models.TextField(blank=True)),
                ('review_score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('review_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
