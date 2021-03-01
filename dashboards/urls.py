from django.urls import path, re_path
from .views import (
    user_overview,
    api_overview,
    dq_overview,
    dq_overview_session,
    dqr_listing,
    # people_list,
    # people_matcher
)
from utils.common import states

# Only allow valid state abbreviations
state_abbrs = [s.abbr.lower() for s in states]
state_abbr_pattern = r"({})".format("|".join(state_abbrs))

urlpatterns = [
    path("users/", user_overview),
    path("api/", api_overview),
    path("dq_dashboard/", dqr_listing),
    re_path(r"^dq_overview/(?P<state>{})/$".format(state_abbr_pattern), dq_overview),
    re_path(
        r"^dq_overview/(?P<state>{})/(?P<session>[-\w ]+)/$".format(state_abbr_pattern),
        dq_overview_session,
    ),
    # path("people_dashboard/", people_list),
    # re_path(r"^people_dashboard/(?P<state>{})/$".format(state_abbr_pattern), people_matcher),
]
