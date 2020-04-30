from django.db import models
# from data.models import Jurisdiction, LegislativeSession
# from django.contrib.contenttypes.fields import GenericForeignKey


class DataQualityDashboard(models.Model):

    state = models.CharField(max_length=3)
    chamber = models.CharField(max_length=20)
    session = models.CharField(max_length=20)

    total_bills = models.PositiveIntegerField()
    latest_bill_created_date = models.DateTimeField()
    latest_action_date = models.DateTimeField()
    earliest_action_date = models.DateTimeField()

    average_sponsors_per_bill = models.PositiveIntegerField()
    min_sponsors_per_bill = models.PositiveIntegerField()
    max_sponsors_per_bill = models.PositiveIntegerField()

    average_actions_per_bill = models.PositiveIntegerField()
    min_actions_per_bill = models.PositiveIntegerField()
    max_actions_per_bill = models.PositiveIntegerField()

    average_votes_per_bill = models.PositiveIntegerField()
    min_votes_per_bill = models.PositiveIntegerField()
    max_votes_per_bill = models.PositiveIntegerField()

    average_documents_per_bill = models.PositiveIntegerField()
    min_documents_per_bill = models.PositiveIntegerField()
    max_documents_per_bill = models.PositiveIntegerField()

    average_versions_per_bill = models.PositiveIntegerField()
    min_versions_per_bill = models.PositiveIntegerField()
    max_versions_per_bill = models.PositiveIntegerField()

    total_bills_no_sources = models.PositiveIntegerField()
    total_votes_no_sources = models.PositiveIntegerField()

    overall_number_of_subjects = models.PositiveIntegerField()
    number_of_subjects_in_chamber = models.PositiveIntegerField()
    number_of_bills_without_subjects = models.PositiveIntegerField()

    total_bills_without_versions = models.PositiveIntegerField()

    total_votes_without_voters = models.PositiveIntegerField()
    total_votes_where_votes_dont_match_voters = models.PositiveIntegerField()


    class Meta:
        db_table = "dataqualitydashboard"