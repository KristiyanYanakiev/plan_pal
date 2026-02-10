from django.db import models


class ProposalStatusChoices(models.TextChoices):
    PROPOSED = 'Proposed', 'Proposed'
    CONFIRMED = 'Confirmed', 'Confirmed'
    UPCOMING = 'Upcoming', 'Upcoming'
    PAST = 'Past', 'Past'
    CANCELED = 'Cancelled', 'Cancelled'

