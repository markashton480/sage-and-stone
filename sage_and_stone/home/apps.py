"""
Django AppConfig for the client home app.

Replace 'sage_and_stone' with your actual project name after copying.
Both 'name' and 'label' must be updated.
"""
from __future__ import annotations

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Configuration for the client home app."""

    default_auto_field = "django.db.models.BigAutoField"
    # Update these after renaming sage_and_stone:
    name = "sage_and_stone.home"
    label = "sage_and_stone_home"
    verbose_name = "Home"
