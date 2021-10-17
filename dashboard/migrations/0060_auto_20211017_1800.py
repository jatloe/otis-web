# Generated by Django 3.2.8 on 2021-10-17 22:00

from django.db import migrations
from django.db.models import OuterRef, Subquery


def refactor_suggestion(apps, schema_editor):
	suggestions = apps.get_model('dashboard', 'ProblemSuggestion')
	suggestions.objects.all().update(
		user=Subquery(suggestions.objects.filter(pk=OuterRef('pk')).values('student__user')[:1])
	)


class Migration(migrations.Migration):
	dependencies = [
		('dashboard', '0059_problemsuggestion_user'),
	]
	operations = [migrations.RunPython(refactor_suggestion, migrations.RunPython.noop)]
