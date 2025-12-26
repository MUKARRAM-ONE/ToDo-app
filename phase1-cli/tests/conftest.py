"""Test configuration and shared fixtures."""

import pytest
from unittest.mock import Mock
from typing import Any

# Placeholder for shared fixtures - will be populated as tests are written


@pytest.fixture
def mock_repository() -> Mock:
    """Create a mock task repository for testing."""
    return Mock()
