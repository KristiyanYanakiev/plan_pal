from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from connections.models import Connection

User = get_user_model()


class ConnectionTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(
            username="user1",
            password="pass12345"
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="pass12345"
        )

        self.user3 = User.objects.create_user(
            username="user3",
            password="pass12345"
        )

    def test_send_connection_request(self):
        self.client.login(username="user1", password="pass12345")

        response = self.client.post(
            f"/connections/send/{self.user2.id}/"
        )

        self.assertEqual(response.status_code, 302)

        conn = Connection.objects.get(
            from_user=self.user1,
            to_user=self.user2
        )

        self.assertFalse(conn.accepted)

    def test_accept_connection_request(self):
        conn = Connection.objects.create(
            from_user=self.user1,
            to_user=self.user2,
            accepted=False
        )

        self.client.login(username="user2", password="pass12345")

        response = self.client.post(
            f"/connections/accept/{conn.id}/"
        )

        conn.refresh_from_db()

        self.assertTrue(conn.accepted)
        self.assertEqual(response.status_code, 302)

    def test_unique_connection_constraint(self):
        Connection.objects.create(
            from_user=self.user1,
            to_user=self.user2
        )

        obj, created = Connection.objects.get_or_create(
            from_user=self.user1,
            to_user=self.user2
        )

        self.assertFalse(created)
        self.assertEqual(Connection.objects.count(), 1)

    def test_get_friends_returns_accepted_connections(self):
        Connection.objects.create(
            from_user=self.user1,
            to_user=self.user2,
            accepted=True
        )

        Connection.objects.create(
            from_user=self.user3,
            to_user=self.user1,
            accepted=True
        )

        friends = self.user1.get_friends()

        self.assertIn(self.user2, friends)
        self.assertIn(self.user3, friends)
        self.assertEqual(friends.count(), 2)