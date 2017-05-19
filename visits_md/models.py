from django.db import models

# Create your models here.


class Visit(models.Model):
    start_date = models.DateTimeField(
        blank=True,
    )
    end_date = models.DateTimeField(
        blank=True,
    )
    # Seat place
    # Doctor place

    def __str__(self):
        return "{}".format(self.start_date)  # here will be Patient
