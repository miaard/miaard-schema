from __future__ import annotations

import re
from typing import Any, ClassVar, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer,
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True,
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )

    @model_serializer(mode="wrap", when_used="unless-none")
    def treat_empty_lists_as_none(
        self, handler: SerializerFunctionWrapHandler, info: SerializationInfo
    ) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not (field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "c14",
        "default_range": "string",
        "description": "Minimum Information about any Radiocarbon Date",
        "id": "https://w3id.org/MIxS-MInAS/miaard",
        "imports": ["linkml:types"],
        "license": "MIT",
        "name": "miaard",
        "prefixes": {
            "PATO": {
                "prefix_prefix": "PATO",
                "prefix_reference": "http://purl.obolibrary.org/obo/PATO_",
            },
            "biolink": {
                "prefix_prefix": "biolink",
                "prefix_reference": "https://w3id.org/biolink/",
            },
            "c14": {
                "prefix_prefix": "c14",
                "prefix_reference": "https://w3id.org/MIxS-MInAS/miaard/",
            },
            "example": {
                "prefix_prefix": "example",
                "prefix_reference": "https://example.org/",
            },
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            },
            "schema": {
                "prefix_prefix": "schema",
                "prefix_reference": "http://schema.org/",
            },
        },
        "see_also": ["https://MIxS-MInAS.github.io/miaard"],
        "source_file": "src/c14/schema/c14.yaml",
        "title": "miaard",
    }
)


class RadiocarbonDate(ConfiguredBaseModel):
    """
    A radiocarbon date measurement with associated metadata.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/MIxS-MInAS/miaard"}
    )

    lab_id: str = Field(
        default=...,
        title="Laboratory Identifier of Date Measurement",
        description="""The unique identifier assigned to the radiocarbon date by the laboratory that performed the measurement including the lab specific suffix.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "A 0034"},
                    {"value": "AA 12345"},
                    {"value": "Beta 987654"},
                    {"value": "CN-XX 1234"},
                ],
                "slot_uri": "c14:000001",
            }
        },
    )
    conventional_age: int = Field(
        default=...,
        title="Conventional Radiocarbon Age",
        description="""The conventional radiocarbon age in years BP (Before Present, where Present is defined as AD 1950) as calculated by the laboratory.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "4500"}, {"value": "12345"}],
                "slot_uri": "c14:000002",
            }
        },
    )

    @field_validator("lab_id")
    def pattern_lab_id(cls, v):
        pattern = re.compile(r"^[A-Za-z-]+ [0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid lab_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid lab_id format: {v}"
            raise ValueError(err_msg)
        return v


class RadiocarbonDateCollection(ConfiguredBaseModel):
    """
    A collection of radiocarbon dates measurement with associated metadata.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/MIxS-MInAS/miaard", "tree_root": True}
    )

    entries: Optional[list[RadiocarbonDate]] = Field(
        default=[],
        json_schema_extra={"linkml_meta": {"domain_of": ["RadiocarbonDateCollection"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RadiocarbonDate.model_rebuild()
RadiocarbonDateCollection.model_rebuild()
