from django.urls import path, re_path
from .views.other import styleguide, home, state, site_search
from .views.legislators import legislators, person, find_your_legislator
from .views.bills import BillList, BillListFeed, bill, vote
from .views.donations import donate, custom_donation
from .views.fallback import fallback, legislator_fallback
from utils.common import states


OCD_ID_PATTERN = r"[a-z\d]{8}-[a-z\d]{4}-[a-z\d]{4}-[a-z\d]{4}-[a-z\d]{12}"
# Only allow valid state abbreviations
state_abbrs = [s.abbr.lower() for s in states]
state_abbr_pattern = r"({})".format("|".join(state_abbrs))

urlpatterns = [
    path("styleguide", styleguide, name="styleguide"),
    # flatpages
    path("donate/", donate),
    path("custom_donation/", custom_donation),
    # top level views
    path("", home, name="home"),
    path("find_your_legislator/", find_your_legislator, name="find_your_legislator"),
    path("search/", site_search, name="search"),
    re_path(r"^(?P<state>{})/$".format(state_abbr_pattern), state, name="state"),
    # people
    re_path(
        r"^(?P<state>{})/legislators/$".format(state_abbr_pattern),
        legislators,
        name="legislators",
    ),
    re_path(r"^person/.*\-(?P<person_id>[0-9A-Za-z]+)/$", person, name="person-detail"),
    # bills
    re_path(
        r"^(?P<state>{})/bills/$".format(state_abbr_pattern),
        BillList.as_view(),
        name="bills",
    ),
    # has trailing slash for consistency
    re_path(
        r"^(?P<state>{})/bills/feed/$".format(state_abbr_pattern),
        BillListFeed.as_view(),
        name="bills_feed",
    ),
    re_path(
        r"^(?P<state>{})/bills/(?P<session>[-\w ]+)/(?P<bill_id>[-\w\. ]+)/$".format(
            state_abbr_pattern
        ),
        bill,
        name="bill",
    ),
    re_path(r"^vote/(?P<vote_id>[-0-9a-f]+)/$", vote, name="vote-detail"),
    # fallbacks
    path("reportcard/", fallback),
    re_path(r"[a-z]{2}/votes/[A-Z]{2}V\d{8}/$", fallback),
    re_path(
        r"[a-z]{2}/legislators/(?P<legislator_id>[A-Z]{2}L\d{6})/", legislator_fallback
    ),
]
