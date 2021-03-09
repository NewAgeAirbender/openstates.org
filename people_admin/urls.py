from django.urls import path, re_path
from utils.common import states
from .views import (
    people_list,
    people_matcher,
    people_matcher_session,
)

# Only allow valid state abbreviations
state_abbrs = [s.abbr.lower() for s in states]
state_abbr_pattern = r"({})".format("|".join(state_abbrs))

urlpatterns = [
    path("", people_list),
    re_path(
        r"^(?P<state>{})/matcher/$".format(state_abbr_pattern),
        people_matcher,
        name="people_matcher",
    ),
    re_path(
        r"^(?P<state>{})/matcher/(?P<session>[-\w ]+)/$".format(state_abbr_pattern),
        people_matcher_session,
    ),
]
