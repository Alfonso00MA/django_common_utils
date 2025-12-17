import os
from typing import Any


def get_var_from_env_or_settings(var_name_str: str, is_assert_not_none=True):
    """
    Environment variables have priority
    If not, settings


    # TODO move to django_common_utils
    """

    from django.conf import settings

    to_return_value = os.getenv(var_name_str, None)
    if to_return_value is None:
        to_return_value = getattr(settings, var_name_str, None)

    if is_assert_not_none:
        assert to_return_value is not None

    return to_return_value


def get_settings_var_or_default(var_name_str: str, default_var: Any):
    from django.conf import settings
    return getattr(settings, var_name_str, default_var)

