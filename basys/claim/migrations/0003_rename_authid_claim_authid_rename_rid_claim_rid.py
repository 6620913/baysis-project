# Generated by Django 4.1.7 on 2023-03-13 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_rename_priary_player_disc_claim_primary_player_disc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='AuthID',
            new_name='authID',
        ),
        migrations.RenameField(
            model_name='claim',
            old_name='RID',
            new_name='rID',
        ),
    ]
