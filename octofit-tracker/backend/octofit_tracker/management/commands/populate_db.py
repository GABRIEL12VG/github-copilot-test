from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Peter Parker', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Tony Stark', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='captain@marvel.com', team=marvel),
            User.objects.create(name='Clark Kent', email='superman@dc.com', team=dc),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team=dc),
            User.objects.create(name='Diana Prince', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-20')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-11-19')
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date='2025-11-18')

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        workout2 = Workout.objects.create(name='Cardio', description='30 min running')
        workout1.suggested_for.set(users[:3])
        workout2.suggested_for.set(users[3:])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Ensure unique index on email field for users
        with connection.cursor() as cursor:
            cursor.execute('''
                db = connection.get_database()
                db.users.createIndex({ "email": 1 }, { "unique": true })
            ''')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
