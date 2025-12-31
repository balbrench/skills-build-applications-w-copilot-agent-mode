from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength training for heroes', suggested_for='marvel'),
            Workout.objects.create(name='Agility Training', description='Agility and reflexes', suggested_for='dc'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='flight', duration=60, date=date.today())
        Activity.objects.create(user=users[1], type='web-swinging', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='detective work', duration=90, date=date.today())
        Activity.objects.create(user=users[3], type='combat training', duration=50, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=95, rank=3)
        Leaderboard.objects.create(user=users[3], score=85, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
