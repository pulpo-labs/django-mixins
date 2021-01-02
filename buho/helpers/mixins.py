from django.contrib.gis.db import models


class AddressMixin(models.Model):
    """
    Este trait contiene la direccion como un campo JSON.
    :address hace referencia a la direccion en formato JSON
    :address_district hace referencia al barrio donde esta ubicado el elemento
    :address_city hace referencia a la ciudad donde esta ubicado el elemento
    :address_state hace referencia al departamento o estado donde esta ubicado el elemento
    :address_country hace referencia al pais donde esta ubicado el elemento
    :address_postal_code hace referencia al codigo postal donde esta ubicado el elemento
    :address_location_point hace referencia a las coordenadas donde esta ubicado el elemento
    """
    address = models.CharField(
        "Direccion completa.", 
        max_length=200,
        null=True,
        blank=True,
    )
    address_detail = models.CharField(
        "Detalles adicionales de la direccion", 
        max_length=200, 
        null=True,
        blank=True,
    )
    address_district = models.CharField(
        "Distrito o localidad.", 
        max_length=200, 
        null=True,
        blank=True,
    )
    address_neighborhood = models.CharField(
        "Barrio donde esta ubicado.", 
        max_length=200,
        null=True,
        blank=True,
    )
    address_city = models.CharField(
        "Ciudad donde se encuentra.",
        max_length=100,
        null=True,
        blank=True,
    )
    address_state = models.CharField(
        "Departamento donde se encuentra.", 
        max_length=100,
        null=True,
        blank=True,
    )
    address_country = models.CharField(
        "Pais donde se encuentra.", 
        max_length=100, 
        default="Colombia",
        null=True,
        blank=True,
    )
    address_postal_code = models.CharField(
        "Codigo postal donde se encuentra ubicado.",
        max_length=100,
        null=True,
        blank=True,
    )
    address_location_point = models.PointField(
        null=True, 
        spatial_index=True,
        blank=True,
    )

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """
    Este trait ayuda a almacenar si un objeto fue eliminado. La eliminacion se hace via soft delete, es decir,
    la entrada no se borra de la base de datos sino que se marca como trashed
    :trashed Booleano que indica si el objeto fue eliminado
    :trashed_at Timestamp del tiempo en el que se elimino el objeto
    """
    trashed = models.BooleanField(
        'Este campo indica si el objeto fue eliminado.', 
        default=False,
    )
    trashed_at = models.DateTimeField(
        "Este campo almacena cuando fue eliminado el objeto.",
        default=None,
        null=True,
    )

    class Meta:
        abstract = True


class TimestampsMixin(models.Model):
    """
    Esta clase contiene los elementos basicos para una entrada en la base de datos.
    :created_at contiene la fecha de creacion de la entrada.
    :updated_at contiene la fecha de modificacion de la entrada.
    """
    created_at = models.DateTimeField(
        "Cuando fue creada la entrada.", 
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "Cuando fue actualizada la entrada por ultima vez.", 
        auto_now=True,
    )

    class Meta:
        abstract = True
