from django.test import TestCase
from .models import Skill
import unittest
from django.core.mail import send_mail
from django.core import mail

# Create your tests here.
# class ProjectModelTests(TestCase):
#     def test_



class PortfolioTests(TestCase):
    def test_db_connection(self):
        skills = Skill.objects.all()
        self.assertIsNotNone(skills, msg="skills does not exist")

    def test_send_email(self):
        send_mail('Message from Portfolio contact page.',
                  'This is the message',
                  from_email='beja0405@gmail.com',
                  recipient_list=['jake.bestland@gmail.com'],
                  html_message = 'testing')
        
        self.assertEqual(len(mail.outbox),1,"No emails were sent.")

if __name__ == "__main__":
    unittest.main()