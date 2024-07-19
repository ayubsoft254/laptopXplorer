#!/bin/bash

# List of Django libraries to install
libraries=(
  djangorestframework
  django-allauth
  django-crispy-forms
  django-extensions
  django-celery
  django-debug-toolbar
  channels
  django-filter
  django-storages
  django-guardian
  django-cors-headers
  django-compressor
  django-wysiwyg
  django-haystack
  django-versatileimagefield
  django-braces
  django-redis
  django-model-utils
)

# Install each library with --break-system-packages option
for library in "${libraries[@]}"; do
  pip install "$library" --break-system-packages
done

echo "All specified Django libraries have been installed."

