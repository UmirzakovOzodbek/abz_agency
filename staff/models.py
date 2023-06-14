from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image


def upload_to(instance, filename):
    return '/'.join(['staff', str(instance.pk), filename])


class Staff(MPTTModel):

    image = models.ImageField(
        upload_to=upload_to,
        max_length=254,
        null=True
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=128
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=128
    )

    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=128
    )

    position_at_work = models.ForeignKey(
        to='position_at_work.PositionAtWork',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name='Должность'
    )

    employment_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата приема на работу'
    )

    wage = models.PositiveIntegerField(
        'Заработная плата'
    )

    parent = TreeForeignKey(
        to='Staff',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='subordinate',
        verbose_name='Начальник'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name[0]}. {self.patronymic[0]}.'

    class MPTTMeta:
        db_table = 'staff'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def save(self, *args, **kwargs):
        self.__create_image_watermark()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        childrens = self.get_children()
        if len(childrens):
            new_parent = Staff.objects.filter(
                position_at_work=self.position_at_work).exclude(id=self.pk).first()
            if new_parent:
                for children in childrens:
                    children.parent = new_parent
                Staff.objects.bulk_update(childrens, ['parent'])
        return super().delete(*args, **kwargs)

    def __create_image_watermark(instance):
        if instance.image:
            image = Image.open(instance.image)
            watermark = image.copy()
            watermark = watermark.resize(
                (image.width//5, image.height//5),
                Image.ANTIALIAS
            )
            image.paste(watermark, (image.width-watermark.width,
                        image.height-watermark.height))
            name = instance.image.field.generate_filename(
                instance, instance.image.name)
            instance.image.name = instance.image.storage.save(
                name, instance.image.file, max_length=instance.image.field.max_length)
            setattr(instance, instance.image.field.attname, instance.image.name)
            instance.image._committed = True
