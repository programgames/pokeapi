# Generated manually on 2026-06-05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0027_add_specialmove_method_and_eventname"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonmove",
            name="reminder_only",
            field=models.BooleanField(null=True, blank=True, default=None),
        ),
    ]
