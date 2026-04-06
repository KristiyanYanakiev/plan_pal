from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from proposals.models import Proposal
from datetime import datetime, timedelta

User = get_user_model()


class ProposalViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="user1",
            password="pass12345"
        )

        self.other_user = User.objects.create_user(
            username="user2",
            password="pass12345"
        )

        self.proposal = Proposal.objects.create(
            title="View Test",
            date_time=datetime.now() + timedelta(days=1),
            owner=self.user
        )

        self.proposal.participants.add(self.user)

    def test_list_view_requires_login(self):
        response = self.client.get(reverse("proposals:list"))
        self.assertEqual(response.status_code, 302)

    def test_list_view_logged_in(self):
        self.client.login(username="user1", password="pass12345")
        response = self.client.get(reverse("proposals:list"))
        self.assertEqual(response.status_code, 200)

    def test_detail_access_allowed(self):
        self.client.login(username="user1", password="pass12345")
        response = self.client.get(reverse("proposals:details", args=[self.proposal.id]))
        self.assertEqual(response.status_code, 200)

    def test_detail_access_denied_for_non_participant(self):
        self.client.login(username="user2", password="pass12345")
        response = self.client.get(reverse("proposals:details", args=[self.proposal.id]))
        self.assertEqual(response.status_code, 404)