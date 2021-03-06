from django.db import models
from django.contrib.auth.models import User
from openstates.data.models import LegislativeSession, Person


class NameStatus:
    # not matched yet
    UNMATCHED = "U"

    # matched to a legislator (matched_person will be true)
    MATCHED_PERSON = "P"

    # for cases where this isn't a valid sponsor
    SOURCE_ERROR = "E"

    # unresolvable
    IGNORED = "I"


NAME_STATUS_CHOICES = (
    (NameStatus.UNMATCHED, "Unmatched"),
    (NameStatus.MATCHED_PERSON, "Matched Person"),
    (NameStatus.SOURCE_ERROR, "Source Error"),
    (NameStatus.IGNORED, "Ignored"),
)


class PullStatus:
    NOT_CREATED = "N"
    CREATED = "C"
    MERGED = "M"
    REJECTED = "R"


PULL_STATUS_CHOICES = (
    (PullStatus.NOT_CREATED, "Not Created"),
    (PullStatus.CREATED, "Created"),
    (PullStatus.MERGED, "Merged"),
    (PullStatus.REJECTED, "Rejected"),
)


class UnmatchedName(models.Model):
    session = models.ForeignKey(LegislativeSession, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    sponsorships_count = models.PositiveIntegerField()
    votes_count = models.PositiveIntegerField()

    status = models.CharField(
        max_length=1, choices=NAME_STATUS_CHOICES, default=NameStatus.UNMATCHED
    )
    matched_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = [
            ("can_match_names", "Can use the name matching tool."),
        ]


class DeltaSet(models.Model):
    """a group of changes to be applied together"""

    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="delta_sets"
    )
    pr_url = models.URLField(blank=True, default="")
    pr_status = models.CharField(
        max_length=1, choices=PULL_STATUS_CHOICES, default=PullStatus.NOT_CREATED
    )
    created_at = models.DateTimeField(auto_now_add=True)


class PersonDelta(models.Model):
    """a proposed change to a single Person model"""

    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    # changes will be stored as JSON
    data_changes = models.JSONField()

    delta_set = models.ForeignKey(
        DeltaSet, on_delete=models.CASCADE, related_name="person_deltas"
    )

    class Meta:
        permissions = [
            ("can_edit", "Can edit people."),
            ("can_retire", "Can retire people."),
        ]


class PersonRetirement(models.Model):
    """a proposed retirement to a single person object"""

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    is_dead = models.BooleanField()
    is_vacant = models.BooleanField()
    reason = models.TextField()

    delta_set = models.ForeignKey(
        DeltaSet, on_delete=models.CASCADE, related_name="person_retirements"
    )


class NewPerson(models.Model):
    """a proposed addition single person object"""

    name = models.TextField()
    state = models.TextField()
    district = models.TextField()
    chamber = models.TextField()

    delta_set = models.ForeignKey(
        DeltaSet, on_delete=models.CASCADE, related_name="person_addition"
    )
