# Auto generated from c14.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T08:29:56
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

    lab_id: str = None
    conventional_age: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lab_id):
            self.MissingRequiredField("lab_id")
        if not isinstance(self.lab_id, str):
            self.lab_id = str(self.lab_id)

        if self._is_empty(self.conventional_age):
            self.MissingRequiredField("conventional_age")
        if not isinstance(self.conventional_age, int):
            self.conventional_age = int(self.conventional_age)

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


slots.lab_id = Slot(
    uri=C14["000001"],
    name="lab_id",
    curie=C14.curie("000001"),
    model_uri=C14.lab_id,
    domain=None,
    range=str,
    pattern=re.compile(r"^[A-Za-z-]+ [0-9]+$"),
)

slots.conventional_age = Slot(
    uri=C14["000002"],
    name="conventional_age",
    curie=C14.curie("000002"),
    model_uri=C14.conventional_age,
    domain=None,
    range=int,
)

slots.new_term_03 = Slot(
    uri=C14["000003"],
    name="new_term_03",
    curie=C14.curie("000003"),
    model_uri=C14.new_term_03,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_04 = Slot(
    uri=C14["000004"],
    name="new_term_04",
    curie=C14.curie("000004"),
    model_uri=C14.new_term_04,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_05 = Slot(
    uri=C14["000005"],
    name="new_term_05",
    curie=C14.curie("000005"),
    model_uri=C14.new_term_05,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_06 = Slot(
    uri=C14["000006"],
    name="new_term_06",
    curie=C14.curie("000006"),
    model_uri=C14.new_term_06,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_07 = Slot(
    uri=C14["000007"],
    name="new_term_07",
    curie=C14.curie("000007"),
    model_uri=C14.new_term_07,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_08 = Slot(
    uri=C14["000008"],
    name="new_term_08",
    curie=C14.curie("000008"),
    model_uri=C14.new_term_08,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_09 = Slot(
    uri=C14["000009"],
    name="new_term_09",
    curie=C14.curie("000009"),
    model_uri=C14.new_term_09,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_10 = Slot(
    uri=C14["000010"],
    name="new_term_10",
    curie=C14.curie("000010"),
    model_uri=C14.new_term_10,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_11 = Slot(
    uri=C14["000011"],
    name="new_term_11",
    curie=C14.curie("000011"),
    model_uri=C14.new_term_11,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_12 = Slot(
    uri=C14["000012"],
    name="new_term_12",
    curie=C14.curie("000012"),
    model_uri=C14.new_term_12,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_13 = Slot(
    uri=C14["000013"],
    name="new_term_13",
    curie=C14.curie("000013"),
    model_uri=C14.new_term_13,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_14 = Slot(
    uri=C14["000014"],
    name="new_term_14",
    curie=C14.curie("000014"),
    model_uri=C14.new_term_14,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_15 = Slot(
    uri=C14["000015"],
    name="new_term_15",
    curie=C14.curie("000015"),
    model_uri=C14.new_term_15,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_16 = Slot(
    uri=C14["000016"],
    name="new_term_16",
    curie=C14.curie("000016"),
    model_uri=C14.new_term_16,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_17 = Slot(
    uri=C14["000017"],
    name="new_term_17",
    curie=C14.curie("000017"),
    model_uri=C14.new_term_17,
    domain=None,
    range=Union[int, list[int]],
)

slots.new_term_18 = Slot(
    uri=C14["000018"],
    name="new_term_18",
    curie=C14.curie("000018"),
    model_uri=C14.new_term_18,
    domain=None,
    range=Union[int, list[int]],
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
