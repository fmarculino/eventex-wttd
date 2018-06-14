from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fernando Marculino', cpf='55544433322',
                    email='fernandomarculino@gmail.com', phone='94-99189-4670')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fernandomarculino@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents =[
            'Fernando Marculino',
            '55544433322',
            'fernandomarculino@gmail.com',
            '94-99189-4670',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
