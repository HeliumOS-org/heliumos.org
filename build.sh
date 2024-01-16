#!/usr/bin/env bash

rm -rdf dist static

cd heliumos_website

npm run tw-build

python manage.py distill-local --force --collectstatic ../dist

cd ..