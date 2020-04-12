from django.core.management.base import BaseCommand

from learning.models import LearningUnit


class Command(BaseCommand):
    help = 'Add different learning units'

    def handle(self, *args, **options):
        LearningUnit(title='Numeració i càlcul', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Canvi i relacions', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Espai i forma', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Mesura', subject='Matemàtiques', course='1r ESO').save()
        LearningUnit(title='Estadística i atzar', subject='Matemàtiques', course='1r ESO').save()

        LearningUnit(title='Espai i forma', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Mesura', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Estadística i atzar', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Numeració i càlcul', subject='Matemàtiques', course='2n ESO').save()
        LearningUnit(title='Canvi i relacions', subject='Matemàtiques', course='2n ESO').save()

        LearningUnit(title='Espai i forma', subject='Matemàtiques', course='3r ESO').save()
        LearningUnit(title='Mesura', subject='Matemàtiques', course='3r ESO').save()
        LearningUnit(title='Estadística i atzar', subject='Matemàtiques', course='3r ESO').save()
        LearningUnit(title='Numeració i càlcul', subject='Matemàtiques', course='3r ESO').save()
        LearningUnit(title='Canvi i relacions', subject='Matemàtiques', course='3r ESO').save()

        LearningUnit(title='Espai i forma', subject='Matemàtiques', course='4t ESO').save()
        LearningUnit(title='Mesura', subject='Matemàtiques', course='4t ESO').save()
        LearningUnit(title='Estadística i atzar', subject='Matemàtiques', course='4t ESO').save()
        LearningUnit(title='Numeració i càlcul', subject='Matemàtiques', course='4t ESO').save()
        LearningUnit(title='Canvi i relacions', subject='Matemàtiques', course='4t ESO').save()







        LearningUnit(title='El paisatge com a resultat de la interacció entre la humanitat i el medi',
                     subject='Ciències socials', course='1r ESO').save()
        LearningUnit(title='El coneixement del passat: de les societats prehistòriques al món clàssic',
                     subject='Ciències socials', course='1r ESO').save()

        LearningUnit(title='El món medieval',
                     subject='Ciències socials', course='2n ESO').save()
        LearningUnit(title='L’ocupació del territori: població i societat',
                     subject='Ciències socials', course='2n ESO').save()

        LearningUnit(title='L’edat moderna',
                     subject='Ciències socials', course='3r ESO').save()
        LearningUnit(title='Activitat econòmica i organització política',
                     subject='Ciències socials', course='3r ESO').save()

        LearningUnit(title='El món contemporani',
                     subject='Ciències socials', course='4t ESO').save()
        LearningUnit(title='El món actual ',
                     subject='Ciències socials', course='4t ESO').save()





        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua catalana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua castellana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua catalana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua castellana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió comunicació oral ',
                     subject='Llengua catalana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió comunicació oral ',
                     subject='Llengua castellana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua catalana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua castellana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió actitudinal i plurilingüe',
                     subject='Llengua catalana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió actitudinal i plurilingüe',
                     subject='Llengua castellana i literatura', course='1r ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua catalana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua castellana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua catalana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua castellana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua catalana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua castellana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua catalana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua castellana i literatura', course='2n ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua catalana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua castellana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua catalana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua castellana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua catalana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua castellana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua catalana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua castellana i literatura', course='3r ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua catalana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió comprensió lectora ',
                     subject='Llengua castellana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua catalana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió expressió escrita ',
                     subject='Llengua castellana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua catalana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió comunicació oral',
                     subject='Llengua castellana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua catalana i literatura', course='4t ESO').save()
        LearningUnit(title='Dimensió literària',
                     subject='Llengua castellana i literatura', course='4t ESO').save()






        self.stdout.write(self.style.SUCCESS('Successfully added learning units'))
