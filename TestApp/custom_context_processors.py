from .models import *


def general(context):
    technologys = Technology.objects.all()

    return {
        'technologys': technologys,
    }
