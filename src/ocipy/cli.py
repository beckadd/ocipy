import typer

cli = typer.Typer(invoke_without_command=True)


@cli.command()
def add(packages: str):
    """Adds the specified package to the current project's dependencies."""
    ...


@cli.command()
def remove(packages: str):
    """Removes the specified package from the current project's dependencies."""
    ...


@cli.command()
def install(packages: str):
    """Installs the specified package into the current environment."""
    ...


@cli.command()
def uninstall(packages: str):
    """Uninstalls the specified package from the current environment."""
    ...


@cli.command()
def publish(): ...
