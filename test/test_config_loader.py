from pathlib import Path
from typing import Any
import tomlkit

import pytest


@pytest.fixture
def config() -> dict[str, Any]:
    """Fixture to provide a sample configuration for ocipy."""
    
    configuration = {
        "registries": {
            "example-registry": {
                "name": "Example Registry",
                "url": "https://example.com/oci",
                "authenticate": "if-available",
                "package_tags": ["latest", "stable"]
            }
        }
    }

    return configuration

@pytest.fixture
def ocipy_config(config: dict[str, Any], tmp_path: Path) -> Path:
    """Fixture to create a temporary configuration file for ocipy."""
    config_path = tmp_path / "ocipy.toml"
    with config_path.open("w") as f:
        tomlkit.dump(config, f)
    return config_path

@pytest.fixture
def pyproject_config(config: dict[str, Any], tmp_path: Path) -> Path:
    """Fixture to create a temporary pyproject.toml file for ocipy."""
    config_path = tmp_path / "pyproject.toml"

    modified_config = {
        "tool": {
            "ocipy": config
        }
    }

    with config_path.open("w") as f:
        tomlkit.dump(modified_config, f)

    return config_path

@pytest.mark.parametrize()
def test_valid_config(config_file: Path, config):
    """Test the configuration loader for ocipy."""
    ...

def test_missing_config():
    ...
