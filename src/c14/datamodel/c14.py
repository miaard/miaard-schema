# Auto generated from c14.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T08:58:00
# Schema: miaard
#
# id: https://w3id.org/MIxS-MInAS/miaard
# description: Minimum Information about any Radiocarbon Determination
# license: MIT

import re
from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
C14 = CurieNamespace("c14", "https://w3id.org/MIxS-MInAS/miaard/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
DEFAULT_ = C14


# Types

# Class references


@dataclass(repr=False)
class RadiocarbonDate(YAMLRoot):
    """
    A radiocarbon determination with associated metadata.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["RadiocarbonDate"]
    class_class_curie: ClassVar[str] = "c14:RadiocarbonDate"
    class_name: ClassVar[str] = "RadiocarbonDate"
    class_model_uri: ClassVar[URIRef] = C14.RadiocarbonDate

    c14_lab_code: str = None
    c14_f14c: float = None
    c14_f14c_error: float = None
    c14_conventional_age: float = None
    c14_conventional_age_error: str = None
    sample_material: str = None
    sample_taxon_id: Union[int, list[int]] = None
    pretreatment_methods: Union[str, list[str]] = None
    pretreatment_method_description: str = None
    pretreatment_method_protocol: Union[str, list[str]] = None
    measurement_method: str = None
    sample_taxon_id_confidence: Optional[Union[bool, Bool]] = None
    sample_taxon_scientific_name: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.c14_lab_code):
            self.MissingRequiredField("c14_lab_code")
        if not isinstance(self.c14_lab_code, str):
            self.c14_lab_code = str(self.c14_lab_code)

        if self._is_empty(self.c14_lab_code):
            self.MissingRequiredField("c14_lab_code")
        if not isinstance(self.c14_lab_code, str):
            self.c14_lab_code = str(self.c14_lab_code)

        if self._is_empty(self.c14_f14c):
            self.MissingRequiredField("c14_f14c")
        if not isinstance(self.c14_f14c, float):
            self.c14_f14c = float(self.c14_f14c)

        if self._is_empty(self.c14_f14c_error):
            self.MissingRequiredField("c14_f14c_error")
        if not isinstance(self.c14_f14c_error, float):
            self.c14_f14c_error = float(self.c14_f14c_error)

        if self._is_empty(self.c14_conventional_age):
            self.MissingRequiredField("c14_conventional_age")
        if not isinstance(self.c14_conventional_age, float):
            self.c14_conventional_age = float(self.c14_conventional_age)

        if self._is_empty(self.c14_conventional_age_error):
            self.MissingRequiredField("c14_conventional_age_error")
        if not isinstance(self.c14_conventional_age_error, str):
            self.c14_conventional_age_error = str(self.c14_conventional_age_error)

        if self._is_empty(self.sample_material):
            self.MissingRequiredField("sample_material")
        if not isinstance(self.sample_material, str):
            self.sample_material = str(self.sample_material)

        if self._is_empty(self.sample_taxon_id):
            self.MissingRequiredField("sample_taxon_id")
        if not isinstance(self.sample_taxon_id, list):
            self.sample_taxon_id = (
                [self.sample_taxon_id] if self.sample_taxon_id is not None else []
            )
        self.sample_taxon_id = [
            v if isinstance(v, int) else int(v) for v in self.sample_taxon_id
        ]

        if self._is_empty(self.pretreatment_methods):
            self.MissingRequiredField("pretreatment_methods")
        if not isinstance(self.pretreatment_methods, list):
            self.pretreatment_methods = (
                [self.pretreatment_methods]
                if self.pretreatment_methods is not None
                else []
            )
        self.pretreatment_methods = [
            v if isinstance(v, str) else str(v) for v in self.pretreatment_methods
        ]

        if self._is_empty(self.pretreatment_method_description):
            self.MissingRequiredField("pretreatment_method_description")
        if not isinstance(self.pretreatment_method_description, str):
            self.pretreatment_method_description = str(
                self.pretreatment_method_description
            )

        if self._is_empty(self.pretreatment_method_protocol):
            self.MissingRequiredField("pretreatment_method_protocol")
        if not isinstance(self.pretreatment_method_protocol, list):
            self.pretreatment_method_protocol = (
                [self.pretreatment_method_protocol]
                if self.pretreatment_method_protocol is not None
                else []
            )
        self.pretreatment_method_protocol = [
            v if isinstance(v, str) else str(v)
            for v in self.pretreatment_method_protocol
        ]

        if self._is_empty(self.measurement_method):
            self.MissingRequiredField("measurement_method")
        if not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.sample_taxon_id_confidence is not None and not isinstance(
            self.sample_taxon_id_confidence, Bool
        ):
            self.sample_taxon_id_confidence = Bool(self.sample_taxon_id_confidence)

        if self.sample_taxon_scientific_name is not None and not isinstance(
            self.sample_taxon_scientific_name, int
        ):
            self.sample_taxon_scientific_name = int(self.sample_taxon_scientific_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RadiocarbonDateCollection(YAMLRoot):
    """
    A collection of radiocarbon determinations with associated metadata.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["RadiocarbonDateCollection"]
    class_class_curie: ClassVar[str] = "c14:RadiocarbonDateCollection"
    class_name: ClassVar[str] = "RadiocarbonDateCollection"
    class_model_uri: ClassVar[URIRef] = C14.RadiocarbonDateCollection

    entries: Optional[
        Union[Union[dict, RadiocarbonDate], list[Union[dict, RadiocarbonDate]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [
            v if isinstance(v, RadiocarbonDate) else RadiocarbonDate(**as_dict(v))
            for v in self.entries
        ]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass


slots.c14_lab_code = Slot(
    uri=C14["000001"],
    name="c14_lab_code",
    curie=C14.curie("000001"),
    model_uri=C14.c14_lab_code,
    domain=None,
    range=str,
    pattern=re.compile(r"^[A-Za-z-]+-[0-9]+$"),
)

slots.c14_determination_id = Slot(
    uri=C14["000003"],
    name="c14_determination_id",
    curie=C14.curie("000003"),
    model_uri=C14.c14_determination_id,
    domain=None,
    range=str,
)

slots.c14_f14c = Slot(
    uri=C14["000004"],
    name="c14_f14c",
    curie=C14.curie("000004"),
    model_uri=C14.c14_f14c,
    domain=None,
    range=float,
)

slots.c14_f14c_error = Slot(
    uri=C14["000005"],
    name="c14_f14c_error",
    curie=C14.curie("000005"),
    model_uri=C14.c14_f14c_error,
    domain=None,
    range=float,
)

slots.c14_conventional_age = Slot(
    uri=C14["000002"],
    name="c14_conventional_age",
    curie=C14.curie("000002"),
    model_uri=C14.c14_conventional_age,
    domain=None,
    range=float,
)

slots.c14_conventional_age_error = Slot(
    uri=C14["000006"],
    name="c14_conventional_age_error",
    curie=C14.curie("000006"),
    model_uri=C14.c14_conventional_age_error,
    domain=None,
    range=str,
)

slots.sample_material = Slot(
    uri=C14["000007"],
    name="sample_material",
    curie=C14.curie("000007"),
    model_uri=C14.sample_material,
    domain=None,
    range=str,
)

slots.sample_taxon_id = Slot(
    uri=C14["000008"],
    name="sample_taxon_id",
    curie=C14.curie("000008"),
    model_uri=C14.sample_taxon_id,
    domain=None,
    range=Union[int, list[int]],
)

slots.sample_taxon_id_confidence = Slot(
    uri=C14["000009"],
    name="sample_taxon_id_confidence",
    curie=C14.curie("000009"),
    model_uri=C14.sample_taxon_id_confidence,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.sample_taxon_scientific_name = Slot(
    uri=C14["000010"],
    name="sample_taxon_scientific_name",
    curie=C14.curie("000010"),
    model_uri=C14.sample_taxon_scientific_name,
    domain=None,
    range=Optional[int],
)

slots.sample_anatomical_part = Slot(
    uri=C14["000011"],
    name="sample_anatomical_part",
    curie=C14.curie("000011"),
    model_uri=C14.sample_anatomical_part,
    domain=None,
    range=Optional[str],
)

slots.pretreatment_methods = Slot(
    uri=C14["000012"],
    name="pretreatment_methods",
    curie=C14.curie("000012"),
    model_uri=C14.pretreatment_methods,
    domain=None,
    range=Union[str, list[str]],
)

slots.pretreatment_method_description = Slot(
    uri=C14["000013"],
    name="pretreatment_method_description",
    curie=C14.curie("000013"),
    model_uri=C14.pretreatment_method_description,
    domain=None,
    range=str,
)

slots.pretreatment_method_protocol = Slot(
    uri=C14["000014"],
    name="pretreatment_method_protocol",
    curie=C14.curie("000014"),
    model_uri=C14.pretreatment_method_protocol,
    domain=None,
    range=Union[str, list[str]],
)

slots.measurement_method = Slot(
    uri=C14["000015"],
    name="measurement_method",
    curie=C14.curie("000015"),
    model_uri=C14.measurement_method,
    domain=None,
    range=str,
)

slots.sample_starting_weight = Slot(
    uri=C14["000016"],
    name="sample_starting_weight",
    curie=C14.curie("000016"),
    model_uri=C14.sample_starting_weight,
    domain=None,
    range=Optional[float],
)

slots.pretreatment_yield = Slot(
    uri=C14["000017"],
    name="pretreatment_yield",
    curie=C14.curie("000017"),
    model_uri=C14.pretreatment_yield,
    domain=None,
    range=float,
)

slots.pretreatment_percentage_yield = Slot(
    uri=C14["000017"],
    name="pretreatment_percentage_yield",
    curie=C14.curie("000017"),
    model_uri=C14.pretreatment_percentage_yield,
    domain=None,
    range=float,
)

slots.carbon_perc = Slot(
    uri=C14["000018"],
    name="carbon_perc",
    curie=C14.curie("000018"),
    model_uri=C14.carbon_perc,
    domain=None,
    range=float,
)

slots.delta_13_c = Slot(
    uri=C14["000019"],
    name="delta_13_c",
    curie=C14.curie("000019"),
    model_uri=C14.delta_13_c,
    domain=None,
    range=float,
)

slots.delta_13_c_error = Slot(
    uri=C14["000020"],
    name="delta_13_c_error",
    curie=C14.curie("000020"),
    model_uri=C14.delta_13_c_error,
    domain=None,
    range=float,
)

slots.delta_13_c_method = Slot(
    uri=C14["000020"],
    name="delta_13_c_method",
    curie=C14.curie("000020"),
    model_uri=C14.delta_13_c_method,
    domain=None,
    range=str,
)

slots.radiocarbonDateCollection__entries = Slot(
    uri=C14.entries,
    name="radiocarbonDateCollection__entries",
    curie=C14.curie("entries"),
    model_uri=C14.radiocarbonDateCollection__entries,
    domain=None,
    range=Optional[
        Union[Union[dict, RadiocarbonDate], list[Union[dict, RadiocarbonDate]]]
    ],
)
