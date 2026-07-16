"""Regression tests for H2 matched-null inference."""

from __future__ import annotations

import numpy as np
from scripts.h2_centralization_test import empirical_upper_p


def test_empirical_upper_p_treats_rounded_equal_values_as_equal() -> None:
    null = np.full(1_000, 0.068181818)

    assert empirical_upper_p(0.0682, null) == 1.0


def test_empirical_upper_p_uses_plus_one_correction() -> None:
    null = np.zeros(1_000)

    assert empirical_upper_p(1.0, null) == 1 / 1_001
