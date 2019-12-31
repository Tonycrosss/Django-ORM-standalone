import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    all_passcards_list = [Passcard.objects.all()]
    active_passcards_list = [Passcard.objects.filter(is_active=True)]
    print('Количество пропусков:', Passcard.objects.count())
    print('Количество активных пропусков:', len(active_passcards_list[0]))