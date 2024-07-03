# Generated by Django 5.0.6 on 2024-07-02 10:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_hobby_interest_userimages_userqualifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Science', 'Science'), ('Literature', 'Literature'), ('Travel', 'Travel'), ('Food', 'Food'), ('Health', 'Health'), ('Fitness', 'Fitness'), ('Education', 'Education'), ('Fashion', 'Fashion'), ('Entertainment', 'Entertainment'), ('Finance', 'Finance'), ('Politics', 'Politics'), ('Environment', 'Environment'), ('Sports', 'Sports'), ('History', 'History')], default='Technology', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='hobbies',
            field=models.ManyToManyField(to='accounts.hobby'),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='interest',
            field=models.ManyToManyField(related_name='user_interest', to='accounts.interest'),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
