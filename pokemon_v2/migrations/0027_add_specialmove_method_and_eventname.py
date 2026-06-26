# Generated manually on 2026-02-22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0026_alter_pokemonevolution_base_form"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonmove",
            name="eventname",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
