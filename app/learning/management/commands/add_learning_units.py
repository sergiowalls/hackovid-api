from django.core.management.base import BaseCommand

from learning.models import LearningUnit


class Command(BaseCommand):
    help = 'Add different learning units'

    def handle(self, *args, **options):
        LearningUnit(title='Nombres naturals i enters', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Fraccions', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Figures i cossos geomètrics', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Teoremes de Tales i de Pitàgores', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Nombres racionals', subject='Matemàtiques', course='3r ESO').save()
        LearningUnit(title='El paisatge com a resultat de la interacció entre la humanitat i el medi',
                     subject='Ciències socials', course='1r ESO').save()

        self.stdout.write(self.style.SUCCESS('Successfully added learning units'))
