# Generated by Django 4.2.5 on 2023-09-09 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_myuser_remove_customuser_user_ptr'),
        ('book', '0003_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.myuser', verbose_name='the user who has book'),
        ),
    ]
