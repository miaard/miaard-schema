# Auto generated from c14.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-08T09:42:20
# Schema: miaard
#
# id: https://w3id.org/MIxS-MInAS/miaard
# description: Minimum Information about any Radiocarbon Determination
# license: MIT

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
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

    lab_code: Union[str, "LabCodeId"] = None
    lab_id: str = None
    f14c: float = None
    f14c_error: float = None
    conventional_age: float = None
    conventional_age_error: float = None
    sample_ids: Union[str, list[str]] = None
    sample_material: str = None
    sample_taxon_id: Union[str, list[str]] = None
    sample_taxon_id_confidence: Union[bool, Bool] = None
    pretreatment_methods: Union[
        Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]
    ] = None
    pretreatment_method_description: str = None
    pretreatment_method_protocol: Union[str, list[str]] = None
    measurement_method: Union[str, "RadiocarbonMeasurementMethod"] = None
    sample_starting_weight: float = None
    pretreatment_yield: float = None
    carbon_proportion: float = None
    suspected_reservoir_effect: Union[bool, Bool] = None
    carbon_nitro_ratio: float = None
    recrystalisation: Union[bool, Bool] = None
    delta_13_c_calculation_method: Optional[Union[str, "Delta13CMeasurementMethod"]] = (
        None
    )
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
    delta_15_n: Optional[float] = None
    delta_15_n_error: Optional[float] = None
    delta_34_s: Optional[float] = None
    delta_34_s_error: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lab_code):
            self.MissingRequiredField("lab_code")
        if not isinstance(self.lab_code, LabCodeId):
            self.lab_code = LabCodeId(self.lab_code)

        if self._is_empty(self.lab_id):
            self.MissingRequiredField("lab_id")
        if not isinstance(self.lab_id, str):
            self.lab_id = str(self.lab_id)

        if self._is_empty(self.f14c):
            self.MissingRequiredField("f14c")
        if not isinstance(self.f14c, float):
            self.f14c = float(self.f14c)

        if self._is_empty(self.f14c_error):
            self.MissingRequiredField("f14c_error")
        if not isinstance(self.f14c_error, float):
            self.f14c_error = float(self.f14c_error)

        if self._is_empty(self.conventional_age):
            self.MissingRequiredField("conventional_age")
        if not isinstance(self.conventional_age, float):
            self.conventional_age = float(self.conventional_age)

        if self._is_empty(self.conventional_age_error):
            self.MissingRequiredField("conventional_age_error")
        if not isinstance(self.conventional_age_error, float):
            self.conventional_age_error = float(self.conventional_age_error)

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
            self.sample_taxon_id = (
                [self.sample_taxon_id] if self.sample_taxon_id is not None else []
            )
        self.sample_taxon_id = [
            v if isinstance(v, str) else str(v) for v in self.sample_taxon_id
        ]

        if self._is_empty(self.sample_taxon_id_confidence):
            self.MissingRequiredField("sample_taxon_id_confidence")
        if not isinstance(self.sample_taxon_id_confidence, Bool):
            self.sample_taxon_id_confidence = Bool(self.sample_taxon_id_confidence)

        if self._is_empty(self.pretreatment_methods):
            self.MissingRequiredField("pretreatment_methods")
        if not isinstance(self.pretreatment_methods, list):
            self.pretreatment_methods = (
                [self.pretreatment_methods]
                if self.pretreatment_methods is not None
                else []
            )
        self.pretreatment_methods = [
            v if isinstance(v, PretreatmentMethods) else PretreatmentMethods(v)
            for v in self.pretreatment_methods
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
        if not isinstance(self.measurement_method, RadiocarbonMeasurementMethod):
            self.measurement_method = RadiocarbonMeasurementMethod(
                self.measurement_method
            )

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

        if self._is_empty(self.carbon_nitro_ratio):
            self.MissingRequiredField("carbon_nitro_ratio")
        if not isinstance(self.carbon_nitro_ratio, float):
            self.carbon_nitro_ratio = float(self.carbon_nitro_ratio)

        if self._is_empty(self.recrystalisation):
            self.MissingRequiredField("recrystalisation")
        if not isinstance(self.recrystalisation, Bool):
            self.recrystalisation = Bool(self.recrystalisation)

        if self.delta_13_c_calculation_method is not None and not isinstance(
            self.delta_13_c_calculation_method, Delta13CMeasurementMethod
        ):
            self.delta_13_c_calculation_method = Delta13CMeasurementMethod(
                self.delta_13_c_calculation_method
            )

        if self.sample_taxon_scientific_name is not None and not isinstance(
            self.sample_taxon_scientific_name, str
        ):
            self.sample_taxon_scientific_name = str(self.sample_taxon_scientific_name)

        if self.sample_anatomical_part is not None and not isinstance(
            self.sample_anatomical_part, str
        ):
            self.sample_anatomical_part = str(self.sample_anatomical_part)

        if self.suspected_sample_contamination is not None and not isinstance(
            self.suspected_sample_contamination, Bool
        ):
            self.suspected_sample_contamination = Bool(
                self.suspected_sample_contamination
            )

        if (
            self.suspected_sample_contamination_description is not None
            and not isinstance(self.suspected_sample_contamination_description, str)
        ):
            self.suspected_sample_contamination_description = str(
                self.suspected_sample_contamination_description
            )

        if self.sample_location is not None and not isinstance(
            self.sample_location, str
        ):
            self.sample_location = str(self.sample_location)

        if self.decimal_latitude is not None and not isinstance(
            self.decimal_latitude, float
        ):
            self.decimal_latitude = float(self.decimal_latitude)

        if self.decimal_longitude is not None and not isinstance(
            self.decimal_longitude, float
        ):
            self.decimal_longitude = float(self.decimal_longitude)

        if self.coordinate_precision is not None and not isinstance(
            self.coordinate_precision, float
        ):
            self.coordinate_precision = float(self.coordinate_precision)

        if self.pretreatment_percentage_yield is not None and not isinstance(
            self.pretreatment_percentage_yield, float
        ):
            self.pretreatment_percentage_yield = float(
                self.pretreatment_percentage_yield
            )

        if self.delta_13_c is not None and not isinstance(self.delta_13_c, float):
            self.delta_13_c = float(self.delta_13_c)

        if self.delta_13_c_error is not None and not isinstance(
            self.delta_13_c_error, float
        ):
            self.delta_13_c_error = float(self.delta_13_c_error)

        if self.delta_13_c_method is not None and not isinstance(
            self.delta_13_c_method, Delta13CMeasurementMethod
        ):
            self.delta_13_c_method = Delta13CMeasurementMethod(self.delta_13_c_method)

        if self.delta_15_n is not None and not isinstance(self.delta_15_n, float):
            self.delta_15_n = float(self.delta_15_n)

        if self.delta_15_n_error is not None and not isinstance(
            self.delta_15_n_error, float
        ):
            self.delta_15_n_error = float(self.delta_15_n_error)

        if self.delta_34_s is not None and not isinstance(self.delta_34_s, float):
            self.delta_34_s = float(self.delta_34_s)

        if self.delta_34_s_error is not None and not isinstance(
            self.delta_34_s_error, float
        ):
            self.delta_34_s_error = float(self.delta_34_s_error)

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
class LabCodeId(EnumDefinitionImpl):
    """
    Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.
    """

    A = PermissibleValue(
        text="A",
        description="""Carbon-14 Age Determination Laboratory, University of Arizona (Arizona,USA, https://ams.arizona.edu/)""",
    )
    AA = PermissibleValue(
        text="AA",
        description="""Accelerator Mass Spectrometry Lab, University of Arizona (Arizona (AMS),USA, https://ams.arizona.edu/)""",
    )
    AAR = PermissibleValue(
        text="AAR",
        description="Aarhus AMS Centre, Aarhus University (Aarhus, Aarhus, Denmark, https://c14websub.au.dk/)",
    )
    AC = PermissibleValue(
        text="AC",
        description="""INGEIS, University of Buenos Aires (INGEIS, Buenos Aires, Argentina, http://www.ingeis.uba.ar/)""",
    )
    AECV = PermissibleValue(
        text="AECV", description="Alberta Environmental Center of Vegreville (Canada)"
    )
    AERIK = PermissibleValue(
        text="AERIK", description="Atomic Energy Research Institute (Korea)"
    )
    ALG = PermissibleValue(text="ALG", description="Algiers (Algeria)")
    ANAS = PermissibleValue(
        text="ANAS", description="Applied Nuclear-Atomic South Science Lab (Korea)"
    )
    ANL = PermissibleValue(text="ANL", description="Argonne National Laboratory (USA)")
    ANTW = PermissibleValue(text="ANTW", description="Antwerp (Antwerp, Belgium)")
    ANU = PermissibleValue(
        text="ANU",
        description="""ANU Radiocarbon Laboratory, Australian National University (ANU, Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""",
    )
    ANUA = PermissibleValue(
        text="ANUA",
        description="""ANU Radiocarbon Laboratory, Australian National University (AMS) (ANU (AMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""",
    )
    SANU = PermissibleValue(
        text="SANU",
        description="""ANU Radiocarbon Laboratory, Australian National University (SSAMS) (ANU (SSAMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)""",
    )
    AU = PermissibleValue(text="AU", description="University of Alaska (USA)")
    AURIS = PermissibleValue(text="AURIS", description="Ahmedabad (India)")
    Aix = PermissibleValue(
        text="Aix",
        description="""Centre de Recherche et d'Enseignement de Geosciences de l'Environment (CERAGE), Aix-en-Provence (France)""",
    )
    BE = PermissibleValue(
        text="BE",
        description="""Laboratory for the Analysis of Radiocarbon with AMS, University of Bern (LARA Bern, Bern, Switzerland, https://www.14c.unibe.ch/)""",
    )
    B = PermissibleValue(
        text="B",
        description="""Radiocarbon Lab, Climate and Environmental Physics, University of Bern (Bern, Bern, Switzerland, https://www.climate.unibe.ch/services/services_of_cep/radiocarbon_dating/index_eng.html)""",
    )
    BC = PermissibleValue(text="BC", description="Brooklyn College (USA)")
    BGS = PermissibleValue(text="BGS", description="Brock University (Canada)")
    BIOCAMS = PermissibleValue(text="BIOCAMS", description="Miami (Miami, USA)")
    BM = PermissibleValue(text="BM", description="British Museum (London, England)")
    BONN = PermissibleValue(text="BONN", description="Universität Bonn (Bonn, Germany)")
    BRAMS = PermissibleValue(
        text="BRAMS", description="University of Bristol (Bristol, UK)"
    )
    BS = PermissibleValue(text="BS", description="Birbal Sahni Institute (India)")
    Ba = PermissibleValue(text="Ba", description="Bratislava (Bratislava, Slovakia)")
    Beta = PermissibleValue(text="Beta", description="Beta Analytic (USA)")
    Birm = PermissibleValue(text="Birm", description="Birmingham (Birmingham, UK)")
    Bln = PermissibleValue(text="Bln", description="Berlin (Berlin, Germany)")
    C = PermissibleValue(text="C", description="Chicago (Chicago, USA)")
    CAMS = PermissibleValue(
        text="CAMS", description="Lawrence Livermore National Laboratory (USA)"
    )
    CAR = PermissibleValue(
        text="CAR", description="University College, Cardiff (Wales)"
    )
    CENA = PermissibleValue(
        text="CENA",
        description="""Centro Energia Nuclear na Agricultura, Universidade de São Paulo (São Paulo, São Paulo, Brazil)""",
    )
    CG = PermissibleValue(text="CG", description="Institute of Geology (China)")
    CH = PermissibleValue(text="CH", description="Chemistry Laboratory (India)")
    CIRAM = PermissibleValue(text="CIRAM", description="CIRAM, Martillac (France)")
    CAN = PermissibleValue(
        text="CAN", description="Centro Nacional de Aceleradores (Spain)"
    )
    CNL = PermissibleValue(
        text="CNL",
        description="Institute of Geology and Geophysics, Chinese Academy of Sciences (China)",
    )
    COL = PermissibleValue(text="COL", description="Köln AMS (Germany)")
    CRCA = PermissibleValue(text="CRCA", description="Cairo (Cairo, Egypt)")
    CRL = PermissibleValue(
        text="CRL",
        description="""Czech Radiocarbon Laboratory, Czech Academy of Sciences (Řež, Czechia, https://www.ujf.cas.cz/en/our-services/Radiocarbon_laboratory/About_us/)""",
    )
    CSIC = PermissibleValue(
        text="CSIC", description="Geochronology Lab, IQFR-CSIC, Madrid (Spain)"
    )
    CSM = PermissibleValue(
        text="CSM", description="Cosmochem. Lab., USSR Acad. of Sci. (USSR)"
    )
    CT = PermissibleValue(text="CT", description="Caltech, Calif. Inst. Tech. (USA)")
    CU = PermissibleValue(
        text="CU",
        description="Department of Hydrology and Geology, Charles University (Prague, Czechia)",
    )
    D = PermissibleValue(text="D", description="Dublin, Trinity College (Ireland)")
    DAL = PermissibleValue(
        text="DAL",
        description="Radiocarbon Dating Laboratory, Dalhousie University (Dalhousie, Halifax, Canada)",
    )
    DE = PermissibleValue(text="DE", description="USGS, Denver (USA)")
    DEM = PermissibleValue(text="DEM", description="NCSR Demokritos (Greece)")
    DGC = PermissibleValue(
        text="DGC",
        description="Dalhousie Geochronology Centre, Dalhousie University (Dalhousie (DGC), Halifax, Canada)",
    )
    DIC = PermissibleValue(text="DIC", description="Dicar Corp and Dicarb (USA)")
    DK = PermissibleValue(text="DK", description="Univ. de Dakar (Sénégal)")
    DRI = PermissibleValue(text="DRI", description="Desert Research Institute (USA)")
    DSA = PermissibleValue(text="DSA", description="CIRCE, Caserta (Italy)")
    Dak = PermissibleValue(text="Dak", description="Univ. of Dakar (Sénégal)")
    Deb = PermissibleValue(text="Deb", description="Debrecen (Hungary)")
    DebA = PermissibleValue(text="DebA", description="Debrecen (AMS) (Hungary)")
    ENEA = PermissibleValue(text="ENEA", description="ENEA, Bologna (Italy)")
    ETH = PermissibleValue(
        text="ETH",
        description="""Laboratory of Ion Beam Physics, ETH Zürich (ETH Zürich, Zürich, Switzerland, https://ams.ethz.ch/LIPServices/c14.html)""",
    )
    Erl = PermissibleValue(text="Erl", description="Erlangen AMS Facility (Germany)")
    F = PermissibleValue(text="F", description="Florence (Italy)")
    FSU = PermissibleValue(text="FSU", description="Florida State University (USA)")
    FTMC = PermissibleValue(text="FTMC", description="Vilnius AMS Lab (Lithuania)")
    FZ = PermissibleValue(
        text="FZ",
        description="Department of Physics, University of Fortaleza (Fortaleza, Fortaleza, Brazil)",
    )
    Fi = PermissibleValue(text="Fi", description="Florence INFN (Italy)")
    Fr = PermissibleValue(text="Fr", description="Freiberg (Germany)")
    Fra = PermissibleValue(text="Fra", description="Frankfurt (Germany)")
    G = PermissibleValue(text="G", description="Göteborg (Sweden)")
    GAK = PermissibleValue(text="GAK", description="Gakushuin University (Japan)")
    GC = PermissibleValue(
        text="GC", description="Guiyang Institute of Geochemistry (China)"
    )
    GD = PermissibleValue(text="GD", description="Gdansk (Gdansk, Poland)")
    GIN = PermissibleValue(text="GIN", description="Geological Institute (Russia)")
    GL = PermissibleValue(text="GL", description="Geochronological Lab (England)")
    GSC = PermissibleValue(text="GSC", description="Geological Survey (Canada)")
    GU = PermissibleValue(
        text="GU",
        description="Scottish Universities Research & Reactor Centre (Scotland)",
    )
    GV = PermissibleValue(
        text="GV", description="AMS Golden Valley, Novosibirsk (Russia)"
    )
    GX = PermissibleValue(text="GX", description="Geochron Laboratories (USA)")
    GXNUAMS = PermissibleValue(
        text="GXNUAMS", description="Guangxi Normal Univ. AMS Lab (China)"
    )
    GZ = PermissibleValue(
        text="GZ",
        description="Key Laboratory of Isotope Geochronology and Geochemistry (Guangzhou) (China)",
    )
    Gd = PermissibleValue(text="Gd", description="Gliwice (Poland)")
    GdA = PermissibleValue(text="GdA", description="Gliwice (Poland)")
    GdS = PermissibleValue(text="GdS", description="Gliwice (Poland)")
    Gif = PermissibleValue(text="Gif", description="Gif-sure-Yvette (France)")
    GrA = PermissibleValue(text="GrA", description="Groningen AMS (Netherlands)")
    GrM = PermissibleValue(text="GrM", description="Groningen AMS (Netherlands)")
    GrN = PermissibleValue(text="GrN", description="Groningen (Netherlands)")
    GrO = PermissibleValue(text="GrO", description="Groningen (Netherlands)")
    H = PermissibleValue(text="H", description="Heidelberg (Germany)")
    HAM = PermissibleValue(text="HAM", description="Hamburg (Germany)")
    HAR = PermissibleValue(text="HAR", description="Harwell (England)")
    HIG = PermissibleValue(text="HIG", description="Hawaii Inst. of Geophys. (USA)")
    HL = PermissibleValue(text="HL", description="Second Inst. of Oceanography (China)")
    HNS = PermissibleValue(text="HNS", description="Hasleton-Nuclear, Palo Alto (USA)")
    Hd = PermissibleValue(text="Hd", description="Heidelberg (Germany)")
    Hel = PermissibleValue(
        text="Hel",
        description="""Laboratory of Chronology, University of Helsinki (Helsinki, Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)""",
    )
    HelA = PermissibleValue(
        text="HelA",
        description="""Laboratory of Chronology, University of Helsinki (AMS) (Helsinki (AMS), Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)""",
    )
    Hv = PermissibleValue(text="Hv", description="Hannover (Germany)")
    I = PermissibleValue(text="I", description="Teledyne Isotopes (USA)")
    IAA = PermissibleValue(
        text="IAA",
        description="Institute of Accelerator Analysis (beta counting) (Japan)",
    )
    IAAA = PermissibleValue(
        text="IAAA", description="Institute of Accelerator Analysis (AMS) (Japan)"
    )
    IAEA = PermissibleValue(
        text="IAEA", description="International Atomic Energy Agency (Austria)"
    )
    ICA = PermissibleValue(
        text="ICA", description="International Chemical Analysis (USA)"
    )
    ICEN = PermissibleValue(
        text="ICEN", description="Institution Tecnológico e Nuclear (Portugal)"
    )
    IEMAE = PermissibleValue(
        text="IEMAE",
        description="Institute of Evolutionary Morphology & Animal Ecology (Russia)",
    )
    IFAO = PermissibleValue(
        text="IFAO",
        description="""Laboratoire de Datation par le Radiocarbone, Institut français d’archéologie orientale (IFAO, Cairo, Egypt)""",
    )
    IGAN = PermissibleValue(text="IGAN", description="Institute of Geography (Russia)")
    IGS = PermissibleValue(
        text="IGS", description="Institute of Geological Sciences (UK) (London, UK)"
    )
    IGSB = PermissibleValue(
        text="IGSB",
        description="""Institute of Geochemistry and Geophysics, National Academy of Sciences of Belarus (Minsk, Belarus)""",
    )
    IHME = PermissibleValue(
        text="IHME", description="Marzeev Inst. of Hygiene Med. Ecol. (Ukraine)"
    )
    II = PermissibleValue(text="II", description="Isotopes, Inc., Palo Alto (USA)")
    IMTA = PermissibleValue(
        text="IMTA", description="Inst. Mexicano de Tecnología del Agua (Mexico)"
    )
    IOAN = PermissibleValue(text="IOAN", description="Inst. of Oceanography (Russia)")
    IOP = PermissibleValue(
        text="IOP",
        description="Ionplus AG (Ionplus, Dietikon, Switzerland, https://www.ionplus.ch/)",
    )
    IORAN = PermissibleValue(
        text="IORAN", description="Institute of Oceanology (Russia)"
    )
    IRPA = PermissibleValue(
        text="IRPA", description="Royal Institute for Cultural Heritage (Belgium)"
    )
    ISGS = PermissibleValue(
        text="ISGS", description="Illinois State Geological Survey (USA)"
    )
    IUACD = PermissibleValue(
        text="IUACD", description="Inter University Accelerator Centre (India)"
    )
    IVAN = PermissibleValue(
        text="IVAN", description="Institute of Volcanology (Ukraine)"
    )
    IVIC = PermissibleValue(text="IVIC", description="Caracas (Venezuela)")
    IWP = PermissibleValue(
        text="IWP", description="Institute of Water Problems (Russia)"
    )
    JAT = PermissibleValue(
        text="JAT", description="Tono Geoscience Center (JAEA) (Japan)"
    )
    K = PermissibleValue(text="K", description="Copenhagen (Denmark)")
    KATRI = PermissibleValue(text="KATRI", description="Korea Apparel Testing (Korea)")
    KEEA = PermissibleValue(
        text="KEEA",
        description="Kyushu Environ. Eval. Assoc. Property Research Inst. (Japan)",
    )
    KF = PermissibleValue(
        text="KF",
        description="State Key Laboratory of Lake Science and Environment, Chinese Academy of Sciences (China)",
    )
    KGM = PermissibleValue(
        text="KGM",
        description="Korea Institute of Geoscience & Mineral Resources (KIGAM) (Korea)",
    )
    KI = PermissibleValue(text="KI", description="Kiel (Kiel, Germany)")
    KIA = PermissibleValue(text="KIA", description="Kiel (AMS) (Kiel, Germany)")
    KIK = PermissibleValue(
        text="KIK", description="Royal Institute for Cultural Heritage (Belgium)"
    )
    KN = PermissibleValue(text="KN", description="Köln (Cologne, Germany)")
    KR = PermissibleValue(text="KR", description="Kraków (Kraków, Poland)")
    KRIL = PermissibleValue(text="KRIL", description="Krasnoyarsk Institute (Russia)")
    KSU = PermissibleValue(text="KSU", description="Kyoto Sangyo University (Japan)")
    L = PermissibleValue(text="L", description="Lamont-Doherty (USA)")
    LACUFF = PermissibleValue(
        text="LACUFF",
        description="""Radiocarbon Laboratory, Fluminense Federal University (Fluminense, Rio de Janeiro, Brazil, https://lac.uff.br/eng/home/)""",
    )
    LAEC = PermissibleValue(
        text="LAEC", description="Lebanese Atomic Energy Commission (LAEC) (Lebanon)"
    )
    LAR = PermissibleValue(text="LAR", description="Liège State University (Belgium)")
    LE = PermissibleValue(text="LE", description="St. Petersburg (Russia)")
    LEMA = PermissibleValue(
        text="LEMA",
        description="Lab. de Espectrometría de Masas con Aceleradores (Mexico)",
    )
    LIH = PermissibleValue(text="LIH", description="NCSR Demokritos (Greece)")
    LJ = PermissibleValue(text="LJ", description="Scripps (UCSD) La Jolla (USA)")
    LP = PermissibleValue(
        text="LP",
        description="Laboratorio de Tritio y Radiocarbono, National University of La Plata (Argentina)",
    )
    LTL = PermissibleValue(text="LTL", description="University of Lecce (Italy)")
    LU = PermissibleValue(
        text="LU", description="St. Petersburg State University (Russia)"
    )
    LZ = PermissibleValue(
        text="LZ", description="Umweltforschungszentrum Leipzig-Halle (Germany)"
    )
    LZU = PermissibleValue(text="LZU", description="Lanzhou University (China)")
    Lu = PermissibleValue(
        text="Lu",
        description="Radiocarbon Dating Laboratory, Lund University (Lund, Sweden)",
    )
    LuA = PermissibleValue(
        text="LuA",
        description="Radiocarbon Dating Laboratory, Lund University (AMS) (Lund (AMS), Sweden)",
    )
    LuS = PermissibleValue(
        text="LuS",
        description="""Radiocarbon Dating Laboratory, Lund University (SSAMS) (Lund (SSAMS), Sweden, https://www.geology.lu.se/research/laboratories-equipment/radiocarbon-dating-laboratory)""",
    )
    Lv = PermissibleValue(text="Lv", description="Louvain-la-Neuve (Belgium)")
    Ly = PermissibleValue(text="Ly", description="University of Lyon (France)")
    M = PermissibleValue(text="M", description="University of Michigan (USA)")
    MAG = PermissibleValue(text="MAG", description="Quaternary Geology (Russia)")
    MAMS = PermissibleValue(
        text="MAMS", description="Curt-Engelhorn-Zentrum Archaeom. (Germany)"
    )
    MC = PermissibleValue(text="MC", description="Centre Scientifique (Monaco)")
    METU = PermissibleValue(
        text="METU", description="Middle East Technical Univ. (Turkey)"
    )
    MKL = PermissibleValue(text="MKL", description="Lab. of Absolute Dating (Poland)")
    MTC = PermissibleValue(text="MTC", description="University of Tokyo (Japan)")
    Ma = PermissibleValue(text="Ma", description="University of Winnepeg (Canada)")
    N = PermissibleValue(text="N", description="Nishina Memorial (Japan)")
    NB = PermissibleValue(text="NB", description="Nanjing Museum (China)")
    NIST = PermissibleValue(
        text="NIST", description="National Institute of Standards and Technology (USA)"
    )
    NPL = PermissibleValue(
        text="NPL", description="National Physical Laboratory, Middlesex (England)"
    )
    NS = PermissibleValue(
        text="NS", description="Nova Scotia Research Foundation (Canada)"
    )
    NSRL = PermissibleValue(
        text="NSRL", description="INSTAAR, University of Colorado (USA)"
    )
    NSTF = PermissibleValue(
        text="NSTF",
        description="Nuclear Science and Technology Facility, State University of New York (USA)",
    )
    UNSW = PermissibleValue(
        text="UNSW",
        description="""Chronos Radiocarbon Laboratory, University of New South Wales (New South Wales, Sydney, Australia, https://www.analytical.unsw.edu.au/facilities/x-ray-facilities/radiocarbon-laboratory)""",
    )
    NTU = PermissibleValue(
        text="NTU", description="National Taiwan University (Taiwan)"
    )
    NU = PermissibleValue(text="NU", description="Nihon University (Japan)")
    NUTA = PermissibleValue(text="NUTA", description="Tandetron AMS Lab (Japan)")
    NZ = PermissibleValue(text="NZ", description="Rafter Radiocarbon Lab (New Zealand)")
    NZA = PermissibleValue(
        text="NZA", description="Rafter Radiocarbon Lab (AMS) (New Zealand)"
    )
    Ny = PermissibleValue(
        text="Ny", description="Nancy, Centre de Recherches Radiogéologiques (France)"
    )
    O = PermissibleValue(text="O", description="Humble Oil & Refining (USA)")
    OBDY = PermissibleValue(text="OBDY", description="ORSTOM Bondy (France)")
    OR = PermissibleValue(
        text="OR", description="Research Center of Radioisotopes (Japan)"
    )
    ORINS = PermissibleValue(
        text="ORINS", description="Oak Ridge Institute of Nuclear Studies (USA)"
    )
    OS = PermissibleValue(
        text="OS",
        description="National Ocean Sciences, AMS Facility Woods Hole Oceanographic Inst. (USA)",
    )
    OWU = PermissibleValue(text="OWU", description="Ohio Wesleyan Univ. (USA)")
    OX = PermissibleValue(text="OX", description="USDA (Oxford, Missouri) (USA)")
    OZ = PermissibleValue(
        text="OZ",
        description="""Centre for Accelerator Science, Australian Nuclear Science and Technology Organisation (ANSTO, Canberra, Australia, https://www.ansto.gov.au/our-facilities/centre-for-accelerator-science)""",
    )
    OxA = PermissibleValue(
        text="OxA", description="Oxford Radiocarbon Accelerator Unit (Oxford, England)"
    )
    P = PermissibleValue(
        text="P",
        description="University of Pennsylvania (USA) or Max-Planck-Institut Geochronology Lab (Germany)",
    )
    PAL = PermissibleValue(text="PAL", description="Palynosurvery Co. (Japan)")
    PI = PermissibleValue(text="PI", description="Permafrost Institute (Russia)")
    PIC = PermissibleValue(text="PIC", description="Packard (USA)")
    PITT = PermissibleValue(text="PITT", description="University of Pittsburgh (USA)")
    PKU = PermissibleValue(text="PKU", description="Peking University (China)")
    PKUAMS = PermissibleValue(text="PKUAMS", description="Peking Univ. AMS lab (China)")
    PL = PermissibleValue(
        text="PL", description="Purdue Rare Isotope Measurement Lab (USA)"
    )
    PLD = PermissibleValue(text="PLD", description="Paleo Labo. Co., Ltd. (Japan)")
    PRI = PermissibleValue(text="PRI", description="PaleoResearch Institute (USA)")
    PRL = PermissibleValue(
        text="PRL", description="Radiocarbon Dating Research Unit (India)"
    )
    PRLCH = PermissibleValue(text="PRLCH", description="Physical Research Lab (India)")
    PSU = PermissibleValue(text="PSU", description="Penn State University (USA)")
    PSUAMS = PermissibleValue(
        text="PSUAMS", description="Penn State University (AMS) (USA)"
    )
    Pi = PermissibleValue(text="Pi", description="Pisa (Italy)")
    Poz = PermissibleValue(text="Poz", description="Poznan (Poland)")
    Pr = PermissibleValue(text="Pr", description="Prague Czech (Republic)")
    Pta = PermissibleValue(text="Pta", description="Pretoria South (Africa)")
    PV = PermissibleValue(
        text="PV",
        description="Institute of Vertebrate Paleontology and Paleoanthropology (China)",
    )
    Q = PermissibleValue(text="Q", description="Cambridge (England)")
    QC = PermissibleValue(text="QC", description="Queens College (USA)")
    QL = PermissibleValue(text="QL", description="Quaternary Isotope Lab. (USA)")
    QU = PermissibleValue(
        text="QU", description="Centre de Recherches Canada Minérales, (Québec)"
    )
    R = PermissibleValue(text="R", description="Rome (Italy)")
    RCD = PermissibleValue(text="RCD", description="Radiocarbon Dating (England)")
    RCMib = PermissibleValue(
        text="RCMib", description="Milano Bicocca University (Italy)"
    )
    RI = PermissibleValue(text="RI", description="Radiochemistry Inc. (USA)")
    RICH = PermissibleValue(
        text="RICH",
        description="""Royal Institute for Cultural Heritage (KIK-IRPA, Brussels, Belgium, https://www.kikirpa.be/en/)""",
    )
    RIDDL = PermissibleValue(
        text="RIDDL", description="Simon Fraser University (Canada)"
    )
    RL = PermissibleValue(text="RL", description="Radiocarbon, Ltd. (USA)")
    RT = PermissibleValue(text="RT", description="Rehovot (Israel)")
    RTK = PermissibleValue(text="RTK", description="Rehovot (Israel)")
    RU = PermissibleValue(text="RU", description="Rice University (USA)")
    Riga = PermissibleValue(text="Riga", description="Institute of Science (Latvia)")
    RoAMS = PermissibleValue(
        text="RoAMS",
        description="National Institute for Physics and Nuclear Engineering (Romania)",
    )
    Rome = PermissibleValue(
        text="Rome", description="Dept. of Earth Sciences, Rome (Italy)"
    )
    S = PermissibleValue(text="S", description="Saskatchewan (Canada)")
    SFU = PermissibleValue(text="SFU", description="Simon Fraser Univ. (Canada)")
    SH = PermissibleValue(
        text="SH",
        description="State Key Laboratory of Estuarine and Coastal Research (China)",
    )
    SI = PermissibleValue(text="SI", description="Smithsonian Institution (USA)")
    SL = PermissibleValue(text="SL", description="Sharp Laboratories (USA)")
    SM = PermissibleValue(text="SM", description="Mobil Oil Corp., Dallas (USA)")
    SMU = PermissibleValue(text="SMU", description="Southern Methodist Univ. (USA)")
    SNU = PermissibleValue(
        text="SNU", description="Seoul National University South (Korea)"
    )
    SPb = PermissibleValue(text="SPb", description="Herzen State University (Russia)")
    SUERC = PermissibleValue(
        text="SUERC",
        description="Scottish Universities Environmental Research Centre (United Kingdom)",
    )
    Sa = PermissibleValue(text="Sa", description="Saclay, Gif-sure-Yvette (France)")
    Sac = PermissibleValue(
        text="Sac", description="Institution Tecnológico Portugal e (Nuclear)"
    )
    SacA = PermissibleValue(
        text="SacA", description="Gif sure Yvette (Saclay) (France)"
    )
    Sh = PermissibleValue(text="Sh", description="Shell Development Company (USA)")
    T = PermissibleValue(text="T", description="Trondheim (Norway)")
    Ta = PermissibleValue(
        text="Ta", description="University of Tartu (Tartu, Tartu, Estonia)"
    )
    TB = PermissibleValue(text="TB", description="Tblisi (Georgia)")
    TBNC = PermissibleValue(text="TBNC", description="Kaman Instruments (USA)")
    TEM = PermissibleValue(text="TEM", description="Temple University (USA)")
    TF = PermissibleValue(
        text="TF", description="Tata Institute of Fundamental Research (India)"
    )
    TK = PermissibleValue(text="TK", description="University of Tokyo (Japan)")
    TKA = PermissibleValue(
        text="TKA", description="University Museum, Univ. of Tokyo (Japan)"
    )
    TKU = PermissibleValue(text="TKU", description="Turku (Finland)")
    TKa = PermissibleValue(text="TKa", description="University of Tokyo (AMS) (Japan)")
    TO = PermissibleValue(
        text="TO",
        description="Isotrace Radiocarbon Facility, University of Toronto (Isotrace, Toronto, Canada)",
    )
    TRa = PermissibleValue(text="TRa", description="Trondheim (AMS) (Norway)")
    TUBITAK = PermissibleValue(
        text="TUBITAK",
        description="""National 1MV Accelerator Mass Spectrometry Laboratory, Scientific and Technological Research Council of Turkey (TÜBİTAK, Marmara, Turkey, https://mam.tubitak.gov.tr/en/teknoloji-transfer-ofisi/national-1mv-accelerated-mass-spectroscopy-ams-laboratory)""",
    )
    TUNC = PermissibleValue(
        text="TUNC", description="Tehran Univ. Nuclear Centre (Iran)"
    )
    TUa = PermissibleValue(text="TUa", description="Trondheim (AMS) (Norway)")
    Tln = PermissibleValue(
        text="Tln",
        description="Radiocarbon Laboratory, Tallinn University of Technology (Talinn, Talinn, Estonia)",
    )
    Tx = PermissibleValue(text="Tx", description="Texas (USA)")
    U = PermissibleValue(
        text="U", description="Uppsala University (Uppsala, Uppsala, Sweden)"
    )
    Ua = PermissibleValue(
        text="Ua",
        description="""Tandem Laboratory, Uppsala University (Uppsala (AMS), Uppsala, Sweden, https://www.uu.se/en/centre/tandemlab)""",
    )
    UB = PermissibleValue(text="UB", description="Belfast Northern (Ireland)")
    UBA = PermissibleValue(text="UBA", description="Belfast Northern (AMS) (Ireland)")
    UBAR = PermissibleValue(text="UBAR", description="University of Barcelona (Spain)")
    UCD = PermissibleValue(
        text="UCD", description="University College, Dublin (Ireland)"
    )
    UCI = PermissibleValue(text="UCI", description="Univ. of California, Irvine (USA)")
    UCLA = PermissibleValue(
        text="UCLA", description="Univ. of California, Los Angeles (USA)"
    )
    UCR = PermissibleValue(
        text="UCR", description="Univ. of California, Riverside (USA)"
    )
    UD = PermissibleValue(text="UD", description="Udine (Italy)")
    UGRA = PermissibleValue(text="UGRA", description="University of Granada (Spain)")
    UGa = PermissibleValue(text="UGa", description="University of Georgia (USA)")
    UL = PermissibleValue(
        text="UL",
        description="""Radiochronology Laboratory, Université Laval (Laval, Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)""",
    )
    ULA = PermissibleValue(
        text="ULA",
        description="""Radiochronology Laboratory, Université Laval (AMS) (Laval (AMS), Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)""",
    )
    UM = PermissibleValue(text="UM", description="University of Miami (USA)")
    UNAM = PermissibleValue(
        text="UNAM", description="National Autonomous Univ. of Mexico (Mexico)"
    )
    UOC = PermissibleValue(
        text="UOC",
        description="""André E. Lalonde National Facility in Accelerator Mass Spectrometry, University of Ottawa (Ottawa, Ottawa, Canada, https://ams.uottawa.ca/)""",
    )
    UQ = PermissibleValue(text="UQ", description="Univ. of Quebec at Montréal (Canada)")
    URCRM = PermissibleValue(
        text="URCRM",
        description="Ukrainian Research Ctr. for Radiation Medicine (Ukraine)",
    )
    URU = PermissibleValue(text="URU", description="University of Uruguay (Uruguay)")
    USGS = PermissibleValue(text="USGS", description="USGS, Menlo Park (USA)")
    UTCAG = PermissibleValue(text="UTCAG", description="University of Tennessee (USA)")
    UW = PermissibleValue(text="UW", description="University of Washington (USA)")
    UZH = PermissibleValue(
        text="UZH",
        description="""Geochronology Group, University of Zurich (Zurich, Zurich, Switzerland, https://www.geo.uzh.ch/en/units/gch.html)""",
    )
    UtC = PermissibleValue(
        text="UtC", description="Utrecht van de Graaff (Netherlands)"
    )
    V = PermissibleValue(text="V", description="Melbourne, Victoria (Australia)")
    VERA = PermissibleValue(
        text="VERA",
        description="""Vienna Environmental Research Accelerator, University of Vienna (VERA, Vienna, Austria, https://isotopenphysik.univie.ac.at/en/)""",
    )
    VIE = PermissibleValue(
        text="VIE",
        description="""Higham Lab, University of Vienna (Higham Lab, Vienna, Austria, https://highamlab.univie.ac.at/)""",
    )
    VRI = PermissibleValue(
        text="VRI",
        description="Vienna Radium Institute, University of Vienna (Vienna Radium Institute, Vienna, Austria)",
    )
    Vs = PermissibleValue(
        text="Vs", description="Vilnius, Nat. Res. Ctr. (Vilnius, Lithuania)"
    )
    W = PermissibleValue(text="W", description="USGS, National Center (USA)")
    WAT = PermissibleValue(text="WAT", description="University of Waterloo (Canada)")
    WB = PermissibleValue(
        text="WB",
        description="Institute for Preservation Technology of Cultural Relics (China)",
    )
    WIS = PermissibleValue(text="WIS", description="University of Wisconsin (USA)")
    WRD = PermissibleValue(text="WRD", description="USGS Washington, D.C. (USA)")
    WSU = PermissibleValue(text="WSU", description="Washington State Univ. (USA)")
    Wk = PermissibleValue(text="Wk", description="University of Waikato (New Zealand)")
    X = PermissibleValue(text="X", description="Whitworth College (USA)")
    XZ = PermissibleValue(
        text="XZ",
        description="Xinjiang Institute of Disaster Prevention and Relief (China)",
    )
    XLLQ = PermissibleValue(
        text="XLLQ", description="Xi’an Lab. of China Loess & Quat. Geol. (China)"
    )
    Y = PermissibleValue(text="Y", description="Yale University (USA)")
    YU = PermissibleValue(text="YU", description="Yamagata University (Japan)")
    Ya = PermissibleValue(text="Ya", description="Yale University (USA)")
    Z = PermissibleValue(
        text="Z",
        description="""Laboratory for Low-level Radioactivities, Ruđer Bošković Institute (Zagreb, Zagreb, Croatia, https://www.irb.hr/eng/Divisions/Division-of-Experimental-Physics/Laboratory-for-Low-level-Radioactivities)""",
    )
    ZK = PermissibleValue(
        text="ZK",
        description="Institute of Archaeology, Chinese Academy of Social Sciences (China)",
    )

    _defn = EnumDefinition(
        name="LabCodeId",
        description="""Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "CN-XX",
            PermissibleValue(
                text="CN-XX", description="Chinese Academy of Sciences (China)"
            ),
        )
        setattr(
            cls, "D-AMS", PermissibleValue(text="D-AMS", description="Direct AMS (USA)")
        )
        setattr(
            cls,
            "Gif A",
            PermissibleValue(
                text="Gif A", description="Gif-sure-Yvette and Orsay (France)"
            ),
        )
        setattr(
            cls,
            "IAEA-MEL",
            PermissibleValue(
                text="IAEA-MEL", description="Marine Environmental Lab. (Monaco)"
            ),
        )
        setattr(
            cls,
            "Ki(KIEV)",
            PermissibleValue(
                text="Ki(KIEV)",
                description="(KIEV) Institute of Radio-Geochemistry of the Environment (Kyiv, Ukraine)",
            ),
        )


class PretreatmentMethods(EnumDefinitionImpl):
    """
    Specify the types of general pretreatment methods applied for decontamination.
    """

    U = PermissibleValue(text="U", description="No chemical pretreatment")
    Sol_W = PermissibleValue(text="Sol_W", description="Solvent wash")
    A = PermissibleValue(text="A", description="Acid only")
    ABA = PermissibleValue(text="ABA", description="Acid-base-acid (ABA or AAA)")
    Col = PermissibleValue(
        text="Col",
        description="""Collagen (normally including deminieralisation wtih or without a base step, followed by gelatinisation and filtration, often called the 'Longin method')""",
    )
    UF_Col = PermissibleValue(
        text="UF_Col",
        description="""Ultrafiltered collagen (normally including demineralisation with or without a base step, followed by gelatinisation, filtration and ultrafiltration)""",
    )
    XAD = PermissibleValue(
        text="XAD", description="Amino acids purified by XAD-2 resin"
    )
    IE = PermissibleValue(
        text="IE", description="Amino acids purified by other ion exchange resin"
    )
    HYP = PermissibleValue(text="HYP", description="Hydroxyproline")
    Other = PermissibleValue(text="Other", description="Other treatment not covered")
    ABOx = PermissibleValue(
        text="ABOx",
        description="Acid-base-oxidation (ABOx, without the stepped combustion step)",
    )
    BABA = PermissibleValue(text="BABA", description="Base-Acid-Base-Acid")
    Holo_Cel = PermissibleValue(
        text="Holo_Cel", description="Holocellulose (normally ABA followed by bleach)"
    )
    Alph_Cel = PermissibleValue(
        text="Alph_Cel",
        description="Alphacellulose (normally containing bleach followed by ABA)",
    )
    AE = PermissibleValue(text="AE", description="Acid etch")
    Phys = PermissibleValue(
        text="Phys", description="Physical cleaning (surface abrasion)"
    )
    H2O2 = PermissibleValue(text="H2O2", description="Hydrogen peroxide")
    HUMIC = PermissibleValue(
        text="HUMIC", description="Base soluble fraction (normally preceeded by acid)"
    )

    _defn = EnumDefinition(
        name="PretreatmentMethods",
        description="Specify the types of general pretreatment methods applied for decontamination.",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "ABOx-SC",
            PermissibleValue(
                text="ABOx-SC",
                description="Acid-base-oxidation-stepped combustion (ABOx-SC)",
            ),
        )


class RadiocarbonMeasurementMethod(EnumDefinitionImpl):
    """
    Method used to obtain the radiocarbon determination.
    """

    AMS = PermissibleValue(text="AMS", description="Accelerator Mass Spectrometry")
    PIMS = PermissibleValue(text="PIMS", description="Positive Ion Mass Spectrometry")
    Conventional = PermissibleValue(
        text="Conventional",
        description="""Beta counting methods such as gas proportional counting (GPC) or liquid scintillation counting (LSC)""",
    )

    _defn = EnumDefinition(
        name="RadiocarbonMeasurementMethod",
        description="Method used to obtain the radiocarbon determination.",
    )


class Delta13CMeasurementMethod(EnumDefinitionImpl):
    """
    Which spectrophotometry method was used to measure the delta carbon-13 value, either with Isotope Ratio Mass
    Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).
    """

    AMS = PermissibleValue(text="AMS", description="Accelerated Mass Spectrometer")
    IRMS = PermissibleValue(text="IRMS", description="Isotope Ratio Mass Spectrometer")
    CRDS = PermissibleValue(text="CRDS", description="Cavity Ring-Down Spectroscopy")

    _defn = EnumDefinition(
        name="Delta13CMeasurementMethod",
        description="""Which spectrophotometry method was used to measure the delta carbon-13 value, either with Isotope Ratio Mass Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).""",
    )


# Slots
class slots:
    pass


slots.lab_code = Slot(
    uri=C14["000001"],
    name="lab_code",
    curie=C14.curie("000001"),
    model_uri=C14.lab_code,
    domain=None,
    range=Union[str, "LabCodeId"],
)

slots.lab_id = Slot(
    uri=C14["000002"],
    name="lab_id",
    curie=C14.curie("000002"),
    model_uri=C14.lab_id,
    domain=None,
    range=str,
)

slots.f14c = Slot(
    uri=C14["000003"],
    name="f14c",
    curie=C14.curie("000003"),
    model_uri=C14.f14c,
    domain=None,
    range=float,
)

slots.f14c_error = Slot(
    uri=C14["000004"],
    name="f14c_error",
    curie=C14.curie("000004"),
    model_uri=C14.f14c_error,
    domain=None,
    range=float,
)

slots.conventional_age = Slot(
    uri=C14["000005"],
    name="conventional_age",
    curie=C14.curie("000005"),
    model_uri=C14.conventional_age,
    domain=None,
    range=float,
)

slots.conventional_age_error = Slot(
    uri=C14["000006"],
    name="conventional_age_error",
    curie=C14.curie("000006"),
    model_uri=C14.conventional_age_error,
    domain=None,
    range=float,
)

slots.delta_13_c_calculation_method = Slot(
    uri=C14["000007"],
    name="delta_13_c_calculation_method",
    curie=C14.curie("000007"),
    model_uri=C14.delta_13_c_calculation_method,
    domain=None,
    range=Optional[Union[str, "Delta13CMeasurementMethod"]],
)

slots.sample_ids = Slot(
    uri=C14["000008"],
    name="sample_ids",
    curie=C14.curie("000008"),
    model_uri=C14.sample_ids,
    domain=None,
    range=Union[str, list[str]],
)

slots.sample_material = Slot(
    uri=C14["000009"],
    name="sample_material",
    curie=C14.curie("000009"),
    model_uri=C14.sample_material,
    domain=None,
    range=str,
)

slots.sample_taxon_id = Slot(
    uri=C14["000010"],
    name="sample_taxon_id",
    curie=C14.curie("000010"),
    model_uri=C14.sample_taxon_id,
    domain=None,
    range=Union[str, list[str]],
)

slots.sample_taxon_id_confidence = Slot(
    uri=C14["000011"],
    name="sample_taxon_id_confidence",
    curie=C14.curie("000011"),
    model_uri=C14.sample_taxon_id_confidence,
    domain=None,
    range=Union[bool, Bool],
)

slots.sample_taxon_scientific_name = Slot(
    uri=C14["000012"],
    name="sample_taxon_scientific_name",
    curie=C14.curie("000012"),
    model_uri=C14.sample_taxon_scientific_name,
    domain=None,
    range=Optional[str],
)

slots.sample_anatomical_part = Slot(
    uri=C14["000013"],
    name="sample_anatomical_part",
    curie=C14.curie("000013"),
    model_uri=C14.sample_anatomical_part,
    domain=None,
    range=Optional[str],
)

slots.suspected_sample_contamination = Slot(
    uri=C14["000014"],
    name="suspected_sample_contamination",
    curie=C14.curie("000014"),
    model_uri=C14.suspected_sample_contamination,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.suspected_sample_contamination_description = Slot(
    uri=C14["000015"],
    name="suspected_sample_contamination_description",
    curie=C14.curie("000015"),
    model_uri=C14.suspected_sample_contamination_description,
    domain=None,
    range=Optional[str],
)

slots.sample_location = Slot(
    uri=C14["000016"],
    name="sample_location",
    curie=C14.curie("000016"),
    model_uri=C14.sample_location,
    domain=None,
    range=Optional[str],
)

slots.decimal_latitude = Slot(
    uri=C14["000017"],
    name="decimal_latitude",
    curie=C14.curie("000017"),
    model_uri=C14.decimal_latitude,
    domain=None,
    range=Optional[float],
)

slots.decimal_longitude = Slot(
    uri=C14["000018"],
    name="decimal_longitude",
    curie=C14.curie("000018"),
    model_uri=C14.decimal_longitude,
    domain=None,
    range=Optional[float],
)

slots.coordinate_precision = Slot(
    uri=C14["000019"],
    name="coordinate_precision",
    curie=C14.curie("000019"),
    model_uri=C14.coordinate_precision,
    domain=None,
    range=Optional[float],
)

slots.pretreatment_methods = Slot(
    uri=C14["000020"],
    name="pretreatment_methods",
    curie=C14.curie("000020"),
    model_uri=C14.pretreatment_methods,
    domain=None,
    range=Union[
        Union[str, "PretreatmentMethods"], list[Union[str, "PretreatmentMethods"]]
    ],
)

slots.pretreatment_method_description = Slot(
    uri=C14["000021"],
    name="pretreatment_method_description",
    curie=C14.curie("000021"),
    model_uri=C14.pretreatment_method_description,
    domain=None,
    range=str,
)

slots.pretreatment_method_protocol = Slot(
    uri=C14["000022"],
    name="pretreatment_method_protocol",
    curie=C14.curie("000022"),
    model_uri=C14.pretreatment_method_protocol,
    domain=None,
    range=Union[str, list[str]],
)

slots.measurement_method = Slot(
    uri=C14["000023"],
    name="measurement_method",
    curie=C14.curie("000023"),
    model_uri=C14.measurement_method,
    domain=None,
    range=Union[str, "RadiocarbonMeasurementMethod"],
)

slots.sample_starting_weight = Slot(
    uri=C14["000024"],
    name="sample_starting_weight",
    curie=C14.curie("000024"),
    model_uri=C14.sample_starting_weight,
    domain=None,
    range=float,
)

slots.pretreatment_yield = Slot(
    uri=C14["000025"],
    name="pretreatment_yield",
    curie=C14.curie("000025"),
    model_uri=C14.pretreatment_yield,
    domain=None,
    range=float,
)

slots.pretreatment_percentage_yield = Slot(
    uri=C14["000026"],
    name="pretreatment_percentage_yield",
    curie=C14.curie("000026"),
    model_uri=C14.pretreatment_percentage_yield,
    domain=None,
    range=Optional[float],
)

slots.carbon_proportion = Slot(
    uri=C14["000027"],
    name="carbon_proportion",
    curie=C14.curie("000027"),
    model_uri=C14.carbon_proportion,
    domain=None,
    range=float,
)

slots.delta_13_c = Slot(
    uri=C14["000028"],
    name="delta_13_c",
    curie=C14.curie("000028"),
    model_uri=C14.delta_13_c,
    domain=None,
    range=Optional[float],
)

slots.delta_13_c_error = Slot(
    uri=C14["000029"],
    name="delta_13_c_error",
    curie=C14.curie("000029"),
    model_uri=C14.delta_13_c_error,
    domain=None,
    range=Optional[float],
)

slots.delta_13_c_method = Slot(
    uri=C14["000030"],
    name="delta_13_c_method",
    curie=C14.curie("000030"),
    model_uri=C14.delta_13_c_method,
    domain=None,
    range=Optional[Union[str, "Delta13CMeasurementMethod"]],
)

slots.suspected_reservoir_effect = Slot(
    uri=C14["000031"],
    name="suspected_reservoir_effect",
    curie=C14.curie("000031"),
    model_uri=C14.suspected_reservoir_effect,
    domain=None,
    range=Union[bool, Bool],
)

slots.carbon_nitro_ratio = Slot(
    uri=C14["000032"],
    name="carbon_nitro_ratio",
    curie=C14.curie("000032"),
    model_uri=C14.carbon_nitro_ratio,
    domain=None,
    range=float,
)

slots.delta_15_n = Slot(
    uri=C14["000033"],
    name="delta_15_n",
    curie=C14.curie("000033"),
    model_uri=C14.delta_15_n,
    domain=None,
    range=Optional[float],
)

slots.delta_15_n_error = Slot(
    uri=C14["000034"],
    name="delta_15_n_error",
    curie=C14.curie("000034"),
    model_uri=C14.delta_15_n_error,
    domain=None,
    range=Optional[float],
)

slots.delta_34_s = Slot(
    uri=C14["000035"],
    name="delta_34_s",
    curie=C14.curie("000035"),
    model_uri=C14.delta_34_s,
    domain=None,
    range=Optional[float],
)

slots.delta_34_s_error = Slot(
    uri=C14["000036"],
    name="delta_34_s_error",
    curie=C14.curie("000036"),
    model_uri=C14.delta_34_s_error,
    domain=None,
    range=Optional[float],
)

slots.recrystalisation = Slot(
    uri=C14["000037"],
    name="recrystalisation",
    curie=C14.curie("000037"),
    model_uri=C14.recrystalisation,
    domain=None,
    range=Union[bool, Bool],
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
