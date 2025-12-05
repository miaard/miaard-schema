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
        "description": "Minimum Information about any Radiocarbon Determination",
        "id": "https://w3id.org/MIxS-MInAS/miaard",
        "imports": ["linkml:types"],
        "license": "MIT",
        "name": "miaard",
        "prefixes": {
            "c14": {
                "prefix_prefix": "c14",
                "prefix_reference": "https://w3id.org/MIxS-MInAS/miaard/",
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
    A radiocarbon determination with associated metadata.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/MIxS-MInAS/miaard"}
    )

    c14_lab_code: str = Field(
        default=...,
        title="Laboratory code designation",
        description="""Unique laboratory code designation of the institution that made the measurement.
This is the prefix used for each determination ID. The prefix should be
derived from: https://radiocarbon.webhost.uits.arizona.edu/laboratories.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "OxA"},
                    {"value": "CAMS"},
                    {"value": "Beta"},
                    {"value": "CN-XX"},
                ],
                "recommended": True,
                "slot_uri": "c14:000001",
            }
        },
    )
    c14_f14c: float = Field(
        default=...,
        description="""The F14C value from the laboratory measurement, i.e. the fraction modern carbon.
For older determinations, generally equivalent to \"percent modern\" (pMC, or pM) divided by 100.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.83756"}, {"value": "0.5371"}],
                "recommended": True,
                "slot_uri": "c14:000004",
            }
        },
    )
    c14_f14c_error: float = Field(
        default=...,
        title="F14C radiocarbon error",
        description="""The 1-sigma uncertainty around the F14C (C14) measurement,
normally indicated as a ± after the main value. Must be in the same format.
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.00434"}, {"value": "0.023843"}],
                "recommended": True,
                "slot_uri": "c14:000005",
            }
        },
    )
    c14_conventional_age: float = Field(
        default=...,
        title="Conventional radiocarbon age",
        description="""The uncalibrated age from the laboratory measurement. Also known as the
conventional radiocarbon age (CRA). Should be a conventional 14C age (i.e., BP) NOT in AD/BC format.
This is typically the 'raw' age reported by the radiocarbon lab, in Before Present (BP) notation.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "4500"}, {"value": "12345"}],
                "recommended": True,
                "slot_uri": "c14:000002",
            }
        },
    )
    c14_conventional_age_error: str = Field(
        default=...,
        title="Conventional radiocarbon age error",
        description="""The 1-sigma uncertainty around the conventional radiocarbon age (C14) measurement,
normally indicated as a ± after the main age. Must be in the same format (i.e. BP).
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "25"}, {"value": "300"}],
                "slot_uri": "c14:000006",
            }
        },
    )
    sample_material: str = Field(
        default=...,
        title="Radiocarbon dating sample material",
        description="""Material of the sample used to extract carbon used for radiocarbon dating measurements.
Use ontology terms where possible, e.g. from UBERON for anatomical parts, or ENVO for other
organic samples.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": ""}, {"value": ""}],
                "recommended": True,
                "slot_uri": "c14:000007",
            }
        },
    )
    sample_taxon_id: list[int] = Field(
        default=...,
        title="Radiocarbon dating sample taxon",
        description="""A taxonomic ID of the organism from which the sample used to extract carbon used for
radiocarbon measurement originated. The taxonomic ID should come from an established
ontology or database.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": ""}, {"value": ""}],
                "recommended": True,
                "slot_uri": "c14:000008",
            }
        },
    )
    sample_taxon_id_confidence: Optional[bool] = Field(
        default=None,
        title="Confidence of taxon assignment",
        description="""Specify the level of confidence of an exact taxon identification.
If secure identification, indicate TRUE, if identification is unclear or
uncertain specify FALSE.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "True"}, {"value": "False"}],
                "recommended": False,
                "slot_uri": "c14:000009",
            }
        },
    )
    sample_taxon_scientific_name: Optional[int] = Field(
        default=None,
        title="Scientific name of the sample taxon",
        description="""A scientific name of the taxon corresponding to the taxonomic ID, or when a
taxonomic ID does not currently exist for the specific taxon.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "Mammathus primigenius"},
                    {"value": "cf Mammathus"},
                ],
                "recommended": True,
                "slot_uri": "c14:000010",
            }
        },
    )
    pretreatment_methods: list[str] = Field(
        default=...,
        title="Radiocarbon pretreatment methods",
        description="""Specify the types of general pretreatment methods applied for decontamination.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "ABA"},
                    {"value": "A"},
                    {"value": "BABA"},
                    {"value": "Gelatinsation"},
                    {"value": "Ultrafiltration"},
                    {"value": "XAD"},
                    {"value": "None"},
                    {"value": "Unknown"},
                ],
                "recommended": True,
                "slot_uri": "c14:000012",
            }
        },
    )
    pretreatment_method_description: str = Field(
        default=...,
        title="Radiocarbon pretreatment method description",
        description="""Description of specific pretreatment method used for decontamination of sample prior determination.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": ""}, {"value": ""}],
                "recommended": True,
                "slot_uri": "c14:000013",
            }
        },
    )
    pretreatment_method_protocol: list[str] = Field(
        default=...,
        title="Radiocarbon pretreatment method protocol",
        description="""A DOI or URL to a publication describing the specific method of pretreatment applied.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": ""}, {"value": ""}],
                "slot_uri": "c14:000014",
            }
        },
    )
    measurement_method: str = Field(
        default=...,
        title="Radiocarbon measurement method",
        description="""Type of measurement method the determination was made by.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "AMS"},
                    {"value": "Conventional"},
                    {"value": "PIMS"},
                ],
                "recommended": True,
                "slot_uri": "c14:000015",
            }
        },
    )

    @field_validator("c14_lab_code")
    def pattern_c14_lab_code(cls, v):
        pattern = re.compile(r"^[A-Za-z-]+-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid c14_lab_code format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid c14_lab_code format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("c14_f14c")
    def pattern_c14_f14c(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid c14_f14c format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid c14_f14c format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("c14_f14c_error")
    def pattern_c14_f14c_error(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid c14_f14c_error format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid c14_f14c_error format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("c14_conventional_age_error")
    def pattern_c14_conventional_age_error(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid c14_conventional_age_error format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid c14_conventional_age_error format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_material")
    def pattern_sample_material(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_material format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_material format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_taxon_id")
    def pattern_sample_taxon_id(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_taxon_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_taxon_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_taxon_id_confidence")
    def pattern_sample_taxon_id_confidence(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_taxon_id_confidence format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_taxon_id_confidence format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_taxon_scientific_name")
    def pattern_sample_taxon_scientific_name(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_taxon_scientific_name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_taxon_scientific_name format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("pretreatment_methods")
    def pattern_pretreatment_methods(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pretreatment_methods format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pretreatment_methods format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("pretreatment_method_description")
    def pattern_pretreatment_method_description(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = (
                        f"Invalid pretreatment_method_description format: {element}"
                    )
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pretreatment_method_description format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("pretreatment_method_protocol")
    def pattern_pretreatment_method_protocol(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pretreatment_method_protocol format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pretreatment_method_protocol format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("measurement_method")
    def pattern_measurement_method(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid measurement_method format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid measurement_method format: {v}"
            raise ValueError(err_msg)
        return v


class RadiocarbonDateCollection(ConfiguredBaseModel):
    """
    A collection of radiocarbon determinations with associated metadata.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/MIxS-MInAS/miaard", "tree_root": True}
    )

    entries: Optional[list[RadiocarbonDate]] = Field(
        default=[],
        description="""A list of multiple radiocarbon determinations.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RadiocarbonDateCollection"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RadiocarbonDate.model_rebuild()
RadiocarbonDateCollection.model_rebuild()
