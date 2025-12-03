<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# miaard

Minimum Information about any Radiocarbon Date

## Documentation Website

[https://MIxS-MInAS.github.io/miaard](https://MIxS-MInAS.github.io/miaard)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [c14](src/c14)
    * [schema/](src/c14/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/c14/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## User Information

To validate the schema you will need LinkML installed.

As an example, you can see the contents of `examples/example-1.csv` of an example
of a radiocarbon date collection that can be  validated against the schema.

```csv
lab_id,conventional_age
MAMS 81038,4468
```

To validate, you then run the following command:

```bash
linkml-validate --schema src/c14/schema/c14.yaml --target-class RadiocarbonDate examples/example-1.csv
```

## Developer Tools

### Set up

After cloning the repository, you will need `uv`, `just` and `pre-commit` to
run the developer commands.

To install with `pipx`:

```bash
pipx install uv
pipx install just
pipx install pre-commit
```

### Running Commands

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

A typical workflow is:

```bash
## Testing
just test
just lint
just testdoc

## Pushing
just site
pre-commit run -a
```

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
