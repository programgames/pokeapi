# Generated manually on 2026-02-22

from django.db import migrations, models


def add_special_move_method(apps, schema_editor):
    """Add the 'special-move' MoveLearnMethod and its French name."""
    MoveLearnMethod = apps.get_model("pokemon_v2", "MoveLearnMethod")
    MoveLearnMethodName = apps.get_model("pokemon_v2", "MoveLearnMethodName")

    # Create the new MoveLearnMethod
    special_move_method = MoveLearnMethod.objects.create(
        id=12,
        name="special-move",
    )

    # Create the French name (language_id=5)
    MoveLearnMethodName.objects.create(
        move_learn_method=special_move_method,
        language_id=5,
        name="Événement",
    )


def remove_special_move_method(apps, schema_editor):
    """Remove the 'special-move' MoveLearnMethod and its names."""
    MoveLearnMethod = apps.get_model("pokemon_v2", "MoveLearnMethod")
    MoveLearnMethodName = apps.get_model("pokemon_v2", "MoveLearnMethodName")

    # Delete the name first (FK constraint)
    MoveLearnMethodName.objects.filter(move_learn_method_id=12).delete()
    # Delete the method
    MoveLearnMethod.objects.filter(id=12).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0025_pokemonstatpast"),
    ]

    operations = [
        # Add eventname field to PokemonMove
        migrations.AddField(
            model_name="pokemonmove",
            name="eventname",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        # Add the special-move method and its French name
        migrations.RunPython(add_special_move_method, remove_special_move_method),
    ]
