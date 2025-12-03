# Auto generated from c14.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-02T15:15:20
# Schema: miaard
#
# id: https://w3id.org/MIxS-MInAS/miaard
# description: Minimum Information about any Radiocarbon Date
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
    A radiocarbon date measurement with associated metadata.
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
    A collection of radiocarbon dates measurement with associated metadata.
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
