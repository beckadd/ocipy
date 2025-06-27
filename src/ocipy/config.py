from dataclasses import dataclass, field
from collections.abc import Mapping
from pathlib import Path
from typing_extensions import Literal
import tomllib

@dataclass
class Registry:
    """Coniguration for an OCI registry.
    """

    name: str
    url: str
    authenticate: Literal["always", "never", "if-available"] = "if-available"
    package_tags: list[str] = field(default_factory=list)

@dataclass
class Config:
    """Configuration for the ocipy tool.
    """

    registries: Mapping[str, Registry]
    
    @classmethod
    def from_toml(cls, path: Path = Path("ocipy.toml")):
        """Extracts configuration from a TOML file.
        
        Args:
            path: Path to the TOML file. Defaults to `ocipy.toml` in the 
                current directory.
        Returns:
            The configuration object.

        Raises:
            FileNotFoundError: If the specified TOML file does not exist.
            ValueError: If the TOML file is not valid or does not contain 
                the expected structure.
        """

        
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f"Configuration file {path} not found.")
        
        try:
            configuration = tomllib.loads(path.read_text())
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Invalid TOML file {path}: {e}") from e

        # any tool.ocipy.* keys need to remove that suffix to be used as a key

        configuration = {
            key.removeprefix("tool.ocipy."): value
            for key, value in configuration.items()
        }

        return cls(**configuration)
