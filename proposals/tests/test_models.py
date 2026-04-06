from django.test import TestCase
from django.contrib.auth import get_user_model
from proposals.models import Proposal
from datetime import datetime, timedelta

User = get_user_model()


class ProposalModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.proposal = Proposal.objects.create(
            title="Test Proposal",
            date_time=datetime.now() + timedelta(days=1),
            owner=self.user
        )

        self.proposal.participants.add(self.user)

    def test_proposal_creation(self):
        self.assertEqual(self.proposal.title, "Test Proposal")
        self.assertEqual(self.proposal.owner, self.user)

    def test_participant_added(self):
        self.assertIn(self.user, self.proposal.participants.all())