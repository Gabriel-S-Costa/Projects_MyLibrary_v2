# Generated by Django 4.1.2 on 2022-12-29 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Excluído em"
                    ),
                ),
                ("name", models.CharField(max_length=80, verbose_name="Nome")),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Excluído em"
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "publication_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date de publicação"
                    ),
                ),
                ("edition", models.IntegerField(default=1, verbose_name="Edição")),
                ("isbn", models.CharField(max_length=13, verbose_name="ISBN")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.category",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Livro",
                "verbose_name_plural": "Livros",
            },
        ),
    ]
