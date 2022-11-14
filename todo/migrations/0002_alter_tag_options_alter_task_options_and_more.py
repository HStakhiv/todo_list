# Generated by Django 4.1.3 on 2022-11-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["status", "-datetime"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="task",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
