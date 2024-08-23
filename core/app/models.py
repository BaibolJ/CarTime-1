from django.db import models


class ImgFile(models.Model):
    file = models.ImageField(
        upload_to='media/photo_details'
    )


class BrandCars(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(
        max_length=500
    )
    price_day = models.PositiveIntegerField()
    img_main = models.ImageField(
        upload_to='media/logo'
    )
    detail_img = models.ManyToManyField(
        ImgFile
    )
    volume = models.DecimalField(
        max_digits=8,
        decimal_places=1
    )
    power = models.IntegerField()
    fuel_type = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Дизель'),
            (2, 'Бензин'),
            (3, 'Электро'),
        )
    )
    gearbox = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Механика'),
            (2, "Автомат")
        )
    )
    type_car_body = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Гибрид'),
            (2, 'Электро'),
            (3, 'ДВС')
        )
    )
    brand = models.ForeignKey(
        BrandCars,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Забронирован'),
            (2, "Свободен")
        ),
        default=1
    )
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Rental(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    total_cost = models.PositiveIntegerField()

    def __str__(self):
        return self.car

