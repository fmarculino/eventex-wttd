# Eventex

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/fmarculino/eventex-wttd.svg?branch=master)](https://travis-ci.org/fmarculino/eventex-wttd)
[![Code Health](https://landscape.io/github/fmarculino/eventex-wttd/master/landscape.svg?style=flat)](https://landscape.io/github/fmarculino/eventex-wttd/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/f3f7caba9a0374e9936b/maintainability)](https://codeclimate.com/github/fmarculino/eventex-wttd/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f3f7caba9a0374e9936b/test_coverage)](https://codeclimate.com/github/fmarculino/eventex-wttd/test_coverage)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python 3.6.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:fmarculino/eventex-wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instancia no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configura o email
git push heroku master --force 
```