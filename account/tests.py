from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="AhmadDibo",
            email="ahmadaldibo212009@gmail.com",
            password="12345678"
        )

    def test_login_success(self):
        """
        Test dat een gebruiker correct wordt ingelogd
        via de echte login view (email + password).
        """

        response = self.client.post(
            reverse("login"),  # ⚠️ deze URL moet bestaan
            {
                "email": "ahmadaldibo212009@gmail.com",
                "password": "12345678"
            },
            follow=True
        )

        self.assertTrue(response.wsgi_request.user.is_authenticated)


class SessionDataTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_session_is_created_after_data_write(self):
        """
        Django maakt pas een session aan
        zodra er data wordt opgeslagen.
        """

        session = self.client.session
        session["test_key"] = "test_value"
        session.save()

        self.assertIsNotNone(session.session_key)

    def test_session_store_and_retrieve_data(self):
        """
        Verifieert opslag en ophalen van session data.
        """

        session = self.client.session
        session["language"] = "nl"
        session.save()

        response = self.client.get("/")
        session = response.wsgi_request.session

        self.assertEqual(session["language"], "nl")
    
    def test_session_items(self):
        """
        Controleert dat session.items() correct werkt.
        """

        session = self.client.session
        session["key1"] = "value1"
        session["key2"] = "value2"
        session.save()

        session = self.client.session
        items = dict(session.items())
        print(items)

        self.assertEqual(items["key1"], "value1")
        self.assertEqual(items["key2"], "value2")


class SessionWithAuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="AhmadDibo",
            email="ahmadaldibo212009@gmail.com",
            password="12345678"
        )

    def test_user_id_in_session_after_login(self):
        """
        Controleert of Django na login
        het user ID in de session zet.
        """

        self.client.post(
            reverse("login"),
            {
                "email": "ahmadaldibo212009@gmail.com",
                "password": "12345678"
            }
        )

        session = self.client.session


        self.assertIn("_auth_user_id", session)
        self.assertEqual(int(session["_auth_user_id"]), self.user.id)
