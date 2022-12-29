from django.db import models
from app.common.models import BaseModel

from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    name = models.CharField(max_length=80, verbose_name="Nome")
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return f"{self.pk} | {self.name}"


class Author(BaseModel):
    first_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name=_("Primeiro Nome")
    )
    last_name = models.CharField(
        max_length=150, null=False, blank=False, verbose_name=_("Último Nome")
    )

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return f"{self.pk} | {self.first_name} {self.last_name}"


class Publisher(BaseModel):
    name = models.CharField(verbose_name=_("Nome"), max_length=100)
    address = models.TextField(verbose_name=_("Endereço"), null=True, blank=True)
    phone = models.CharField(
        verbose_name=_("Telefone"), null=True, blank=True, max_length=20
    )
    site = models.URLField(verbose_name=_("Site"), null=True, blank=True)
    email = models.EmailField(
        verbose_name=_("E-mail de contato"), null=True, blank=True
    )

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Book(BaseModel):
    title = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Título"
    )
    original_title = models.CharField(
        max_length=200, verbose_name=_("Título Original"), null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_("Categoria"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    publication_date = models.DateField(
        null=True, blank=True, verbose_name="Date de publicação"
    )
    edition = models.IntegerField(default=1, verbose_name="Edição")
    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Editora"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    isbn = models.CharField(max_length=13, verbose_name="ISBN")
    author = models.ForeignKey(
        Author,
        verbose_name=_("Autor"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self) -> str:
        return f"{self.title} | ed: {self.edition}"
