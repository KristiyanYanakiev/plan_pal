from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from proposals.models import Proposal
from votes.models import Vote
from datetime import datetime, timedelta

User = get_user_model()


class VoteTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.owner = User.objects.create_user(
            username="owner",
            password="pass12345"
        )

        self.user = User.objects.create_user(
            username="user",
            password="pass12345"
        )

        self.other = User.objects.create_user(
            username="other",
            password="pass12345"
        )

        self.proposal = Proposal.objects.create(
            title="Voting Test",
            date_time=datetime.now() + timedelta(days=1),
            owner=self.owner
        )

        self.proposal.participants.add(self.user)

    def test_user_can_vote_yes(self):
        self.client.login(username="user", password="pass12345")

        url = reverse("proposals:vote", args=[self.proposal.id, 1])
        response = self.client.post(url)

        vote = Vote.objects.get(user=self.user, proposal=self.proposal)

        self.assertTrue(vote.yes)
        self.assertEqual(response.status_code, 302)

    def test_user_can_vote_no(self):
        self.client.login(username="user", password="pass12345")

        url = reverse("proposals:vote", args=[self.proposal.id, 0])
        self.client.post(url)

        vote = Vote.objects.get(user=self.user, proposal=self.proposal)

        self.assertFalse(vote.yes)

    def test_vote_updates_not_duplicates(self):
        self.client.login(username="user", password="pass12345")

        url_yes = reverse("proposals:vote", args=[self.proposal.id, 1])
        url_no = reverse("proposals:vote", args=[self.proposal.id, 0])

        self.client.post(url_yes)
        self.client.post(url_no)

        votes = Vote.objects.filter(user=self.user, proposal=self.proposal)

        self.assertEqual(votes.count(), 1)
        self.assertFalse(votes.first().yes)

    def test_owner_cannot_vote(self):
        self.client.login(username="owner", password="pass12345")

        url = reverse("proposals:vote", args=[self.proposal.id, 1])
        self.client.post(url)

        votes = Vote.objects.filter(user=self.owner, proposal=self.proposal)

        self.assertEqual(votes.count(), 0)

    def test_non_participant_cannot_vote(self):
        self.client.login(username="other", password="pass12345")

        url = reverse("proposals:vote", args=[self.proposal.id, 1])
        self.client.post(url)

        votes = Vote.objects.filter(user=self.other, proposal=self.proposal)

        self.assertEqual(votes.count(), 0)