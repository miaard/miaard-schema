# Auto generated from c14.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-14T17:25:43
# Schema: miaard
#
# id: https://w3id.org/miaard/miaard-schema
# description: Minimum Information about any Radiocarbon Determination
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
C14 = CurieNamespace('c14', 'https://w3id.org/miaard/miaard-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
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

    lab_code: Union[str, "LabCode"] = None
    lab_id: str = None
    conventional_age: float = None
    conventional_age_error: float = None
    f14c: float = None
    f14c_error: float = None
    sample_ids: Union[str, list[str]] = None
    sample_material: str = None
    sample_taxon_id: Union[str, list[str]] = None
    sample_taxon_id_confidence: Union[bool, Bool] = None
    pretreatment_methods: Union[Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]] = None
    pretreatment_method_description: str = None
    pretreatment_method_protocol: Union[str, list[str]] = None
    measurement_method: Union[str, "RadiocarbonMeasurementMethod"] = None
    sample_starting_weight: float = None
    pretreatment_yield: float = None
    carbon_proportion: float = None
    suspected_reservoir_effect: Union[bool, Bool] = None
    delta_13_c_calculation_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None
    sample_taxon_scientific_name: Optional[str] = None
    sample_anatomical_part: Optional[str] = None
    suspected_sample_contamination: Optional[Union[bool, Bool]] = None
    suspected_sample_contamination_description: Optional[str] = None
    sample_location: Optional[str] = None
    decimal_latitude: Optional[float] = None
    decimal_longitude: Optional[float] = None
    coordinate_precision: Optional[float] = None
    pretreatment_percentage_yield: Optional[float] = None
    delta_13_c: Optional[float] = None
    delta_13_c_error: Optional[float] = None
    delta_13_c_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lab_code):
            self.MissingRequiredField("lab_code")
        if not isinstance(self.lab_code, LabCode):
            self.lab_code = LabCode(self.lab_code)

        if self._is_empty(self.lab_id):
            self.MissingRequiredField("lab_id")
        if not isinstance(self.lab_id, str):
            self.lab_id = str(self.lab_id)

        if self._is_empty(self.conventional_age):
            self.MissingRequiredField("conventional_age")
        if not isinstance(self.conventional_age, float):
            self.conventional_age = float(self.conventional_age)

        if self._is_empty(self.conventional_age_error):
            self.MissingRequiredField("conventional_age_error")
        if not isinstance(self.conventional_age_error, float):
            self.conventional_age_error = float(self.conventional_age_error)

        if self._is_empty(self.f14c):
            self.MissingRequiredField("f14c")
        if not isinstance(self.f14c, float):
            self.f14c = float(self.f14c)

        if self._is_empty(self.f14c_error):
            self.MissingRequiredField("f14c_error")
        if not isinstance(self.f14c_error, float):
            self.f14c_error = float(self.f14c_error)

        if self._is_empty(self.sample_ids):
            self.MissingRequiredField("sample_ids")
        if not isinstance(self.sample_ids, list):
            self.sample_ids = [self.sample_ids] if self.sample_ids is not None else []
        self.sample_ids = [v if isinstance(v, str) else str(v) for v in self.sample_ids]

        if self._is_empty(self.sample_material):
            self.MissingRequiredField("sample_material")
        if not isinstance(self.sample_material, str):
            self.sample_material = str(self.sample_material)

        if self._is_empty(self.sample_taxon_id):
            self.MissingRequiredField("sample_taxon_id")
        if not isinstance(self.sample_taxon_id, list):
            self.sample_taxon_id = [self.sample_taxon_id] if self.sample_taxon_id is not None else []
        self.sample_taxon_id = [v if isinstance(v, str) else str(v) for v in self.sample_taxon_id]

        if self._is_empty(self.sample_taxon_id_confidence):
            self.MissingRequiredField("sample_taxon_id_confidence")
        if not isinstance(self.sample_taxon_id_confidence, Bool):
            self.sample_taxon_id_confidence = Bool(self.sample_taxon_id_confidence)

        if self._is_empty(self.pretreatment_methods):
            self.MissingRequiredField("pretreatment_methods")
        if not isinstance(self.pretreatment_methods, list):
            self.pretreatment_methods = [self.pretreatment_methods] if self.pretreatment_methods is not None else []
        self.pretreatment_methods = [v if isinstance(v, PretreatmentMethods) else PretreatmentMethods(v) for v in self.pretreatment_methods]

        if self._is_empty(self.pretreatment_method_description):
            self.MissingRequiredField("pretreatment_method_description")
        if not isinstance(self.pretreatment_method_description, str):
            self.pretreatment_method_description = str(self.pretreatment_method_description)

        if self._is_empty(self.pretreatment_method_protocol):
            self.MissingRequiredField("pretreatment_method_protocol")
        if not isinstance(self.pretreatment_method_protocol, list):
            self.pretreatment_method_protocol = [self.pretreatment_method_protocol] if self.pretreatment_method_protocol is not None else []
        self.pretreatment_method_protocol = [v if isinstance(v, str) else str(v) for v in self.pretreatment_method_protocol]

        if self._is_empty(self.measurement_method):
            self.MissingRequiredField("measurement_method")
        if not isinstance(self.measurement_method, RadiocarbonMeasurementMethod):
            self.measurement_method = RadiocarbonMeasurementMethod(self.measurement_method)

        if self._is_empty(self.sample_starting_weight):
            self.MissingRequiredField("sample_starting_weight")
        if not isinstance(self.sample_starting_weight, float):
            self.sample_starting_weight = float(self.sample_starting_weight)

        if self._is_empty(self.pretreatment_yield):
            self.MissingRequiredField("pretreatment_yield")
        if not isinstance(self.pretreatment_yield, float):
            self.pretreatment_yield = float(self.pretreatment_yield)

        if self._is_empty(self.carbon_proportion):
            self.MissingRequiredField("carbon_proportion")
        if not isinstance(self.carbon_proportion, float):
            self.carbon_proportion = float(self.carbon_proportion)

        if self._is_empty(self.suspected_reservoir_effect):
            self.MissingRequiredField("suspected_reservoir_effect")
        if not isinstance(self.suspected_reservoir_effect, Bool):
            self.suspected_reservoir_effect = Bool(self.suspected_reservoir_effect)

        if self.delta_13_c_calculation_method is not None and not isinstance(self.delta_13_c_calculation_method, Delta13CMeasurementMethod):
            self.delta_13_c_calculation_method = Delta13CMeasurementMethod(self.delta_13_c_calculation_method)

        if self.sample_taxon_scientific_name is not None and not isinstance(self.sample_taxon_scientific_name, str):
            self.sample_taxon_scientific_name = str(self.sample_taxon_scientific_name)

        if self.sample_anatomical_part is not None and not isinstance(self.sample_anatomical_part, str):
            self.sample_anatomical_part = str(self.sample_anatomical_part)

        if self.suspected_sample_contamination is not None and not isinstance(self.suspected_sample_contamination, Bool):
            self.suspected_sample_contamination = Bool(self.suspected_sample_contamination)

        if self.suspected_sample_contamination_description is not None and not isinstance(self.suspected_sample_contamination_description, str):
            self.suspected_sample_contamination_description = str(self.suspected_sample_contamination_description)

        if self.sample_location is not None and not isinstance(self.sample_location, str):
            self.sample_location = str(self.sample_location)

        if self.decimal_latitude is not None and not isinstance(self.decimal_latitude, float):
            self.decimal_latitude = float(self.decimal_latitude)

        if self.decimal_longitude is not None and not isinstance(self.decimal_longitude, float):
            self.decimal_longitude = float(self.decimal_longitude)

        if self.coordinate_precision is not None and not isinstance(self.coordinate_precision, float):
            self.coordinate_precision = float(self.coordinate_precision)

        if self.pretreatment_percentage_yield is not None and not isinstance(self.pretreatment_percentage_yield, float):
            self.pretreatment_percentage_yield = float(self.pretreatment_percentage_yield)

        if self.delta_13_c is not None and not isinstance(self.delta_13_c, float):
            self.delta_13_c = float(self.delta_13_c)

        if self.delta_13_c_error is not None and not isinstance(self.delta_13_c_error, float):
            self.delta_13_c_error = float(self.delta_13_c_error)

        if self.delta_13_c_method is not None and not isinstance(self.delta_13_c_method, Delta13CMeasurementMethod):
            self.delta_13_c_method = Delta13CMeasurementMethod(self.delta_13_c_method)

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

    entries: Optional[Union[Union[dict, RadiocarbonDate], list[Union[dict, RadiocarbonDate]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, RadiocarbonDate) else RadiocarbonDate(**as_dict(v)) for v in self.entries]

        super().__post_init__(**kwargs)


class Extension(YAMLRoot):
    """
    A collection of recommended metadata terms for a specific context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["Extension"]
    class_class_curie: ClassVar[str] = "c14:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = C14.Extension


@dataclass(repr=False)
class ProteinaceousSample(Extension):
    """
    Terms specific to proteinaceous samples being dated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["ProteinaceousSample"]
    class_class_curie: ClassVar[str] = "c14:ProteinaceousSample"
    class_name: ClassVar[str] = "ProteinaceousSample"
    class_model_uri: ClassVar[URIRef] = C14.ProteinaceousSample

    carbon_nitro_ratio: float = None
    delta_15_n: Optional[float] = None
    delta_15_n_error: Optional[float] = None
    delta_34_s: Optional[float] = None
    delta_34_s_error: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.carbon_nitro_ratio):
            self.MissingRequiredField("carbon_nitro_ratio")
        if not isinstance(self.carbon_nitro_ratio, float):
            self.carbon_nitro_ratio = float(self.carbon_nitro_ratio)

        if self.delta_15_n is not None and not isinstance(self.delta_15_n, float):
            self.delta_15_n = float(self.delta_15_n)

        if self.delta_15_n_error is not None and not isinstance(self.delta_15_n_error, float):
            self.delta_15_n_error = float(self.delta_15_n_error)

        if self.delta_34_s is not None and not isinstance(self.delta_34_s, float):
            self.delta_34_s = float(self.delta_34_s)

        if self.delta_34_s_error is not None and not isinstance(self.delta_34_s_error, float):
            self.delta_34_s_error = float(self.delta_34_s_error)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarbonateSample(Extension):
    """
    Terms specific to carbonate samples being dated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["CarbonateSample"]
    class_class_curie: ClassVar[str] = "c14:CarbonateSample"
    class_name: ClassVar[str] = "CarbonateSample"
    class_model_uri: ClassVar[URIRef] = C14.CarbonateSample

    recrystalisation: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recrystalisation):
            self.MissingRequiredField("recrystalisation")
        if not isinstance(self.recrystalisation, Bool):
            self.recrystalisation = Bool(self.recrystalisation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RadiocarbonDateProteinaceousSample(ProteinaceousSample):
    """
    A radiocarbon determination on a proteinaceous sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["RadiocarbonDateProteinaceousSample"]
    class_class_curie: ClassVar[str] = "c14:RadiocarbonDateProteinaceousSample"
    class_name: ClassVar[str] = "RadiocarbonDateProteinaceousSample"
    class_model_uri: ClassVar[URIRef] = C14.RadiocarbonDateProteinaceousSample

    carbon_nitro_ratio: float = None
    lab_code: Union[str, "LabCode"] = None
    lab_id: str = None
    conventional_age: float = None
    conventional_age_error: float = None
    f14c: float = None
    f14c_error: float = None
    sample_ids: Union[str, list[str]] = None
    sample_material: str = None
    sample_taxon_id: Union[str, list[str]] = None
    sample_taxon_id_confidence: Union[bool, Bool] = None
    pretreatment_methods: Union[Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]] = None
    pretreatment_method_description: str = None
    pretreatment_method_protocol: Union[str, list[str]] = None
    measurement_method: Union[str, "RadiocarbonMeasurementMethod"] = None
    sample_starting_weight: float = None
    pretreatment_yield: float = None
    carbon_proportion: float = None
    suspected_reservoir_effect: Union[bool, Bool] = None
    delta_13_c_calculation_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None
    sample_taxon_scientific_name: Optional[str] = None
    sample_anatomical_part: Optional[str] = None
    suspected_sample_contamination: Optional[Union[bool, Bool]] = None
    suspected_sample_contamination_description: Optional[str] = None
    sample_location: Optional[str] = None
    decimal_latitude: Optional[float] = None
    decimal_longitude: Optional[float] = None
    coordinate_precision: Optional[float] = None
    pretreatment_percentage_yield: Optional[float] = None
    delta_13_c: Optional[float] = None
    delta_13_c_error: Optional[float] = None
    delta_13_c_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lab_code):
            self.MissingRequiredField("lab_code")
        if not isinstance(self.lab_code, LabCode):
            self.lab_code = LabCode(self.lab_code)

        if self._is_empty(self.lab_id):
            self.MissingRequiredField("lab_id")
        if not isinstance(self.lab_id, str):
            self.lab_id = str(self.lab_id)

        if self._is_empty(self.conventional_age):
            self.MissingRequiredField("conventional_age")
        if not isinstance(self.conventional_age, float):
            self.conventional_age = float(self.conventional_age)

        if self._is_empty(self.conventional_age_error):
            self.MissingRequiredField("conventional_age_error")
        if not isinstance(self.conventional_age_error, float):
            self.conventional_age_error = float(self.conventional_age_error)

        if self._is_empty(self.f14c):
            self.MissingRequiredField("f14c")
        if not isinstance(self.f14c, float):
            self.f14c = float(self.f14c)

        if self._is_empty(self.f14c_error):
            self.MissingRequiredField("f14c_error")
        if not isinstance(self.f14c_error, float):
            self.f14c_error = float(self.f14c_error)

        if self._is_empty(self.sample_ids):
            self.MissingRequiredField("sample_ids")
        if not isinstance(self.sample_ids, list):
            self.sample_ids = [self.sample_ids] if self.sample_ids is not None else []
        self.sample_ids = [v if isinstance(v, str) else str(v) for v in self.sample_ids]

        if self._is_empty(self.sample_material):
            self.MissingRequiredField("sample_material")
        if not isinstance(self.sample_material, str):
            self.sample_material = str(self.sample_material)

        if self._is_empty(self.sample_taxon_id):
            self.MissingRequiredField("sample_taxon_id")
        if not isinstance(self.sample_taxon_id, list):
            self.sample_taxon_id = [self.sample_taxon_id] if self.sample_taxon_id is not None else []
        self.sample_taxon_id = [v if isinstance(v, str) else str(v) for v in self.sample_taxon_id]

        if self._is_empty(self.sample_taxon_id_confidence):
            self.MissingRequiredField("sample_taxon_id_confidence")
        if not isinstance(self.sample_taxon_id_confidence, Bool):
            self.sample_taxon_id_confidence = Bool(self.sample_taxon_id_confidence)

        if self._is_empty(self.pretreatment_methods):
            self.MissingRequiredField("pretreatment_methods")
        if not isinstance(self.pretreatment_methods, list):
            self.pretreatment_methods = [self.pretreatment_methods] if self.pretreatment_methods is not None else []
        self.pretreatment_methods = [v if isinstance(v, PretreatmentMethods) else PretreatmentMethods(v) for v in self.pretreatment_methods]

        if self._is_empty(self.pretreatment_method_description):
            self.MissingRequiredField("pretreatment_method_description")
        if not isinstance(self.pretreatment_method_description, str):
            self.pretreatment_method_description = str(self.pretreatment_method_description)

        if self._is_empty(self.pretreatment_method_protocol):
            self.MissingRequiredField("pretreatment_method_protocol")
        if not isinstance(self.pretreatment_method_protocol, list):
            self.pretreatment_method_protocol = [self.pretreatment_method_protocol] if self.pretreatment_method_protocol is not None else []
        self.pretreatment_method_protocol = [v if isinstance(v, str) else str(v) for v in self.pretreatment_method_protocol]

        if self._is_empty(self.measurement_method):
            self.MissingRequiredField("measurement_method")
        if not isinstance(self.measurement_method, RadiocarbonMeasurementMethod):
            self.measurement_method = RadiocarbonMeasurementMethod(self.measurement_method)

        if self._is_empty(self.sample_starting_weight):
            self.MissingRequiredField("sample_starting_weight")
        if not isinstance(self.sample_starting_weight, float):
            self.sample_starting_weight = float(self.sample_starting_weight)

        if self._is_empty(self.pretreatment_yield):
            self.MissingRequiredField("pretreatment_yield")
        if not isinstance(self.pretreatment_yield, float):
            self.pretreatment_yield = float(self.pretreatment_yield)

        if self._is_empty(self.carbon_proportion):
            self.MissingRequiredField("carbon_proportion")
        if not isinstance(self.carbon_proportion, float):
            self.carbon_proportion = float(self.carbon_proportion)

        if self._is_empty(self.suspected_reservoir_effect):
            self.MissingRequiredField("suspected_reservoir_effect")
        if not isinstance(self.suspected_reservoir_effect, Bool):
            self.suspected_reservoir_effect = Bool(self.suspected_reservoir_effect)

        if self.delta_13_c_calculation_method is not None and not isinstance(self.delta_13_c_calculation_method, Delta13CMeasurementMethod):
            self.delta_13_c_calculation_method = Delta13CMeasurementMethod(self.delta_13_c_calculation_method)

        if self.sample_taxon_scientific_name is not None and not isinstance(self.sample_taxon_scientific_name, str):
            self.sample_taxon_scientific_name = str(self.sample_taxon_scientific_name)

        if self.sample_anatomical_part is not None and not isinstance(self.sample_anatomical_part, str):
            self.sample_anatomical_part = str(self.sample_anatomical_part)

        if self.suspected_sample_contamination is not None and not isinstance(self.suspected_sample_contamination, Bool):
            self.suspected_sample_contamination = Bool(self.suspected_sample_contamination)

        if self.suspected_sample_contamination_description is not None and not isinstance(self.suspected_sample_contamination_description, str):
            self.suspected_sample_contamination_description = str(self.suspected_sample_contamination_description)

        if self.sample_location is not None and not isinstance(self.sample_location, str):
            self.sample_location = str(self.sample_location)

        if self.decimal_latitude is not None and not isinstance(self.decimal_latitude, float):
            self.decimal_latitude = float(self.decimal_latitude)

        if self.decimal_longitude is not None and not isinstance(self.decimal_longitude, float):
            self.decimal_longitude = float(self.decimal_longitude)

        if self.coordinate_precision is not None and not isinstance(self.coordinate_precision, float):
            self.coordinate_precision = float(self.coordinate_precision)

        if self.pretreatment_percentage_yield is not None and not isinstance(self.pretreatment_percentage_yield, float):
            self.pretreatment_percentage_yield = float(self.pretreatment_percentage_yield)

        if self.delta_13_c is not None and not isinstance(self.delta_13_c, float):
            self.delta_13_c = float(self.delta_13_c)

        if self.delta_13_c_error is not None and not isinstance(self.delta_13_c_error, float):
            self.delta_13_c_error = float(self.delta_13_c_error)

        if self.delta_13_c_method is not None and not isinstance(self.delta_13_c_method, Delta13CMeasurementMethod):
            self.delta_13_c_method = Delta13CMeasurementMethod(self.delta_13_c_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RadiocarbonDateCarbonateSample(CarbonateSample):
    """
    A radiocarbon determination on a carbonate sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = C14["RadiocarbonDateCarbonateSample"]
    class_class_curie: ClassVar[str] = "c14:RadiocarbonDateCarbonateSample"
    class_name: ClassVar[str] = "RadiocarbonDateCarbonateSample"
    class_model_uri: ClassVar[URIRef] = C14.RadiocarbonDateCarbonateSample

    recrystalisation: Union[bool, Bool] = None
    lab_code: Union[str, "LabCode"] = None
    lab_id: str = None
    conventional_age: float = None
    conventional_age_error: float = None
    f14c: float = None
    f14c_error: float = None
    sample_ids: Union[str, list[str]] = None
    sample_material: str = None
    sample_taxon_id: Union[str, list[str]] = None
    sample_taxon_id_confidence: Union[bool, Bool] = None
    pretreatment_methods: Union[Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]] = None
    pretreatment_method_description: str = None
    pretreatment_method_protocol: Union[str, list[str]] = None
    measurement_method: Union[str, "RadiocarbonMeasurementMethod"] = None
    sample_starting_weight: float = None
    pretreatment_yield: float = None
    carbon_proportion: float = None
    suspected_reservoir_effect: Union[bool, Bool] = None
    delta_13_c_calculation_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None
    sample_taxon_scientific_name: Optional[str] = None
    sample_anatomical_part: Optional[str] = None
    suspected_sample_contamination: Optional[Union[bool, Bool]] = None
    suspected_sample_contamination_description: Optional[str] = None
    sample_location: Optional[str] = None
    decimal_latitude: Optional[float] = None
    decimal_longitude: Optional[float] = None
    coordinate_precision: Optional[float] = None
    pretreatment_percentage_yield: Optional[float] = None
    delta_13_c: Optional[float] = None
    delta_13_c_error: Optional[float] = None
    delta_13_c_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lab_code):
            self.MissingRequiredField("lab_code")
        if not isinstance(self.lab_code, LabCode):
            self.lab_code = LabCode(self.lab_code)

        if self._is_empty(self.lab_id):
            self.MissingRequiredField("lab_id")
        if not isinstance(self.lab_id, str):
            self.lab_id = str(self.lab_id)

        if self._is_empty(self.conventional_age):
            self.MissingRequiredField("conventional_age")
        if not isinstance(self.conventional_age, float):
            self.conventional_age = float(self.conventional_age)

        if self._is_empty(self.conventional_age_error):
            self.MissingRequiredField("conventional_age_error")
        if not isinstance(self.conventional_age_error, float):
            self.conventional_age_error = float(self.conventional_age_error)

        if self._is_empty(self.f14c):
            self.MissingRequiredField("f14c")
        if not isinstance(self.f14c, float):
            self.f14c = float(self.f14c)

        if self._is_empty(self.f14c_error):
            self.MissingRequiredField("f14c_error")
        if not isinstance(self.f14c_error, float):
            self.f14c_error = float(self.f14c_error)

        if self._is_empty(self.sample_ids):
            self.MissingRequiredField("sample_ids")
        if not isinstance(self.sample_ids, list):
            self.sample_ids = [self.sample_ids] if self.sample_ids is not None else []
        self.sample_ids = [v if isinstance(v, str) else str(v) for v in self.sample_ids]

        if self._is_empty(self.sample_material):
            self.MissingRequiredField("sample_material")
        if not isinstance(self.sample_material, str):
            self.sample_material = str(self.sample_material)

        if self._is_empty(self.sample_taxon_id):
            self.MissingRequiredField("sample_taxon_id")
        if not isinstance(self.sample_taxon_id, list):
            self.sample_taxon_id = [self.sample_taxon_id] if self.sample_taxon_id is not None else []
        self.sample_taxon_id = [v if isinstance(v, str) else str(v) for v in self.sample_taxon_id]

        if self._is_empty(self.sample_taxon_id_confidence):
            self.MissingRequiredField("sample_taxon_id_confidence")
        if not isinstance(self.sample_taxon_id_confidence, Bool):
            self.sample_taxon_id_confidence = Bool(self.sample_taxon_id_confidence)

        if self._is_empty(self.pretreatment_methods):
            self.MissingRequiredField("pretreatment_methods")
        if not isinstance(self.pretreatment_methods, list):
            self.pretreatment_methods = [self.pretreatment_methods] if self.pretreatment_methods is not None else []
        self.pretreatment_methods = [v if isinstance(v, PretreatmentMethods) else PretreatmentMethods(v) for v in self.pretreatment_methods]

        if self._is_empty(self.pretreatment_method_description):
            self.MissingRequiredField("pretreatment_method_description")
        if not isinstance(self.pretreatment_method_description, str):
            self.pretreatment_method_description = str(self.pretreatment_method_description)

        if self._is_empty(self.pretreatment_method_protocol):
            self.MissingRequiredField("pretreatment_method_protocol")
        if not isinstance(self.pretreatment_method_protocol, list):
            self.pretreatment_method_protocol = [self.pretreatment_method_protocol] if self.pretreatment_method_protocol is not None else []
        self.pretreatment_method_protocol = [v if isinstance(v, str) else str(v) for v in self.pretreatment_method_protocol]

        if self._is_empty(self.measurement_method):
            self.MissingRequiredField("measurement_method")
        if not isinstance(self.measurement_method, RadiocarbonMeasurementMethod):
            self.measurement_method = RadiocarbonMeasurementMethod(self.measurement_method)

        if self._is_empty(self.sample_starting_weight):
            self.MissingRequiredField("sample_starting_weight")
        if not isinstance(self.sample_starting_weight, float):
            self.sample_starting_weight = float(self.sample_starting_weight)

        if self._is_empty(self.pretreatment_yield):
            self.MissingRequiredField("pretreatment_yield")
        if not isinstance(self.pretreatment_yield, float):
            self.pretreatment_yield = float(self.pretreatment_yield)

        if self._is_empty(self.carbon_proportion):
            self.MissingRequiredField("carbon_proportion")
        if not isinstance(self.carbon_proportion, float):
            self.carbon_proportion = float(self.carbon_proportion)

        if self._is_empty(self.suspected_reservoir_effect):
            self.MissingRequiredField("suspected_reservoir_effect")
        if not isinstance(self.suspected_reservoir_effect, Bool):
            self.suspected_reservoir_effect = Bool(self.suspected_reservoir_effect)

        if self.delta_13_c_calculation_method is not None and not isinstance(self.delta_13_c_calculation_method, Delta13CMeasurementMethod):
            self.delta_13_c_calculation_method = Delta13CMeasurementMethod(self.delta_13_c_calculation_method)

        if self.sample_taxon_scientific_name is not None and not isinstance(self.sample_taxon_scientific_name, str):
            self.sample_taxon_scientific_name = str(self.sample_taxon_scientific_name)

        if self.sample_anatomical_part is not None and not isinstance(self.sample_anatomical_part, str):
            self.sample_anatomical_part = str(self.sample_anatomical_part)

        if self.suspected_sample_contamination is not None and not isinstance(self.suspected_sample_contamination, Bool):
            self.suspected_sample_contamination = Bool(self.suspected_sample_contamination)

        if self.suspected_sample_contamination_description is not None and not isinstance(self.suspected_sample_contamination_description, str):
            self.suspected_sample_contamination_description = str(self.suspected_sample_contamination_description)

        if self.sample_location is not None and not isinstance(self.sample_location, str):
            self.sample_location = str(self.sample_location)

        if self.decimal_latitude is not None and not isinstance(self.decimal_latitude, float):
            self.decimal_latitude = float(self.decimal_latitude)

        if self.decimal_longitude is not None and not isinstance(self.decimal_longitude, float):
            self.decimal_longitude = float(self.decimal_longitude)

        if self.coordinate_precision is not None and not isinstance(self.coordinate_precision, float):
            self.coordinate_precision = float(self.coordinate_precision)

        if self.pretreatment_percentage_yield is not None and not isinstance(self.pretreatment_percentage_yield, float):
            self.pretreatment_percentage_yield = float(self.pretreatment_percentage_yield)

        if self.delta_13_c is not None and not isinstance(self.delta_13_c, float):
            self.delta_13_c = float(self.delta_13_c)

        if self.delta_13_c_error is not None and not isinstance(self.delta_13_c_error, float):
            self.delta_13_c_error = float(self.delta_13_c_error)

        if self.delta_13_c_method is not None and not isinstance(self.delta_13_c_method, Delta13CMeasurementMethod):
            self.delta_13_c_method = Delta13CMeasurementMethod(self.delta_13_c_method)

        super().__post_init__(**kwargs)


# Enumerations
class LabCode(EnumDefinitionImpl):
    """
    Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.
    """
    a = PermissibleValue(
        text="a",
        title="A",
        description="""Carbon-14 Age Determination Laboratory, University of Arizona (Arizona,USA, https://ams.arizona.edu/)""")
    aa = PermissibleValue(
        text="aa",
        title="AA",
        description="""Accelerator Mass Spectrometry Lab, University of Arizona (Arizona (AMS),USA, https://ams.arizona.edu/)""")
    aar = PermissibleValue(
        text="aar",
        title="AAR",
        description="Aarhus AMS Centre, Aarhus University (Aarhus, Aarhus, Denmark, https://c14websub.au.dk/)")
    ac = PermissibleValue(
        text="ac",
        title="AC",
        description="""INGEIS, University of Buenos Aires (INGEIS, Buenos Aires, Argentina, http://www.ingeis.uba.ar/)""")
    aecv = PermissibleValue(
        text="aecv",
        title="AECV",
        description="Alberta Environmental Center of Vegreville (Canada)")
    aerik = PermissibleValue(
        text="aerik",
        title="AERIK",
        description="Atomic Energy Research Institute (Korea)")
    alg = PermissibleValue(
        text="alg",
        title="ALG",
        description="Algiers (Algeria)")
    anas = PermissibleValue(
        text="anas",
        title="ANAS",
        description="Applied Nuclear-Atomic South Science Lab (Korea)")
    anl = PermissibleValue(
        text="anl",
        title="ANL",
        description="Argonne National Laboratory (USA)")
    antw = PermissibleValue(
        text="antw",
        title="ANTW",
        description="Antwerp (Antwerp, Belgium)")
    anu = PermissibleValue(
        text="anu",
        title="ANU",
        description="""ANU Radiocarbon Laboratory, Australian National University (ANU, Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""")
    anua = PermissibleValue(
        text="anua",
        title="ANUA",
        description="""ANU Radiocarbon Laboratory, Australian National University (AMS) (ANU (AMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""")
    sanu = PermissibleValue(
        text="sanu",
        title="SANU",
        description="""ANU Radiocarbon Laboratory, Australian National University (SSAMS) (ANU (SSAMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""")
    au = PermissibleValue(
        text="au",
        title="AU",
        description="University of Alaska (USA)")
    auris = PermissibleValue(
        text="auris",
        title="AURIS",
        description="Ahmedabad (India)")
    aix = PermissibleValue(
        text="aix",
        title="Aix",
        description="""Centre de Recherche et d'Enseignement de Geosciences de l'Environment (CERAGE), Aix-en-Provence (France)""")
    be = PermissibleValue(
        text="be",
        title="BE",
        description="""Laboratory for the Analysis of Radiocarbon with AMS, University of Bern (LARA Bern, Bern, Switzerland, https://www.14c.unibe.ch/)""")
    b = PermissibleValue(
        text="b",
        title="B",
        description="""Radiocarbon Lab, Climate and Environmental Physics, University of Bern (Bern, Bern, Switzerland, https://www.climate.unibe.ch/services/services_of_cep/radiocarbon_dating/index_eng.html)""")
    bc = PermissibleValue(
        text="bc",
        title="BC",
        description="Brooklyn College (USA)")
    bgs = PermissibleValue(
        text="bgs",
        title="BGS",
        description="Brock University (Canada)")
    biocams = PermissibleValue(
        text="biocams",
        title="BIOCAMS",
        description="Miami (Miami, USA)")
    bm = PermissibleValue(
        text="bm",
        title="BM",
        description="British Museum (London, England)")
    bonn = PermissibleValue(
        text="bonn",
        title="BONN",
        description="Universität Bonn (Bonn, Germany)")
    brams = PermissibleValue(
        text="brams",
        title="BRAMS",
        description="University of Bristol (Bristol, UK)")
    bs = PermissibleValue(
        text="bs",
        title="BS",
        description="Birbal Sahni Institute (India)")
    ba = PermissibleValue(
        text="ba",
        title="Ba",
        description="Bratislava (Bratislava, Slovakia)")
    beta = PermissibleValue(
        text="beta",
        title="Beta",
        description="Beta Analytic (USA)")
    birm = PermissibleValue(
        text="birm",
        title="Birm",
        description="Birmingham (Birmingham, UK)")
    bln = PermissibleValue(
        text="bln",
        title="Bln",
        description="Berlin (Berlin, Germany)")
    c = PermissibleValue(
        text="c",
        title="C",
        description="Chicago (Chicago, USA)")
    cams = PermissibleValue(
        text="cams",
        title="CAMS",
        description="Lawrence Livermore National Laboratory (USA)")
    car = PermissibleValue(
        text="car",
        title="CAR",
        description="University College, Cardiff (Wales)")
    cena = PermissibleValue(
        text="cena",
        title="CENA",
        description="""Centro Energia Nuclear na Agricultura, Universidade de São Paulo (São Paulo, São Paulo, Brazil)""")
    cg = PermissibleValue(
        text="cg",
        title="CG",
        description="Institute of Geology (China)")
    ch = PermissibleValue(
        text="ch",
        title="CH",
        description="Chemistry Laboratory (India)")
    ciram = PermissibleValue(
        text="ciram",
        title="CIRAM",
        description="CIRAM, Martillac (France)")
    cn_xx = PermissibleValue(
        text="cn_xx",
        title="CN-XX",
        description="Chinese Academy of Sciences (China)")
    can = PermissibleValue(
        text="can",
        title="CAN",
        description="Centro Nacional de Aceleradores (Spain)")
    cnl = PermissibleValue(
        text="cnl",
        title="CNL",
        description="Institute of Geology and Geophysics, Chinese Academy of Sciences (China)")
    col = PermissibleValue(
        text="col",
        title="COL",
        description="Köln AMS (Germany)")
    crca = PermissibleValue(
        text="crca",
        title="CRCA",
        description="Cairo (Cairo, Egypt)")
    crl = PermissibleValue(
        text="crl",
        title="CRL",
        description="""Czech Radiocarbon Laboratory, Czech Academy of Sciences (Řež, Czechia, https://www.ujf.cas.cz/en/our-services/Radiocarbon_laboratory/About_us/)""")
    csic = PermissibleValue(
        text="csic",
        title="CSIC",
        description="Geochronology Lab, IQFR-CSIC, Madrid (Spain)")
    csm = PermissibleValue(
        text="csm",
        title="CSM",
        description="Cosmochem. Lab., USSR Acad. of Sci. (USSR)")
    ct = PermissibleValue(
        text="ct",
        title="CT",
        description="Caltech, Calif. Inst. Tech. (USA)")
    cu = PermissibleValue(
        text="cu",
        title="CU",
        description="Department of Hydrology and Geology, Charles University (Prague, Czechia)")
    d = PermissibleValue(
        text="d",
        title="D",
        description="Dublin, Trinity College (Ireland)")
    d_ams = PermissibleValue(
        text="d_ams",
        title="D-AMS",
        description="Direct AMS (USA)")
    dal = PermissibleValue(
        text="dal",
        title="DAL",
        description="Radiocarbon Dating Laboratory, Dalhousie University (Dalhousie, Halifax, Canada)")
    de = PermissibleValue(
        text="de",
        title="DE",
        description="USGS, Denver (USA)")
    dem = PermissibleValue(
        text="dem",
        title="DEM",
        description="NCSR Demokritos (Greece)")
    dgc = PermissibleValue(
        text="dgc",
        title="DGC",
        description="Dalhousie Geochronology Centre, Dalhousie University (Dalhousie (DGC), Halifax, Canada)")
    dic = PermissibleValue(
        text="dic",
        title="DIC",
        description="Dicar Corp and Dicarb (USA)")
    dk = PermissibleValue(
        text="dk",
        title="DK",
        description="Univ. de Dakar (Sénégal)")
    dri = PermissibleValue(
        text="dri",
        title="DRI",
        description="Desert Research Institute (USA)")
    dsa = PermissibleValue(
        text="dsa",
        title="DSA",
        description="CIRCE, Caserta (Italy)")
    dak = PermissibleValue(
        text="dak",
        title="Dak",
        description="Univ. of Dakar (Sénégal)")
    deb = PermissibleValue(
        text="deb",
        title="Deb",
        description="Debrecen (Hungary)")
    deba = PermissibleValue(
        text="deba",
        title="DebA",
        description="Debrecen (AMS) (Hungary)")
    enea = PermissibleValue(
        text="enea",
        title="ENEA",
        description="ENEA, Bologna (Italy)")
    eth = PermissibleValue(
        text="eth",
        title="ETH",
        description="""Laboratory of Ion Beam Physics, ETH Zürich (ETH Zürich, Zürich, Switzerland, https://ams.ethz.ch/LIPServices/c14.html)""")
    erl = PermissibleValue(
        text="erl",
        title="Erl",
        description="Erlangen AMS Facility (Germany)")
    f = PermissibleValue(
        text="f",
        title="F",
        description="Florence (Italy)")
    fsu = PermissibleValue(
        text="fsu",
        title="FSU",
        description="Florida State University (USA)")
    ftmc = PermissibleValue(
        text="ftmc",
        title="FTMC",
        description="Vilnius AMS Lab (Lithuania)")
    fz = PermissibleValue(
        text="fz",
        title="FZ",
        description="Department of Physics, University of Fortaleza (Fortaleza, Fortaleza, Brazil)")
    fi = PermissibleValue(
        text="fi",
        title="Fi",
        description="Florence INFN (Italy)")
    fr = PermissibleValue(
        text="fr",
        title="Fr",
        description="Freiberg (Germany)")
    fra = PermissibleValue(
        text="fra",
        title="Fra",
        description="Frankfurt (Germany)")
    g = PermissibleValue(
        text="g",
        title="G",
        description="Göteborg (Sweden)")
    gak = PermissibleValue(
        text="gak",
        title="GAK",
        description="Gakushuin University (Japan)")
    gc = PermissibleValue(
        text="gc",
        title="GC",
        description="Guiyang Institute of Geochemistry (China)")
    gdansk = PermissibleValue(
        text="gdansk",
        title="GD",
        description="Gdansk (Gdansk, Poland)")
    gin = PermissibleValue(
        text="gin",
        title="GIN",
        description="Geological Institute (Russia)")
    gl = PermissibleValue(
        text="gl",
        title="GL",
        description="Geochronological Lab (England)")
    gsc = PermissibleValue(
        text="gsc",
        title="GSC",
        description="Geological Survey (Canada)")
    gu = PermissibleValue(
        text="gu",
        title="GU",
        description="Scottish Universities Research & Reactor Centre (Scotland)")
    gv = PermissibleValue(
        text="gv",
        title="GV",
        description="AMS Golden Valley, Novosibirsk (Russia)")
    gx = PermissibleValue(
        text="gx",
        title="GX",
        description="Geochron Laboratories (USA)")
    gxnuams = PermissibleValue(
        text="gxnuams",
        title="GXNUAMS",
        description="Guangxi Normal Univ. AMS Lab (China)")
    gz = PermissibleValue(
        text="gz",
        title="GZ",
        description="Key Laboratory of Isotope Geochronology and Geochemistry (Guangzhou) (China)")
    gliwice = PermissibleValue(
        text="gliwice",
        title="Gd",
        description="Gliwice (Poland)")
    gda = PermissibleValue(
        text="gda",
        title="GdA",
        description="Gliwice (Poland)")
    gds = PermissibleValue(
        text="gds",
        title="GdS",
        description="Gliwice (Poland)")
    gif = PermissibleValue(
        text="gif",
        title="Gif",
        description="Gif-sure-Yvette (France)")
    gifa = PermissibleValue(
        text="gifa",
        title="GifA",
        description="Gif-sure-Yvette and Orsay (France)")
    gra = PermissibleValue(
        text="gra",
        title="GrA",
        description="Groningen AMS (Netherlands)")
    grm = PermissibleValue(
        text="grm",
        title="GrM",
        description="Groningen AMS (Netherlands)")
    grn = PermissibleValue(
        text="grn",
        title="GrN",
        description="Groningen (Netherlands)")
    gro = PermissibleValue(
        text="gro",
        title="GrO",
        description="Groningen (Netherlands)")
    h = PermissibleValue(
        text="h",
        title="H",
        description="Heidelberg (Germany)")
    ham = PermissibleValue(
        text="ham",
        title="HAM",
        description="Hamburg (Germany)")
    har = PermissibleValue(
        text="har",
        title="HAR",
        description="Harwell (England)")
    hig = PermissibleValue(
        text="hig",
        title="HIG",
        description="Hawaii Inst. of Geophys. (USA)")
    hl = PermissibleValue(
        text="hl",
        title="HL",
        description="Second Inst. of Oceanography (China)")
    hns = PermissibleValue(
        text="hns",
        title="HNS",
        description="Hasleton-Nuclear, Palo Alto (USA)")
    hd = PermissibleValue(
        text="hd",
        title="Hd",
        description="Heidelberg (Germany)")
    hel = PermissibleValue(
        text="hel",
        title="Hel",
        description="""Laboratory of Chronology, University of Helsinki (Helsinki, Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)""")
    hela = PermissibleValue(
        text="hela",
        title="HelA",
        description="""Laboratory of Chronology, University of Helsinki (AMS) (Helsinki (AMS), Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)""")
    hv = PermissibleValue(
        text="hv",
        title="Hv",
        description="Hannover (Germany)")
    i = PermissibleValue(
        text="i",
        title="I",
        description="Teledyne Isotopes (USA)")
    iaa = PermissibleValue(
        text="iaa",
        title="IAA",
        description="Institute of Accelerator Analysis (beta counting) (Japan)")
    iaaa = PermissibleValue(
        text="iaaa",
        title="IAAA",
        description="Institute of Accelerator Analysis (AMS) (Japan)")
    iaea = PermissibleValue(
        text="iaea",
        title="IAEA",
        description="International Atomic Energy Agency (Austria)")
    iaea_mel = PermissibleValue(
        text="iaea_mel",
        title="IAEA-MEL",
        description="Marine Environmental Lab. (Monaco)")
    ica = PermissibleValue(
        text="ica",
        title="ICA",
        description="International Chemical Analysis (USA)")
    icen = PermissibleValue(
        text="icen",
        title="ICEN",
        description="Institution Tecnológico e Nuclear (Portugal)")
    iemae = PermissibleValue(
        text="iemae",
        title="IEMAE",
        description="Institute of Evolutionary Morphology & Animal Ecology (Russia)")
    ifao = PermissibleValue(
        text="ifao",
        title="IFAO",
        description="""Laboratoire de Datation par le Radiocarbone, Institut français d’archéologie orientale (IFAO, Cairo, Egypt)""")
    igan = PermissibleValue(
        text="igan",
        title="IGAN",
        description="Institute of Geography (Russia)")
    igs = PermissibleValue(
        text="igs",
        title="IGS",
        description="Institute of Geological Sciences (UK) (London, UK)")
    igsb = PermissibleValue(
        text="igsb",
        title="IGSB",
        description="""Institute of Geochemistry and Geophysics, National Academy of Sciences of Belarus (Minsk, Belarus)""")
    ihme = PermissibleValue(
        text="ihme",
        title="IHME",
        description="Marzeev Inst. of Hygiene Med. Ecol. (Ukraine)")
    ii = PermissibleValue(
        text="ii",
        title="II",
        description="Isotopes, Inc., Palo Alto (USA)")
    imta = PermissibleValue(
        text="imta",
        title="IMTA",
        description="Inst. Mexicano de Tecnología del Agua (Mexico)")
    ioan = PermissibleValue(
        text="ioan",
        title="IOAN",
        description="Inst. of Oceanography (Russia)")
    iop = PermissibleValue(
        text="iop",
        title="IOP",
        description="Ionplus AG (Ionplus, Dietikon, Switzerland, https://www.ionplus.ch/)")
    ioran = PermissibleValue(
        text="ioran",
        title="IORAN",
        description="Institute of Oceanology (Russia)")
    irpa = PermissibleValue(
        text="irpa",
        title="IRPA",
        description="Royal Institute for Cultural Heritage (Belgium)")
    isgs = PermissibleValue(
        text="isgs",
        title="ISGS",
        description="Illinois State Geological Survey (USA)")
    iuacd = PermissibleValue(
        text="iuacd",
        title="IUACD",
        description="Inter University Accelerator Centre (India)")
    ivan = PermissibleValue(
        text="ivan",
        title="IVAN",
        description="Institute of Volcanology (Ukraine)")
    ivic = PermissibleValue(
        text="ivic",
        title="IVIC",
        description="Caracas (Venezuela)")
    iwp = PermissibleValue(
        text="iwp",
        title="IWP",
        description="Institute of Water Problems (Russia)")
    jat = PermissibleValue(
        text="jat",
        title="JAT",
        description="Tono Geoscience Center (JAEA) (Japan)")
    k = PermissibleValue(
        text="k",
        title="K",
        description="Copenhagen (Denmark)")
    katri = PermissibleValue(
        text="katri",
        title="KATRI",
        description="Korea Apparel Testing (Korea)")
    keea = PermissibleValue(
        text="keea",
        title="KEEA",
        description="Kyushu Environ. Eval. Assoc. Property Research Inst. (Japan)")
    kf = PermissibleValue(
        text="kf",
        title="KF",
        description="State Key Laboratory of Lake Science and Environment, Chinese Academy of Sciences (China)")
    kgm = PermissibleValue(
        text="kgm",
        title="KGM",
        description="Korea Institute of Geoscience & Mineral Resources (KIGAM) (Korea)")
    kiel = PermissibleValue(
        text="kiel",
        title="KI",
        description="Kiel (Kiel, Germany)")
    kia = PermissibleValue(
        text="kia",
        title="KIA",
        description="Kiel (AMS) (Kiel, Germany)")
    kik = PermissibleValue(
        text="kik",
        title="KIK",
        description="Royal Institute for Cultural Heritage (Belgium)")
    kn = PermissibleValue(
        text="kn",
        title="KN",
        description="Köln (Cologne, Germany)")
    kr = PermissibleValue(
        text="kr",
        title="KR",
        description="Kraków (Kraków, Poland)")
    kril = PermissibleValue(
        text="kril",
        title="KRIL",
        description="Krasnoyarsk Institute (Russia)")
    ksu = PermissibleValue(
        text="ksu",
        title="KSU",
        description="Kyoto Sangyo University (Japan)")
    kiev = PermissibleValue(
        text="kiev",
        title="Ki(KIEV)",
        description="(KIEV) Institute of Radio-Geochemistry of the Environment (Kyiv, Ukraine)")
    l = PermissibleValue(
        text="l",
        title="L",
        description="Lamont-Doherty (USA)")
    lacuff = PermissibleValue(
        text="lacuff",
        title="LACUFF",
        description="""Radiocarbon Laboratory, Fluminense Federal University (Fluminense, Rio de Janeiro, Brazil, https://lac.uff.br/eng/home/)""")
    laec = PermissibleValue(
        text="laec",
        title="LAEC",
        description="Lebanese Atomic Energy Commission (LAEC) (Lebanon)")
    lar = PermissibleValue(
        text="lar",
        title="LAR",
        description="Liège State University (Belgium)")
    le = PermissibleValue(
        text="le",
        title="LE",
        description="St. Petersburg (Russia)")
    lema = PermissibleValue(
        text="lema",
        title="LEMA",
        description="Lab. de Espectrometría de Masas con Aceleradores (Mexico)")
    lih = PermissibleValue(
        text="lih",
        title="LIH",
        description="NCSR Demokritos (Greece)")
    lj = PermissibleValue(
        text="lj",
        title="LJ",
        description="Scripps (UCSD) La Jolla (USA)")
    lp = PermissibleValue(
        text="lp",
        title="LP",
        description="Laboratorio de Tritio y Radiocarbono, National University of La Plata (Argentina)")
    ltl = PermissibleValue(
        text="ltl",
        title="LTL",
        description="University of Lecce (Italy)")
    st_petersburg = PermissibleValue(
        text="st_petersburg",
        title="LU",
        description="St. Petersburg State University (Russia)")
    lz = PermissibleValue(
        text="lz",
        title="LZ",
        description="Umweltforschungszentrum Leipzig-Halle (Germany)")
    lzu = PermissibleValue(
        text="lzu",
        title="LZU",
        description="Lanzhou University (China)")
    lund = PermissibleValue(
        text="lund",
        title="Lu",
        description="Radiocarbon Dating Laboratory, Lund University (Lund, Sweden)")
    lua = PermissibleValue(
        text="lua",
        title="LuA",
        description="Radiocarbon Dating Laboratory, Lund University (AMS) (Lund (AMS), Sweden)")
    lus = PermissibleValue(
        text="lus",
        title="LuS",
        description="""Radiocarbon Dating Laboratory, Lund University (SSAMS) (Lund (SSAMS), Sweden, https://www.geology.lu.se/research/laboratories-equipment/radiocarbon-dating-laboratory)""")
    lv = PermissibleValue(
        text="lv",
        title="Lv",
        description="Louvain-la-Neuve (Belgium)")
    ly = PermissibleValue(
        text="ly",
        title="Ly",
        description="University of Lyon (France)")
    m = PermissibleValue(
        text="m",
        title="M",
        description="University of Michigan (USA)")
    mag = PermissibleValue(
        text="mag",
        title="MAG",
        description="Quaternary Geology (Russia)")
    mams = PermissibleValue(
        text="mams",
        title="MAMS",
        description="Curt-Engelhorn-Zentrum Archaeom. (Germany)")
    mc = PermissibleValue(
        text="mc",
        title="MC",
        description="Centre Scientifique (Monaco)")
    metu = PermissibleValue(
        text="metu",
        title="METU",
        description="Middle East Technical Univ. (Turkey)")
    mkl = PermissibleValue(
        text="mkl",
        title="MKL",
        description="Lab. of Absolute Dating (Poland)")
    mtc = PermissibleValue(
        text="mtc",
        title="MTC",
        description="University of Tokyo (Japan)")
    ma = PermissibleValue(
        text="ma",
        title="Ma",
        description="University of Winnepeg (Canada)")
    n = PermissibleValue(
        text="n",
        title="N",
        description="Nishina Memorial (Japan)")
    nb = PermissibleValue(
        text="nb",
        title="NB",
        description="Nanjing Museum (China)")
    nist = PermissibleValue(
        text="nist",
        title="NIST",
        description="National Institute of Standards and Technology (USA)")
    npl = PermissibleValue(
        text="npl",
        title="NPL",
        description="National Physical Laboratory, Middlesex (England)")
    ns = PermissibleValue(
        text="ns",
        title="NS",
        description="Nova Scotia Research Foundation (Canada)")
    nsrl = PermissibleValue(
        text="nsrl",
        title="NSRL",
        description="INSTAAR, University of Colorado (USA)")
    nstf = PermissibleValue(
        text="nstf",
        title="NSTF",
        description="Nuclear Science and Technology Facility, State University of New York (USA)")
    unsw = PermissibleValue(
        text="unsw",
        title="UNSW",
        description="""Chronos Radiocarbon Laboratory, University of New South Wales (New South Wales, Sydney, Australia, https://www.analytical.unsw.edu.au/facilities/x-ray-facilities/radiocarbon-laboratory)""")
    ntu = PermissibleValue(
        text="ntu",
        title="NTU",
        description="National Taiwan University (Taiwan)")
    nu = PermissibleValue(
        text="nu",
        title="NU",
        description="Nihon University (Japan)")
    nuta = PermissibleValue(
        text="nuta",
        title="NUTA",
        description="Tandetron AMS Lab (Japan)")
    nz = PermissibleValue(
        text="nz",
        title="NZ",
        description="Rafter Radiocarbon Lab (New Zealand)")
    nza = PermissibleValue(
        text="nza",
        title="NZA",
        description="Rafter Radiocarbon Lab (AMS) (New Zealand)")
    ny = PermissibleValue(
        text="ny",
        title="Ny",
        description="Nancy, Centre de Recherches Radiogéologiques (France)")
    o = PermissibleValue(
        text="o",
        title="O",
        description="Humble Oil & Refining (USA)")
    obdy = PermissibleValue(
        text="obdy",
        title="OBDY",
        description="ORSTOM Bondy (France)")
    orins = PermissibleValue(
        text="orins",
        title="ORINS",
        description="Oak Ridge Institute of Nuclear Studies (USA)")
    os = PermissibleValue(
        text="os",
        title="OS",
        description="National Ocean Sciences, AMS Facility Woods Hole Oceanographic Inst. (USA)")
    owu = PermissibleValue(
        text="owu",
        title="OWU",
        description="Ohio Wesleyan Univ. (USA)")
    ox = PermissibleValue(
        text="ox",
        title="OX",
        description="USDA (Oxford, Missouri) (USA)")
    oz = PermissibleValue(
        text="oz",
        title="OZ",
        description="""Centre for Accelerator Science, Australian Nuclear Science and Technology Organisation (ANSTO, Canberra, Australia, https://www.ansto.gov.au/our-facilities/centre-for-accelerator-science)""")
    oxa = PermissibleValue(
        text="oxa",
        title="OxA",
        description="Oxford Radiocarbon Accelerator Unit (Oxford, England)")
    p = PermissibleValue(
        text="p",
        title="P",
        description="University of Pennsylvania (USA) or Max-Planck-Institut Geochronology Lab (Germany)")
    pal = PermissibleValue(
        text="pal",
        title="PAL",
        description="Palynosurvery Co. (Japan)")
    permafrost_institute = PermissibleValue(
        text="permafrost_institute",
        title="PI",
        description="Permafrost Institute (Russia)")
    pic = PermissibleValue(
        text="pic",
        title="PIC",
        description="Packard (USA)")
    pitt = PermissibleValue(
        text="pitt",
        title="PITT",
        description="University of Pittsburgh (USA)")
    pku = PermissibleValue(
        text="pku",
        title="PKU",
        description="Peking University (China)")
    pkuams = PermissibleValue(
        text="pkuams",
        title="PKUAMS",
        description="Peking Univ. AMS lab (China)")
    pl = PermissibleValue(
        text="pl",
        title="PL",
        description="Purdue Rare Isotope Measurement Lab (USA)")
    pld = PermissibleValue(
        text="pld",
        title="PLD",
        description="Paleo Labo. Co., Ltd. (Japan)")
    pri = PermissibleValue(
        text="pri",
        title="PRI",
        description="PaleoResearch Institute (USA)")
    prl = PermissibleValue(
        text="prl",
        title="PRL",
        description="Radiocarbon Dating Research Unit (India)")
    prlch = PermissibleValue(
        text="prlch",
        title="PRLCH",
        description="Physical Research Lab (India)")
    psu = PermissibleValue(
        text="psu",
        title="PSU",
        description="Penn State University (USA)")
    psuams = PermissibleValue(
        text="psuams",
        title="PSUAMS",
        description="Penn State University (AMS) (USA)")
    pisa = PermissibleValue(
        text="pisa",
        title="Pi",
        description="Pisa (Italy)")
    poz = PermissibleValue(
        text="poz",
        title="Poz",
        description="Poznan (Poland)")
    pr = PermissibleValue(
        text="pr",
        title="Pr",
        description="Prague Czech (Republic)")
    pta = PermissibleValue(
        text="pta",
        title="Pta",
        description="Pretoria South (Africa)")
    pv = PermissibleValue(
        text="pv",
        title="PV",
        description="Institute of Vertebrate Paleontology and Paleoanthropology (China)")
    q = PermissibleValue(
        text="q",
        title="Q",
        description="Cambridge (England)")
    qc = PermissibleValue(
        text="qc",
        title="QC",
        description="Queens College (USA)")
    ql = PermissibleValue(
        text="ql",
        title="QL",
        description="Quaternary Isotope Lab. (USA)")
    qu = PermissibleValue(
        text="qu",
        title="QU",
        description="Centre de Recherches Canada Minérales, (Québec)")
    r = PermissibleValue(
        text="r",
        title="R",
        description="Rome (Italy)")
    rcd = PermissibleValue(
        text="rcd",
        title="RCD",
        description="Radiocarbon Dating (England)")
    rcmib = PermissibleValue(
        text="rcmib",
        title="RCMib",
        description="Milano Bicocca University (Italy)")
    ri = PermissibleValue(
        text="ri",
        title="RI",
        description="Radiochemistry Inc. (USA)")
    rich = PermissibleValue(
        text="rich",
        title="RICH",
        description="""Royal Institute for Cultural Heritage (KIK-IRPA, Brussels, Belgium, https://www.kikirpa.be/en/)""")
    riddl = PermissibleValue(
        text="riddl",
        title="RIDDL",
        description="Simon Fraser University (Canada)")
    rl = PermissibleValue(
        text="rl",
        title="RL",
        description="Radiocarbon, Ltd. (USA)")
    rt = PermissibleValue(
        text="rt",
        title="RT",
        description="Rehovot (Israel)")
    rtk = PermissibleValue(
        text="rtk",
        title="RTK",
        description="Rehovot (Israel)")
    ru = PermissibleValue(
        text="ru",
        title="RU",
        description="Rice University (USA)")
    riga = PermissibleValue(
        text="riga",
        title="Riga",
        description="Institute of Science (Latvia)")
    roams = PermissibleValue(
        text="roams",
        title="RoAMS",
        description="National Institute for Physics and Nuclear Engineering (Romania)")
    rome = PermissibleValue(
        text="rome",
        title="Rome",
        description="Dept. of Earth Sciences, Rome (Italy)")
    s = PermissibleValue(
        text="s",
        title="S",
        description="Saskatchewan (Canada)")
    sfu = PermissibleValue(
        text="sfu",
        title="SFU",
        description="Simon Fraser Univ. (Canada)")
    sh = PermissibleValue(
        text="sh",
        title="SH",
        description="State Key Laboratory of Estuarine and Coastal Research (China)")
    si = PermissibleValue(
        text="si",
        title="SI",
        description="Smithsonian Institution (USA)")
    sl = PermissibleValue(
        text="sl",
        title="SL",
        description="Sharp Laboratories (USA)")
    sm = PermissibleValue(
        text="sm",
        title="SM",
        description="Mobil Oil Corp., Dallas (USA)")
    smu = PermissibleValue(
        text="smu",
        title="SMU",
        description="Southern Methodist Univ. (USA)")
    snu = PermissibleValue(
        text="snu",
        title="SNU",
        description="Seoul National University South (Korea)")
    spb = PermissibleValue(
        text="spb",
        title="SPb",
        description="Herzen State University (Russia)")
    suerc = PermissibleValue(
        text="suerc",
        title="SUERC",
        description="Scottish Universities Environmental Research Centre (United Kingdom)")
    sa = PermissibleValue(
        text="sa",
        title="Sa",
        description="Saclay, Gif-sure-Yvette (France)")
    sac = PermissibleValue(
        text="sac",
        title="Sac",
        description="Institution Tecnológico Portugal e (Nuclear)")
    saca = PermissibleValue(
        text="saca",
        title="SacA",
        description="Gif sure Yvette (Saclay) (France)")
    shell = PermissibleValue(
        text="shell",
        title="Sh",
        description="Shell Development Company (USA)")
    t = PermissibleValue(
        text="t",
        title="T",
        description="Trondheim (Norway)")
    ta = PermissibleValue(
        text="ta",
        title="Ta",
        description="University of Tartu (Tartu, Tartu, Estonia)")
    tb = PermissibleValue(
        text="tb",
        title="TB",
        description="Tblisi (Georgia)")
    tbnc = PermissibleValue(
        text="tbnc",
        title="TBNC",
        description="Kaman Instruments (USA)")
    tem = PermissibleValue(
        text="tem",
        title="TEM",
        description="Temple University (USA)")
    tf = PermissibleValue(
        text="tf",
        title="TF",
        description="Tata Institute of Fundamental Research (India)")
    tk = PermissibleValue(
        text="tk",
        title="TK",
        description="University of Tokyo (Japan)")
    tokyo_museum = PermissibleValue(
        text="tokyo_museum",
        title="TKA",
        description="University Museum, Univ. of Tokyo (Japan)")
    tku = PermissibleValue(
        text="tku",
        title="TKU",
        description="Turku (Finland)")
    tokyo_ams = PermissibleValue(
        text="tokyo_ams",
        title="TKa",
        description="University of Tokyo (AMS) (Japan)")
    to = PermissibleValue(
        text="to",
        title="TO",
        description="Isotrace Radiocarbon Facility, University of Toronto (Isotrace, Toronto, Canada)")
    tra = PermissibleValue(
        text="tra",
        title="TRa",
        description="Trondheim (AMS) (Norway)")
    tubitak = PermissibleValue(
        text="tubitak",
        title="TUBITAK",
        description="""National 1MV Accelerator Mass Spectrometry Laboratory, Scientific and Technological Research Council of Turkey (TÜBİTAK, Marmara, Turkey, https://mam.tubitak.gov.tr/en/teknoloji-transfer-ofisi/national-1mv-accelerated-mass-spectroscopy-ams-laboratory)""")
    tunc = PermissibleValue(
        text="tunc",
        title="TUNC",
        description="Tehran Univ. Nuclear Centre (Iran)")
    tua = PermissibleValue(
        text="tua",
        title="TUa",
        description="Trondheim (AMS) (Norway)")
    tln = PermissibleValue(
        text="tln",
        title="Tln",
        description="Radiocarbon Laboratory, Tallinn University of Technology (Talinn, Talinn, Estonia)")
    tx = PermissibleValue(
        text="tx",
        title="Tx",
        description="Texas (USA)")
    u = PermissibleValue(
        text="u",
        title="U",
        description="Uppsala University (Uppsala, Uppsala, Sweden)")
    ua = PermissibleValue(
        text="ua",
        title="Ua",
        description="""Tandem Laboratory, Uppsala University (Uppsala (AMS), Uppsala, Sweden, https://www.uu.se/en/centre/tandemlab)""")
    ub = PermissibleValue(
        text="ub",
        title="UB",
        description="Belfast Northern (Ireland)")
    uba = PermissibleValue(
        text="uba",
        title="UBA",
        description="Belfast Northern (AMS) (Ireland)")
    ubar = PermissibleValue(
        text="ubar",
        title="UBAR",
        description="University of Barcelona (Spain)")
    ucd = PermissibleValue(
        text="ucd",
        title="UCD",
        description="University College, Dublin (Ireland)")
    uci = PermissibleValue(
        text="uci",
        title="UCI",
        description="Univ. of California, Irvine (USA)")
    ucla = PermissibleValue(
        text="ucla",
        title="UCLA",
        description="Univ. of California, Los Angeles (USA)")
    ucr = PermissibleValue(
        text="ucr",
        title="UCR",
        description="Univ. of California, Riverside (USA)")
    ud = PermissibleValue(
        text="ud",
        title="UD",
        description="Udine (Italy)")
    ugra = PermissibleValue(
        text="ugra",
        title="UGRA",
        description="University of Granada (Spain)")
    uga = PermissibleValue(
        text="uga",
        title="UGa",
        description="University of Georgia (USA)")
    ul = PermissibleValue(
        text="ul",
        title="UL",
        description="""Radiochronology Laboratory, Université Laval (Laval, Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)""")
    ula = PermissibleValue(
        text="ula",
        title="ULA",
        description="""Radiochronology Laboratory, Université Laval (AMS) (Laval (AMS), Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)""")
    um = PermissibleValue(
        text="um",
        title="UM",
        description="University of Miami (USA)")
    unam = PermissibleValue(
        text="unam",
        title="UNAM",
        description="National Autonomous Univ. of Mexico (Mexico)")
    uoc = PermissibleValue(
        text="uoc",
        title="UOC",
        description="""André E. Lalonde National Facility in Accelerator Mass Spectrometry, University of Ottawa (Ottawa, Ottawa, Canada, https://ams.uottawa.ca/)""")
    uq = PermissibleValue(
        text="uq",
        title="UQ",
        description="Univ. of Quebec at Montréal (Canada)")
    urcrm = PermissibleValue(
        text="urcrm",
        title="URCRM",
        description="Ukrainian Research Ctr. for Radiation Medicine (Ukraine)")
    uru = PermissibleValue(
        text="uru",
        title="URU",
        description="University of Uruguay (Uruguay)")
    usgs = PermissibleValue(
        text="usgs",
        title="USGS",
        description="USGS, Menlo Park (USA)")
    utcag = PermissibleValue(
        text="utcag",
        title="UTCAG",
        description="University of Tennessee (USA)")
    uw = PermissibleValue(
        text="uw",
        title="UW",
        description="University of Washington (USA)")
    uzh = PermissibleValue(
        text="uzh",
        title="UZH",
        description="""Geochronology Group, University of Zurich (Zurich, Zurich, Switzerland, https://www.geo.uzh.ch/en/units/gch.html)""")
    utc = PermissibleValue(
        text="utc",
        title="UtC",
        description="Utrecht van de Graaff (Netherlands)")
    v = PermissibleValue(
        text="v",
        title="V",
        description="Melbourne, Victoria (Australia)")
    vera = PermissibleValue(
        text="vera",
        title="VERA",
        description="""Vienna Environmental Research Accelerator, University of Vienna (VERA, Vienna, Austria, https://isotopenphysik.univie.ac.at/en/)""")
    vie = PermissibleValue(
        text="vie",
        title="VIE",
        description="""Higham Lab, University of Vienna (Higham Lab, Vienna, Austria, https://highamlab.univie.ac.at/)""")
    vri = PermissibleValue(
        text="vri",
        title="VRI",
        description="Vienna Radium Institute, University of Vienna (Vienna Radium Institute, Vienna, Austria)")
    vs = PermissibleValue(
        text="vs",
        title="Vs",
        description="Vilnius, Nat. Res. Ctr. (Vilnius, Lithuania)")
    w = PermissibleValue(
        text="w",
        title="W",
        description="USGS, National Center (USA)")
    wat = PermissibleValue(
        text="wat",
        title="WAT",
        description="University of Waterloo (Canada)")
    wb = PermissibleValue(
        text="wb",
        title="WB",
        description="Institute for Preservation Technology of Cultural Relics (China)")
    wis = PermissibleValue(
        text="wis",
        title="WIS",
        description="University of Wisconsin (USA)")
    wrd = PermissibleValue(
        text="wrd",
        title="WRD",
        description="USGS Washington, D.C. (USA)")
    wsu = PermissibleValue(
        text="wsu",
        title="WSU",
        description="Washington State Univ. (USA)")
    wk = PermissibleValue(
        text="wk",
        title="Wk",
        description="University of Waikato (New Zealand)")
    x = PermissibleValue(
        text="x",
        title="X",
        description="Whitworth College (USA)")
    xz = PermissibleValue(
        text="xz",
        title="XZ",
        description="Xinjiang Institute of Disaster Prevention and Relief (China)")
    xllq = PermissibleValue(
        text="xllq",
        title="XLLQ",
        description="Xi’an Lab. of China Loess & Quat. Geol. (China)")
    y = PermissibleValue(
        text="y",
        title="Y",
        description="Yale University (USA)")
    yu = PermissibleValue(
        text="yu",
        title="YU",
        description="Yamagata University (Japan)")
    ya = PermissibleValue(
        text="ya",
        title="Ya",
        description="Yale University (USA)")
    zz = PermissibleValue(
        text="zz",
        title="Z",
        description="""Laboratory for Low-level Radioactivities, Ruđer Bošković Institute (Zagreb, Zagreb, Croatia, https://www.irb.hr/eng/Divisions/Division-of-Experimental-Physics/Laboratory-for-Low-level-Radioactivities)""")
    zk = PermissibleValue(
        text="zk",
        title="ZK",
        description="Institute of Archaeology, Chinese Academy of Social Sciences (China)")

    _defn = EnumDefinition(
        name="LabCode",
        description="""Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "or",
            PermissibleValue(
                text="or",
                title="OR",
                description="Research Center of Radioisotopes (Japan)"))

class PretreatmentMethods(EnumDefinitionImpl):
    """
    Specify the types of general pretreatment methods applied for decontamination.
    """
    U = PermissibleValue(
        text="U",
        description="No chemical pretreatment")
    Sol_W = PermissibleValue(
        text="Sol_W",
        description="Solvent wash")
    A = PermissibleValue(
        text="A",
        description="Acid only")
    ABA = PermissibleValue(
        text="ABA",
        description="Acid-base-acid (ABA or AAA)")
    Col = PermissibleValue(
        text="Col",
        description="""Collagen (normally including deminieralisation wtih or without a base step, followed by gelatinisation and filtration, often called the 'Longin method')""")
    UF_Col = PermissibleValue(
        text="UF_Col",
        description="""Ultrafiltered collagen (normally including demineralisation with or without a base step, followed by gelatinisation, filtration and ultrafiltration)""")
    XAD = PermissibleValue(
        text="XAD",
        description="Amino acids purified by XAD-2 resin")
    IE = PermissibleValue(
        text="IE",
        description="Amino acids purified by other ion exchange resin")
    HYP = PermissibleValue(
        text="HYP",
        description="Hydroxyproline")
    Other = PermissibleValue(
        text="Other",
        description="Other treatment not covered")
    ABOx = PermissibleValue(
        text="ABOx",
        description="Acid-base-oxidation (ABOx, without the stepped combustion step)")
    BABA = PermissibleValue(
        text="BABA",
        description="Base-Acid-Base-Acid")
    Holo_Cel = PermissibleValue(
        text="Holo_Cel",
        description="Holocellulose (normally ABA followed by bleach)")
    Alph_Cel = PermissibleValue(
        text="Alph_Cel",
        description="Alphacellulose (normally containing bleach followed by ABA)")
    AE = PermissibleValue(
        text="AE",
        description="Acid etch")
    Phys = PermissibleValue(
        text="Phys",
        description="Physical cleaning (surface abrasion)")
    H2O2 = PermissibleValue(
        text="H2O2",
        description="Hydrogen peroxide")
    HUMIC = PermissibleValue(
        text="HUMIC",
        description="Base soluble fraction (normally preceeded by acid)")

    _defn = EnumDefinition(
        name="PretreatmentMethods",
        description="Specify the types of general pretreatment methods applied for decontamination.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ABOx-SC",
            PermissibleValue(
                text="ABOx-SC",
                description="Acid-base-oxidation-stepped combustion (ABOx-SC)"))

class RadiocarbonMeasurementMethod(EnumDefinitionImpl):
    """
    Method used to obtain the radiocarbon determination.
    """
    AMS = PermissibleValue(
        text="AMS",
        description="Accelerator Mass Spectrometry")
    PIMS = PermissibleValue(
        text="PIMS",
        description="Positive Ion Mass Spectrometry")
    Conventional = PermissibleValue(
        text="Conventional",
        description="""Beta counting methods such as gas proportional counting (GPC) or liquid scintillation counting (LSC)""")

    _defn = EnumDefinition(
        name="RadiocarbonMeasurementMethod",
        description="Method used to obtain the radiocarbon determination.",
    )

class Delta13CMeasurementMethod(EnumDefinitionImpl):
    """
    Which spectrophotometry method was used to measure the delta carbon-13 value, either with Isotope Ratio Mass
    Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).
    """
    AMS = PermissibleValue(
        text="AMS",
        description="Accelerated Mass Spectrometer")
    IRMS = PermissibleValue(
        text="IRMS",
        description="Isotope Ratio Mass Spectrometer")
    CRDS = PermissibleValue(
        text="CRDS",
        description="Cavity Ring-Down Spectroscopy")

    _defn = EnumDefinition(
        name="Delta13CMeasurementMethod",
        description="""Which spectrophotometry method was used to measure the delta carbon-13 value, either with Isotope Ratio Mass Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).""",
    )

# Slots
class slots:
    pass

slots.lab_code = Slot(uri=C14['000001'], name="lab_code", curie=C14.curie('000001'),
                   model_uri=C14.lab_code, domain=None, range=Union[str, "LabCode"])

slots.lab_id = Slot(uri=C14['000002'], name="lab_id", curie=C14.curie('000002'),
                   model_uri=C14.lab_id, domain=None, range=str)

slots.conventional_age = Slot(uri=C14['000005'], name="conventional_age", curie=C14.curie('000005'),
                   model_uri=C14.conventional_age, domain=None, range=float)

slots.conventional_age_error = Slot(uri=C14['000006'], name="conventional_age_error", curie=C14.curie('000006'),
                   model_uri=C14.conventional_age_error, domain=None, range=float)

slots.f14c = Slot(uri=C14['000003'], name="f14c", curie=C14.curie('000003'),
                   model_uri=C14.f14c, domain=None, range=float)

slots.f14c_error = Slot(uri=C14['000004'], name="f14c_error", curie=C14.curie('000004'),
                   model_uri=C14.f14c_error, domain=None, range=float)

slots.delta_13_c_calculation_method = Slot(uri=C14['000007'], name="delta_13_c_calculation_method", curie=C14.curie('000007'),
                   model_uri=C14.delta_13_c_calculation_method, domain=None, range=Optional[Union[str, "Delta13CMeasurementMethod"]])

slots.sample_ids = Slot(uri=C14['000008'], name="sample_ids", curie=C14.curie('000008'),
                   model_uri=C14.sample_ids, domain=None, range=Union[str, list[str]])

slots.sample_material = Slot(uri=C14['000009'], name="sample_material", curie=C14.curie('000009'),
                   model_uri=C14.sample_material, domain=None, range=str,
                   pattern=re.compile(r'[a-zA-Z]{2,}:[a-zA-Z0-9]\d+'))

slots.sample_taxon_id = Slot(uri=C14['000010'], name="sample_taxon_id", curie=C14.curie('000010'),
                   model_uri=C14.sample_taxon_id, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'[a-zA-Z]{2,}:[a-zA-Z0-9]\d+'))

slots.sample_taxon_id_confidence = Slot(uri=C14['000011'], name="sample_taxon_id_confidence", curie=C14.curie('000011'),
                   model_uri=C14.sample_taxon_id_confidence, domain=None, range=Union[bool, Bool])

slots.sample_taxon_scientific_name = Slot(uri=C14['000012'], name="sample_taxon_scientific_name", curie=C14.curie('000012'),
                   model_uri=C14.sample_taxon_scientific_name, domain=None, range=Optional[str])

slots.sample_anatomical_part = Slot(uri=C14['000013'], name="sample_anatomical_part", curie=C14.curie('000013'),
                   model_uri=C14.sample_anatomical_part, domain=None, range=Optional[str],
                   pattern=re.compile(r'[a-zA-Z]{2,}:[a-zA-Z0-9]\d+'))

slots.suspected_sample_contamination = Slot(uri=C14['000014'], name="suspected_sample_contamination", curie=C14.curie('000014'),
                   model_uri=C14.suspected_sample_contamination, domain=None, range=Optional[Union[bool, Bool]])

slots.suspected_sample_contamination_description = Slot(uri=C14['000015'], name="suspected_sample_contamination_description", curie=C14.curie('000015'),
                   model_uri=C14.suspected_sample_contamination_description, domain=None, range=Optional[str])

slots.sample_location = Slot(uri=C14['000016'], name="sample_location", curie=C14.curie('000016'),
                   model_uri=C14.sample_location, domain=None, range=Optional[str])

slots.decimal_latitude = Slot(uri=C14['000017'], name="decimal_latitude", curie=C14.curie('000017'),
                   model_uri=C14.decimal_latitude, domain=None, range=Optional[float])

slots.decimal_longitude = Slot(uri=C14['000018'], name="decimal_longitude", curie=C14.curie('000018'),
                   model_uri=C14.decimal_longitude, domain=None, range=Optional[float])

slots.coordinate_precision = Slot(uri=C14['000019'], name="coordinate_precision", curie=C14.curie('000019'),
                   model_uri=C14.coordinate_precision, domain=None, range=Optional[float])

slots.pretreatment_methods = Slot(uri=C14['000020'], name="pretreatment_methods", curie=C14.curie('000020'),
                   model_uri=C14.pretreatment_methods, domain=None, range=Union[Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]])

slots.pretreatment_method_description = Slot(uri=C14['000021'], name="pretreatment_method_description", curie=C14.curie('000021'),
                   model_uri=C14.pretreatment_method_description, domain=None, range=str)

slots.pretreatment_method_protocol = Slot(uri=C14['000022'], name="pretreatment_method_protocol", curie=C14.curie('000022'),
                   model_uri=C14.pretreatment_method_protocol, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^(PMID:\d+|https:\/\/doi\.org\/10\.\d{2,9}/.*|https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*))$'))

slots.measurement_method = Slot(uri=C14['000023'], name="measurement_method", curie=C14.curie('000023'),
                   model_uri=C14.measurement_method, domain=None, range=Union[str, "RadiocarbonMeasurementMethod"])

slots.sample_starting_weight = Slot(uri=C14['000024'], name="sample_starting_weight", curie=C14.curie('000024'),
                   model_uri=C14.sample_starting_weight, domain=None, range=float)

slots.pretreatment_yield = Slot(uri=C14['000025'], name="pretreatment_yield", curie=C14.curie('000025'),
                   model_uri=C14.pretreatment_yield, domain=None, range=float)

slots.pretreatment_percentage_yield = Slot(uri=C14['000026'], name="pretreatment_percentage_yield", curie=C14.curie('000026'),
                   model_uri=C14.pretreatment_percentage_yield, domain=None, range=Optional[float])

slots.carbon_proportion = Slot(uri=C14['000027'], name="carbon_proportion", curie=C14.curie('000027'),
                   model_uri=C14.carbon_proportion, domain=None, range=float)

slots.delta_13_c = Slot(uri=C14['000028'], name="delta_13_c", curie=C14.curie('000028'),
                   model_uri=C14.delta_13_c, domain=None, range=Optional[float])

slots.delta_13_c_error = Slot(uri=C14['000029'], name="delta_13_c_error", curie=C14.curie('000029'),
                   model_uri=C14.delta_13_c_error, domain=None, range=Optional[float])

slots.delta_13_c_method = Slot(uri=C14['000030'], name="delta_13_c_method", curie=C14.curie('000030'),
                   model_uri=C14.delta_13_c_method, domain=None, range=Optional[Union[str, "Delta13CMeasurementMethod"]])

slots.suspected_reservoir_effect = Slot(uri=C14['000031'], name="suspected_reservoir_effect", curie=C14.curie('000031'),
                   model_uri=C14.suspected_reservoir_effect, domain=None, range=Union[bool, Bool])

slots.carbon_nitro_ratio = Slot(uri=C14['000032'], name="carbon_nitro_ratio", curie=C14.curie('000032'),
                   model_uri=C14.carbon_nitro_ratio, domain=None, range=float)

slots.delta_15_n = Slot(uri=C14['000033'], name="delta_15_n", curie=C14.curie('000033'),
                   model_uri=C14.delta_15_n, domain=None, range=Optional[float])

slots.delta_15_n_error = Slot(uri=C14['000034'], name="delta_15_n_error", curie=C14.curie('000034'),
                   model_uri=C14.delta_15_n_error, domain=None, range=Optional[float])

slots.delta_34_s = Slot(uri=C14['000035'], name="delta_34_s", curie=C14.curie('000035'),
                   model_uri=C14.delta_34_s, domain=None, range=Optional[float])

slots.delta_34_s_error = Slot(uri=C14['000036'], name="delta_34_s_error", curie=C14.curie('000036'),
                   model_uri=C14.delta_34_s_error, domain=None, range=Optional[float])

slots.recrystalisation = Slot(uri=C14['000037'], name="recrystalisation", curie=C14.curie('000037'),
                   model_uri=C14.recrystalisation, domain=None, range=Union[bool, Bool])

slots.radiocarbonDateCollection__entries = Slot(uri=C14.entries, name="radiocarbonDateCollection__entries", curie=C14.curie('entries'),
                   model_uri=C14.radiocarbonDateCollection__entries, domain=None, range=Optional[Union[Union[dict, RadiocarbonDate], list[Union[dict, RadiocarbonDate]]]])
