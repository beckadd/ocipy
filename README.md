# ocipy: OCI Python Packaging Tool

`ocipy` allows you to publish and install Python packages using [OCI (Open Container Initiative) registries](https://opencontainers.org/). It provides a simple command-line interface to build, publish, and install Python packages as OCI images.

This is particularly useful for organizations that want to leverage their existing OCI registries' capabilities for versioning, distribution, and security of Python packages without having to setup complicated proxy infrastructure to support PyPI-based registries.

## Installation

You can install `ocipy` using pip:

```bash
pip install ocipy
```

However, if you're using it as part of your build system, you'll probably want to instead include it in your `pyproject.toml` file under the `build-system` section:

```toml
[build-system]
requires = ["ocipy"]
```

This ensures that `ocipy` is available when building your package, and it will be used automatically when you run `pip install .` or similar commands.

## Usage

### Configuration

You can configure `ocipy` using a configuration file named `ocipy.toml` or preferably `pyproject.toml`. The configuration file should be placed in the root of your project directory. See the [documentation](#) for more details on configuration options.

### Publishing a Package

Publishing a package to an OCI registry can be done using the `ocipy publish` command. This command will build your package and push it to the specified OCI registry.

```bash
ocipy publish --registry oci://registry.example.com/my-oci-package:latest
```

This will build your package in the current directory and push it to the specified OCI registry. The `--registry` option specifies the OCI registry URL where the package will be published.

You can also specify the target registry or registries in your `pyproject.toml` file. This is useful for automating the publishing process.

### Installing a Package

Installing a package can be done using the `ocipy install` command. This will pull the package from the OCI registry and install it in your environment.

```bash
ocipy install my-oci-package
```

```toml
[project]
# ... other project metadata ...

dependencies = [
    "my-oci-package @ oci://registry.example.com/my-oci-package:latest"
]

[build-system]
# You must specify ocipy as a build dependency.
requires = ["ocipy"]
```

If you have a `pyproject.toml` file in your project, you need to specify the source registry. This can be done either using a direct reference using the OCI URL or by specifying the source of the package in the `pyproject.toml` file.

```toml
[project]
# ... other project metadata ...

dependencies = ["my-oci-package"]

[tools.ocipy.sources]
my-oci-package = {
    "url" = "oci://registry.example.com/my-oci-package:latest"
}

[build-system]
# You must specify ocipy as a build dependency.
requires = ["ocipy"]
```

See the [documentation](#) for more options on configuring package sources.

## Documentation

Full documentation is available at [https://beckadd.github.io/ocipy](https://beckadd.github.io/ocipy). The documentation includes:

- **Getting Started Guide** - Installation and quick start tutorial
- **User Guide** - Detailed guides for publishing and installing packages
- **API Reference** - Complete CLI and configuration reference
- **Version History** - Changelog and versioned documentation

The documentation uses versioned hosting, so you can access documentation for specific versions of ocipy using the version selector.
