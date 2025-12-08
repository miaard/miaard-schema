from __future__ import annotations

import re
from enum import Enum
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
        "settings": {
            "DOI": {
                "setting_key": "DOI",
                "setting_value": "^https:\\/\\/doi\\.org\\/10.\\d{2,9}/.*$",
            },
            "PMID": {"setting_key": "PMID", "setting_value": "^PMID:\\d+$"},
            "URL": {
                "setting_key": "URL",
                "setting_value": "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$",
            },
            "termID": {
                "setting_key": "termID",
                "setting_value": "[a-zA-Z]{2,}:[a-zA-Z0-9]\\d+",
            },
        },
        "source_file": "src/c14/schema/c14.yaml",
        "subsets": {
            "identifier": {
                "from_schema": "https://w3id.org/MIxS-MInAS/miaard",
                "name": "identifier",
            },
            "measurement": {
                "from_schema": "https://w3id.org/MIxS-MInAS/miaard",
                "name": "measurement",
            },
            "method": {
                "from_schema": "https://w3id.org/MIxS-MInAS/miaard",
                "name": "method",
            },
            "quality control": {
                "from_schema": "https://w3id.org/MIxS-MInAS/miaard",
                "name": "quality control",
            },
            "sample": {
                "from_schema": "https://w3id.org/MIxS-MInAS/miaard",
                "name": "sample",
            },
        },
        "title": "miaard",
    }
)


class LabCodeId(str, Enum):
    """
    Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.
    """

    A = "A"
    """
    Carbon-14 Age Determination Laboratory, University of Arizona (Arizona,USA, https://ams.arizona.edu/)
    """
    AA = "AA"
    """
    Accelerator Mass Spectrometry Lab, University of Arizona (Arizona (AMS),USA, https://ams.arizona.edu/)
    """
    AAR = "AAR"
    """
    Aarhus AMS Centre, Aarhus University (Aarhus, Aarhus, Denmark, https://c14websub.au.dk/)
    """
    AC = "AC"
    """
    INGEIS, University of Buenos Aires (INGEIS, Buenos Aires, Argentina, http://www.ingeis.uba.ar/)
    """
    AECV = "AECV"
    """
    Alberta Environmental Center of Vegreville (Canada)
    """
    AERIK = "AERIK"
    """
    Atomic Energy Research Institute (Korea)
    """
    ALG = "ALG"
    """
    Algiers (Algeria)
    """
    ANAS = "ANAS"
    """
    Applied Nuclear-Atomic South Science Lab (Korea)
    """
    ANL = "ANL"
    """
    Argonne National Laboratory (USA)
    """
    ANTW = "ANTW"
    """
    Antwerp (Antwerp, Belgium)
    """
    ANU = "ANU"
    """
    ANU Radiocarbon Laboratory, Australian National University (ANU, Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    ANUA = "ANUA"
    """
    ANU Radiocarbon Laboratory, Australian National University (AMS) (ANU (AMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    SANU = "SANU"
    """
    ANU Radiocarbon Laboratory, Australian National University (SSAMS) (ANU (SSAMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    AU = "AU"
    """
    University of Alaska (USA)
    """
    AURIS = "AURIS"
    """
    Ahmedabad (India)
    """
    Aix = "Aix"
    """
    Centre de Recherche et d'Enseignement de Geosciences de l'Environment (CERAGE), Aix-en-Provence (France)
    """
    BE = "BE"
    """
    Laboratory for the Analysis of Radiocarbon with AMS, University of Bern (LARA Bern, Bern, Switzerland, https://www.14c.unibe.ch/)
    """
    B = "B"
    """
    Radiocarbon Lab, Climate and Environmental Physics, University of Bern (Bern, Bern, Switzerland, https://www.climate.unibe.ch/services/services_of_cep/radiocarbon_dating/index_eng.html)
    """
    BC = "BC"
    """
    Brooklyn College (USA)
    """
    BGS = "BGS"
    """
    Brock University (Canada)
    """
    BIOCAMS = "BIOCAMS"
    """
    Miami (Miami, USA)
    """
    BM = "BM"
    """
    British Museum (London, England)
    """
    BONN = "BONN"
    """
    Universität Bonn (Bonn, Germany)
    """
    BRAMS = "BRAMS"
    """
    University of Bristol (Bristol, UK)
    """
    BS = "BS"
    """
    Birbal Sahni Institute (India)
    """
    Ba = "Ba"
    """
    Bratislava (Bratislava, Slovakia)
    """
    Beta = "Beta"
    """
    Beta Analytic (USA)
    """
    Birm = "Birm"
    """
    Birmingham (Birmingham, UK)
    """
    Bln = "Bln"
    """
    Berlin (Berlin, Germany)
    """
    C = "C"
    """
    Chicago (Chicago, USA)
    """
    CAMS = "CAMS"
    """
    Lawrence Livermore National Laboratory (USA)
    """
    CAR = "CAR"
    """
    University College, Cardiff (Wales)
    """
    CENA = "CENA"
    """
    Centro Energia Nuclear na Agricultura, Universidade de São Paulo (São Paulo, São Paulo, Brazil)
    """
    CG = "CG"
    """
    Institute of Geology (China)
    """
    CH = "CH"
    """
    Chemistry Laboratory (India)
    """
    CIRAM = "CIRAM"
    """
    CIRAM, Martillac (France)
    """
    CN_XX = "CN-XX"
    """
    Chinese Academy of Sciences (China)
    """
    CAN = "CAN"
    """
    Centro Nacional de Aceleradores (Spain)
    """
    CNL = "CNL"
    """
    Institute of Geology and Geophysics, Chinese Academy of Sciences (China)
    """
    COL = "COL"
    """
    Köln AMS (Germany)
    """
    CRCA = "CRCA"
    """
    Cairo (Cairo, Egypt)
    """
    CRL = "CRL"
    """
    Czech Radiocarbon Laboratory, Czech Academy of Sciences (Řež, Czechia, https://www.ujf.cas.cz/en/our-services/Radiocarbon_laboratory/About_us/)
    """
    CSIC = "CSIC"
    """
    Geochronology Lab, IQFR-CSIC, Madrid (Spain)
    """
    CSM = "CSM"
    """
    Cosmochem. Lab., USSR Acad. of Sci. (USSR)
    """
    CT = "CT"
    """
    Caltech, Calif. Inst. Tech. (USA)
    """
    CU = "CU"
    """
    Department of Hydrology and Geology, Charles University (Prague, Czechia)
    """
    D = "D"
    """
    Dublin, Trinity College (Ireland)
    """
    D_AMS = "D-AMS"
    """
    Direct AMS (USA)
    """
    DAL = "DAL"
    """
    Radiocarbon Dating Laboratory, Dalhousie University (Dalhousie, Halifax, Canada)
    """
    DE = "DE"
    """
    USGS, Denver (USA)
    """
    DEM = "DEM"
    """
    NCSR Demokritos (Greece)
    """
    DGC = "DGC"
    """
    Dalhousie Geochronology Centre, Dalhousie University (Dalhousie (DGC), Halifax, Canada)
    """
    DIC = "DIC"
    """
    Dicar Corp and Dicarb (USA)
    """
    DK = "DK"
    """
    Univ. de Dakar (Sénégal)
    """
    DRI = "DRI"
    """
    Desert Research Institute (USA)
    """
    DSA = "DSA"
    """
    CIRCE, Caserta (Italy)
    """
    Dak = "Dak"
    """
    Univ. of Dakar (Sénégal)
    """
    Deb = "Deb"
    """
    Debrecen (Hungary)
    """
    DebA = "DebA"
    """
    Debrecen (AMS) (Hungary)
    """
    ENEA = "ENEA"
    """
    ENEA, Bologna (Italy)
    """
    ETH = "ETH"
    """
    Laboratory of Ion Beam Physics, ETH Zürich (ETH Zürich, Zürich, Switzerland, https://ams.ethz.ch/LIPServices/c14.html)
    """
    Erl = "Erl"
    """
    Erlangen AMS Facility (Germany)
    """
    F = "F"
    """
    Florence (Italy)
    """
    FSU = "FSU"
    """
    Florida State University (USA)
    """
    FTMC = "FTMC"
    """
    Vilnius AMS Lab (Lithuania)
    """
    FZ = "FZ"
    """
    Department of Physics, University of Fortaleza (Fortaleza, Fortaleza, Brazil)
    """
    Fi = "Fi"
    """
    Florence INFN (Italy)
    """
    Fr = "Fr"
    """
    Freiberg (Germany)
    """
    Fra = "Fra"
    """
    Frankfurt (Germany)
    """
    G = "G"
    """
    Göteborg (Sweden)
    """
    GAK = "GAK"
    """
    Gakushuin University (Japan)
    """
    GC = "GC"
    """
    Guiyang Institute of Geochemistry (China)
    """
    GD = "GD"
    """
    Gdansk (Gdansk, Poland)
    """
    GIN = "GIN"
    """
    Geological Institute (Russia)
    """
    GL = "GL"
    """
    Geochronological Lab (England)
    """
    GSC = "GSC"
    """
    Geological Survey (Canada)
    """
    GU = "GU"
    """
    Scottish Universities Research & Reactor Centre (Scotland)
    """
    GV = "GV"
    """
    AMS Golden Valley, Novosibirsk (Russia)
    """
    GX = "GX"
    """
    Geochron Laboratories (USA)
    """
    GXNUAMS = "GXNUAMS"
    """
    Guangxi Normal Univ. AMS Lab (China)
    """
    GZ = "GZ"
    """
    Key Laboratory of Isotope Geochronology and Geochemistry (Guangzhou) (China)
    """
    Gd = "Gd"
    """
    Gliwice (Poland)
    """
    GdA = "GdA"
    """
    Gliwice (Poland)
    """
    GdS = "GdS"
    """
    Gliwice (Poland)
    """
    Gif = "Gif"
    """
    Gif-sure-Yvette (France)
    """
    Gif_A = "Gif A"
    """
    Gif-sure-Yvette and Orsay (France)
    """
    GrA = "GrA"
    """
    Groningen AMS (Netherlands)
    """
    GrM = "GrM"
    """
    Groningen AMS (Netherlands)
    """
    GrN = "GrN"
    """
    Groningen (Netherlands)
    """
    GrO = "GrO"
    """
    Groningen (Netherlands)
    """
    H = "H"
    """
    Heidelberg (Germany)
    """
    HAM = "HAM"
    """
    Hamburg (Germany)
    """
    HAR = "HAR"
    """
    Harwell (England)
    """
    HIG = "HIG"
    """
    Hawaii Inst. of Geophys. (USA)
    """
    HL = "HL"
    """
    Second Inst. of Oceanography (China)
    """
    HNS = "HNS"
    """
    Hasleton-Nuclear, Palo Alto (USA)
    """
    Hd = "Hd"
    """
    Heidelberg (Germany)
    """
    Hel = "Hel"
    """
    Laboratory of Chronology, University of Helsinki (Helsinki, Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)
    """
    HelA = "HelA"
    """
    Laboratory of Chronology, University of Helsinki (AMS) (Helsinki (AMS), Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)
    """
    Hv = "Hv"
    """
    Hannover (Germany)
    """
    I = "I"
    """
    Teledyne Isotopes (USA)
    """
    IAA = "IAA"
    """
    Institute of Accelerator Analysis (beta counting) (Japan)
    """
    IAAA = "IAAA"
    """
    Institute of Accelerator Analysis (AMS) (Japan)
    """
    IAEA = "IAEA"
    """
    International Atomic Energy Agency (Austria)
    """
    IAEA_MEL = "IAEA-MEL"
    """
    Marine Environmental Lab. (Monaco)
    """
    ICA = "ICA"
    """
    International Chemical Analysis (USA)
    """
    ICEN = "ICEN"
    """
    Institution Tecnológico e Nuclear (Portugal)
    """
    IEMAE = "IEMAE"
    """
    Institute of Evolutionary Morphology & Animal Ecology (Russia)
    """
    IFAO = "IFAO"
    """
    Laboratoire de Datation par le Radiocarbone, Institut français d’archéologie orientale (IFAO, Cairo, Egypt)
    """
    IGAN = "IGAN"
    """
    Institute of Geography (Russia)
    """
    IGS = "IGS"
    """
    Institute of Geological Sciences (UK) (London, UK)
    """
    IGSB = "IGSB"
    """
    Institute of Geochemistry and Geophysics, National Academy of Sciences of Belarus (Minsk, Belarus)
    """
    IHME = "IHME"
    """
    Marzeev Inst. of Hygiene Med. Ecol. (Ukraine)
    """
    II = "II"
    """
    Isotopes, Inc., Palo Alto (USA)
    """
    IMTA = "IMTA"
    """
    Inst. Mexicano de Tecnología del Agua (Mexico)
    """
    IOAN = "IOAN"
    """
    Inst. of Oceanography (Russia)
    """
    IOP = "IOP"
    """
    Ionplus AG (Ionplus, Dietikon, Switzerland, https://www.ionplus.ch/)
    """
    IORAN = "IORAN"
    """
    Institute of Oceanology (Russia)
    """
    IRPA = "IRPA"
    """
    Royal Institute for Cultural Heritage (Belgium)
    """
    ISGS = "ISGS"
    """
    Illinois State Geological Survey (USA)
    """
    IUACD = "IUACD"
    """
    Inter University Accelerator Centre (India)
    """
    IVAN = "IVAN"
    """
    Institute of Volcanology (Ukraine)
    """
    IVIC = "IVIC"
    """
    Caracas (Venezuela)
    """
    IWP = "IWP"
    """
    Institute of Water Problems (Russia)
    """
    JAT = "JAT"
    """
    Tono Geoscience Center (JAEA) (Japan)
    """
    K = "K"
    """
    Copenhagen (Denmark)
    """
    KATRI = "KATRI"
    """
    Korea Apparel Testing (Korea)
    """
    KEEA = "KEEA"
    """
    Kyushu Environ. Eval. Assoc. Property Research Inst. (Japan)
    """
    KF = "KF"
    """
    State Key Laboratory of Lake Science and Environment, Chinese Academy of Sciences (China)
    """
    KGM = "KGM"
    """
    Korea Institute of Geoscience & Mineral Resources (KIGAM) (Korea)
    """
    KI = "KI"
    """
    Kiel (Kiel, Germany)
    """
    KIA = "KIA"
    """
    Kiel (AMS) (Kiel, Germany)
    """
    KIK = "KIK"
    """
    Royal Institute for Cultural Heritage (Belgium)
    """
    KN = "KN"
    """
    Köln (Cologne, Germany)
    """
    KR = "KR"
    """
    Kraków (Kraków, Poland)
    """
    KRIL = "KRIL"
    """
    Krasnoyarsk Institute (Russia)
    """
    KSU = "KSU"
    """
    Kyoto Sangyo University (Japan)
    """
    KiLEFT_PARENTHESISKIEVRIGHT_PARENTHESIS = "Ki(KIEV)"
    """
    (KIEV) Institute of Radio-Geochemistry of the Environment (Kyiv, Ukraine)
    """
    L = "L"
    """
    Lamont-Doherty (USA)
    """
    LACUFF = "LACUFF"
    """
    Radiocarbon Laboratory, Fluminense Federal University (Fluminense, Rio de Janeiro, Brazil, https://lac.uff.br/eng/home/)
    """
    LAEC = "LAEC"
    """
    Lebanese Atomic Energy Commission (LAEC) (Lebanon)
    """
    LAR = "LAR"
    """
    Liège State University (Belgium)
    """
    LE = "LE"
    """
    St. Petersburg (Russia)
    """
    LEMA = "LEMA"
    """
    Lab. de Espectrometría de Masas con Aceleradores (Mexico)
    """
    LIH = "LIH"
    """
    NCSR Demokritos (Greece)
    """
    LJ = "LJ"
    """
    Scripps (UCSD) La Jolla (USA)
    """
    LP = "LP"
    """
    Laboratorio de Tritio y Radiocarbono, National University of La Plata (Argentina)
    """
    LTL = "LTL"
    """
    University of Lecce (Italy)
    """
    LU = "LU"
    """
    St. Petersburg State University (Russia)
    """
    LZ = "LZ"
    """
    Umweltforschungszentrum Leipzig-Halle (Germany)
    """
    LZU = "LZU"
    """
    Lanzhou University (China)
    """
    Lu = "Lu"
    """
    Radiocarbon Dating Laboratory, Lund University (Lund, Sweden)
    """
    LuA = "LuA"
    """
    Radiocarbon Dating Laboratory, Lund University (AMS) (Lund (AMS), Sweden)
    """
    LuS = "LuS"
    """
    Radiocarbon Dating Laboratory, Lund University (SSAMS) (Lund (SSAMS), Sweden, https://www.geology.lu.se/research/laboratories-equipment/radiocarbon-dating-laboratory)
    """
    Lv = "Lv"
    """
    Louvain-la-Neuve (Belgium)
    """
    Ly = "Ly"
    """
    University of Lyon (France)
    """
    M = "M"
    """
    University of Michigan (USA)
    """
    MAG = "MAG"
    """
    Quaternary Geology (Russia)
    """
    MAMS = "MAMS"
    """
    Curt-Engelhorn-Zentrum Archaeom. (Germany)
    """
    MC = "MC"
    """
    Centre Scientifique (Monaco)
    """
    METU = "METU"
    """
    Middle East Technical Univ. (Turkey)
    """
    MKL = "MKL"
    """
    Lab. of Absolute Dating (Poland)
    """
    MTC = "MTC"
    """
    University of Tokyo (Japan)
    """
    Ma = "Ma"
    """
    University of Winnepeg (Canada)
    """
    N = "N"
    """
    Nishina Memorial (Japan)
    """
    NB = "NB"
    """
    Nanjing Museum (China)
    """
    NIST = "NIST"
    """
    National Institute of Standards and Technology (USA)
    """
    NPL = "NPL"
    """
    National Physical Laboratory, Middlesex (England)
    """
    NS = "NS"
    """
    Nova Scotia Research Foundation (Canada)
    """
    NSRL = "NSRL"
    """
    INSTAAR, University of Colorado (USA)
    """
    NSTF = "NSTF"
    """
    Nuclear Science and Technology Facility, State University of New York (USA)
    """
    UNSW = "UNSW"
    """
    Chronos Radiocarbon Laboratory, University of New South Wales (New South Wales, Sydney, Australia, https://www.analytical.unsw.edu.au/facilities/x-ray-facilities/radiocarbon-laboratory)
    """
    NTU = "NTU"
    """
    National Taiwan University (Taiwan)
    """
    NU = "NU"
    """
    Nihon University (Japan)
    """
    NUTA = "NUTA"
    """
    Tandetron AMS Lab (Japan)
    """
    NZ = "NZ"
    """
    Rafter Radiocarbon Lab (New Zealand)
    """
    NZA = "NZA"
    """
    Rafter Radiocarbon Lab (AMS) (New Zealand)
    """
    Ny = "Ny"
    """
    Nancy, Centre de Recherches Radiogéologiques (France)
    """
    O = "O"
    """
    Humble Oil & Refining (USA)
    """
    OBDY = "OBDY"
    """
    ORSTOM Bondy (France)
    """
    OR = "OR"
    """
    Research Center of Radioisotopes (Japan)
    """
    ORINS = "ORINS"
    """
    Oak Ridge Institute of Nuclear Studies (USA)
    """
    OS = "OS"
    """
    National Ocean Sciences, AMS Facility Woods Hole Oceanographic Inst. (USA)
    """
    OWU = "OWU"
    """
    Ohio Wesleyan Univ. (USA)
    """
    OX = "OX"
    """
    USDA (Oxford, Missouri) (USA)
    """
    OZ = "OZ"
    """
    Centre for Accelerator Science, Australian Nuclear Science and Technology Organisation (ANSTO, Canberra, Australia, https://www.ansto.gov.au/our-facilities/centre-for-accelerator-science)
    """
    OxA = "OxA"
    """
    Oxford Radiocarbon Accelerator Unit (Oxford, England)
    """
    P = "P"
    """
    University of Pennsylvania (USA) or Max-Planck-Institut Geochronology Lab (Germany)
    """
    PAL = "PAL"
    """
    Palynosurvery Co. (Japan)
    """
    PI = "PI"
    """
    Permafrost Institute (Russia)
    """
    PIC = "PIC"
    """
    Packard (USA)
    """
    PITT = "PITT"
    """
    University of Pittsburgh (USA)
    """
    PKU = "PKU"
    """
    Peking University (China)
    """
    PKUAMS = "PKUAMS"
    """
    Peking Univ. AMS lab (China)
    """
    PL = "PL"
    """
    Purdue Rare Isotope Measurement Lab (USA)
    """
    PLD = "PLD"
    """
    Paleo Labo. Co., Ltd. (Japan)
    """
    PRI = "PRI"
    """
    PaleoResearch Institute (USA)
    """
    PRL = "PRL"
    """
    Radiocarbon Dating Research Unit (India)
    """
    PRLCH = "PRLCH"
    """
    Physical Research Lab (India)
    """
    PSU = "PSU"
    """
    Penn State University (USA)
    """
    PSUAMS = "PSUAMS"
    """
    Penn State University (AMS) (USA)
    """
    Pi = "Pi"
    """
    Pisa (Italy)
    """
    Poz = "Poz"
    """
    Poznan (Poland)
    """
    Pr = "Pr"
    """
    Prague Czech (Republic)
    """
    Pta = "Pta"
    """
    Pretoria South (Africa)
    """
    PV = "PV"
    """
    Institute of Vertebrate Paleontology and Paleoanthropology (China)
    """
    Q = "Q"
    """
    Cambridge (England)
    """
    QC = "QC"
    """
    Queens College (USA)
    """
    QL = "QL"
    """
    Quaternary Isotope Lab. (USA)
    """
    QU = "QU"
    """
    Centre de Recherches Canada Minérales, (Québec)
    """
    R = "R"
    """
    Rome (Italy)
    """
    RCD = "RCD"
    """
    Radiocarbon Dating (England)
    """
    RCMib = "RCMib"
    """
    Milano Bicocca University (Italy)
    """
    RI = "RI"
    """
    Radiochemistry Inc. (USA)
    """
    RICH = "RICH"
    """
    Royal Institute for Cultural Heritage (KIK-IRPA, Brussels, Belgium, https://www.kikirpa.be/en/)
    """
    RIDDL = "RIDDL"
    """
    Simon Fraser University (Canada)
    """
    RL = "RL"
    """
    Radiocarbon, Ltd. (USA)
    """
    RT = "RT"
    """
    Rehovot (Israel)
    """
    RTK = "RTK"
    """
    Rehovot (Israel)
    """
    RU = "RU"
    """
    Rice University (USA)
    """
    Riga = "Riga"
    """
    Institute of Science (Latvia)
    """
    RoAMS = "RoAMS"
    """
    National Institute for Physics and Nuclear Engineering (Romania)
    """
    Rome = "Rome"
    """
    Dept. of Earth Sciences, Rome (Italy)
    """
    S = "S"
    """
    Saskatchewan (Canada)
    """
    SFU = "SFU"
    """
    Simon Fraser Univ. (Canada)
    """
    SH = "SH"
    """
    State Key Laboratory of Estuarine and Coastal Research (China)
    """
    SI = "SI"
    """
    Smithsonian Institution (USA)
    """
    SL = "SL"
    """
    Sharp Laboratories (USA)
    """
    SM = "SM"
    """
    Mobil Oil Corp., Dallas (USA)
    """
    SMU = "SMU"
    """
    Southern Methodist Univ. (USA)
    """
    SNU = "SNU"
    """
    Seoul National University South (Korea)
    """
    SPb = "SPb"
    """
    Herzen State University (Russia)
    """
    SUERC = "SUERC"
    """
    Scottish Universities Environmental Research Centre (United Kingdom)
    """
    Sa = "Sa"
    """
    Saclay, Gif-sure-Yvette (France)
    """
    Sac = "Sac"
    """
    Institution Tecnológico Portugal e (Nuclear)
    """
    SacA = "SacA"
    """
    Gif sure Yvette (Saclay) (France)
    """
    Sh = "Sh"
    """
    Shell Development Company (USA)
    """
    T = "T"
    """
    Trondheim (Norway)
    """
    Ta = "Ta"
    """
    University of Tartu (Tartu, Tartu, Estonia)
    """
    TB = "TB"
    """
    Tblisi (Georgia)
    """
    TBNC = "TBNC"
    """
    Kaman Instruments (USA)
    """
    TEM = "TEM"
    """
    Temple University (USA)
    """
    TF = "TF"
    """
    Tata Institute of Fundamental Research (India)
    """
    TK = "TK"
    """
    University of Tokyo (Japan)
    """
    TKA = "TKA"
    """
    University Museum, Univ. of Tokyo (Japan)
    """
    TKU = "TKU"
    """
    Turku (Finland)
    """
    TKa = "TKa"
    """
    University of Tokyo (AMS) (Japan)
    """
    TO = "TO"
    """
    Isotrace Radiocarbon Facility, University of Toronto (Isotrace, Toronto, Canada)
    """
    TRa = "TRa"
    """
    Trondheim (AMS) (Norway)
    """
    TUBITAK = "TUBITAK"
    """
    National 1MV Accelerator Mass Spectrometry Laboratory, Scientific and Technological Research Council of Turkey (TÜBİTAK, Marmara, Turkey, https://mam.tubitak.gov.tr/en/teknoloji-transfer-ofisi/national-1mv-accelerated-mass-spectroscopy-ams-laboratory)
    """
    TUNC = "TUNC"
    """
    Tehran Univ. Nuclear Centre (Iran)
    """
    TUa = "TUa"
    """
    Trondheim (AMS) (Norway)
    """
    Tln = "Tln"
    """
    Radiocarbon Laboratory, Tallinn University of Technology (Talinn, Talinn, Estonia)
    """
    Tx = "Tx"
    """
    Texas (USA)
    """
    U = "U"
    """
    Uppsala University (Uppsala, Uppsala, Sweden)
    """
    Ua = "Ua"
    """
    Tandem Laboratory, Uppsala University (Uppsala (AMS), Uppsala, Sweden, https://www.uu.se/en/centre/tandemlab)
    """
    UB = "UB"
    """
    Belfast Northern (Ireland)
    """
    UBA = "UBA"
    """
    Belfast Northern (AMS) (Ireland)
    """
    UBAR = "UBAR"
    """
    University of Barcelona (Spain)
    """
    UCD = "UCD"
    """
    University College, Dublin (Ireland)
    """
    UCI = "UCI"
    """
    Univ. of California, Irvine (USA)
    """
    UCLA = "UCLA"
    """
    Univ. of California, Los Angeles (USA)
    """
    UCR = "UCR"
    """
    Univ. of California, Riverside (USA)
    """
    UD = "UD"
    """
    Udine (Italy)
    """
    UGRA = "UGRA"
    """
    University of Granada (Spain)
    """
    UGa = "UGa"
    """
    University of Georgia (USA)
    """
    UL = "UL"
    """
    Radiochronology Laboratory, Université Laval (Laval, Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)
    """
    ULA = "ULA"
    """
    Radiochronology Laboratory, Université Laval (AMS) (Laval (AMS), Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)
    """
    UM = "UM"
    """
    University of Miami (USA)
    """
    UNAM = "UNAM"
    """
    National Autonomous Univ. of Mexico (Mexico)
    """
    UOC = "UOC"
    """
    André E. Lalonde National Facility in Accelerator Mass Spectrometry, University of Ottawa (Ottawa, Ottawa, Canada, https://ams.uottawa.ca/)
    """
    UQ = "UQ"
    """
    Univ. of Quebec at Montréal (Canada)
    """
    URCRM = "URCRM"
    """
    Ukrainian Research Ctr. for Radiation Medicine (Ukraine)
    """
    URU = "URU"
    """
    University of Uruguay (Uruguay)
    """
    USGS = "USGS"
    """
    USGS, Menlo Park (USA)
    """
    UTCAG = "UTCAG"
    """
    University of Tennessee (USA)
    """
    UW = "UW"
    """
    University of Washington (USA)
    """
    UZH = "UZH"
    """
    Geochronology Group, University of Zurich (Zurich, Zurich, Switzerland, https://www.geo.uzh.ch/en/units/gch.html)
    """
    UtC = "UtC"
    """
    Utrecht van de Graaff (Netherlands)
    """
    V = "V"
    """
    Melbourne, Victoria (Australia)
    """
    VERA = "VERA"
    """
    Vienna Environmental Research Accelerator, University of Vienna (VERA, Vienna, Austria, https://isotopenphysik.univie.ac.at/en/)
    """
    VIE = "VIE"
    """
    Higham Lab, University of Vienna (Higham Lab, Vienna, Austria, https://highamlab.univie.ac.at/)
    """
    VRI = "VRI"
    """
    Vienna Radium Institute, University of Vienna (Vienna Radium Institute, Vienna, Austria)
    """
    Vs = "Vs"
    """
    Vilnius, Nat. Res. Ctr. (Vilnius, Lithuania)
    """
    W = "W"
    """
    USGS, National Center (USA)
    """
    WAT = "WAT"
    """
    University of Waterloo (Canada)
    """
    WB = "WB"
    """
    Institute for Preservation Technology of Cultural Relics (China)
    """
    WIS = "WIS"
    """
    University of Wisconsin (USA)
    """
    WRD = "WRD"
    """
    USGS Washington, D.C. (USA)
    """
    WSU = "WSU"
    """
    Washington State Univ. (USA)
    """
    Wk = "Wk"
    """
    University of Waikato (New Zealand)
    """
    X = "X"
    """
    Whitworth College (USA)
    """
    XZ = "XZ"
    """
    Xinjiang Institute of Disaster Prevention and Relief (China)
    """
    XLLQ = "XLLQ"
    """
    Xi’an Lab. of China Loess & Quat. Geol. (China)
    """
    Y = "Y"
    """
    Yale University (USA)
    """
    YU = "YU"
    """
    Yamagata University (Japan)
    """
    Ya = "Ya"
    """
    Yale University (USA)
    """
    Z = "Z"
    """
    Laboratory for Low-level Radioactivities, Ruđer Bošković Institute (Zagreb, Zagreb, Croatia, https://www.irb.hr/eng/Divisions/Division-of-Experimental-Physics/Laboratory-for-Low-level-Radioactivities)
    """
    ZK = "ZK"
    """
    Institute of Archaeology, Chinese Academy of Social Sciences (China)
    """


class PretreatmentMethods(str, Enum):
    """
    Specify the types of general pretreatment methods applied for decontamination.
    """

    U = "U"
    """
    No chemical pretreatment
    """
    Sol_W = "Sol_W"
    """
    Solvent wash
    """
    A = "A"
    """
    Acid only
    """
    ABA = "ABA"
    """
    Acid-base-acid (ABA or AAA)
    """
    Col = "Col"
    """
    Collagen (normally including deminieralisation wtih or without a base step, followed by gelatinisation and filtration, often called the 'Longin method')
    """
    UF_Col = "UF_Col"
    """
    Ultrafiltered collagen (normally including demineralisation with or without a base step, followed by gelatinisation, filtration and ultrafiltration)
    """
    XAD = "XAD"
    """
    Amino acids purified by XAD-2 resin
    """
    IE = "IE"
    """
    Amino acids purified by other ion exchange resin
    """
    HYP = "HYP"
    """
    Hydroxyproline
    """
    Other = "Other"
    """
    Other treatment not covered
    """
    ABOx = "ABOx"
    """
    Acid-base-oxidation (ABOx, without the stepped combustion step)
    """
    ABOx_SC = "ABOx-SC"
    """
    Acid-base-oxidation-stepped combustion (ABOx-SC)
    """
    BABA = "BABA"
    """
    Base-Acid-Base-Acid
    """
    Holo_Cel = "Holo_Cel"
    """
    Holocellulose (normally ABA followed by bleach)
    """
    Alph_Cel = "Alph_Cel"
    """
    Alphacellulose (normally containing bleach followed by ABA)
    """
    AE = "AE"
    """
    Acid etch
    """
    Phys = "Phys"
    """
    Physical cleaning (surface abrasion)
    """
    H2O2 = "H2O2"
    """
    Hydrogen peroxide
    """
    HUMIC = "HUMIC"
    """
    Base soluble fraction (normally preceeded by acid)
    """


class RadiocarbonMeasurementMethod(str, Enum):
    """
    Method used to obtain the radiocarbon determination.
    """

    AMS = "AMS"
    """
    Accelerator Mass Spectrometry
    """
    PIMS = "PIMS"
    """
    Positive Ion Mass Spectrometry
    """
    Conventional = "Conventional"
    """
    Beta counting methods such as gas proportional counting (GPC) or liquid scintillation counting (LSC)
    """


class Delta13CMeasurementMethod(str, Enum):
    """
    Which spectrophotometry method was used to measure the delta carbon-13 value, either with Isotope Ratio Mass Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).
    """

    AMS = "AMS"
    """
    Accelerated Mass Spectrometer
    """
    IRMS = "IRMS"
    """
    Isotope Ratio Mass Spectrometer
    """
    CRDS = "CRDS"
    """
    Cavity Ring-Down Spectroscopy
    """


class RadiocarbonDate(ConfiguredBaseModel):
    """
    A radiocarbon determination with associated metadata.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/MIxS-MInAS/miaard"}
    )

    lab_code: LabCodeId = Field(
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
                "in_subset": ["identifier", "measurement"],
                "slot_uri": "c14:000001",
            }
        },
    )
    lab_id: str = Field(
        default=...,
        title="Radiocarbon determination identifier",
        description="""The unique identifier associated with a specific radiocarbon determination,
without the radiocarbon laboratory identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "982744"},
                    {"value": "i238493"},
                    {"value": "9800507B"},
                    {"value": "-X-1045-13"},
                    {"value": "1415(a)"},
                ],
                "in_subset": ["identifier"],
                "slot_uri": "c14:000002",
            }
        },
    )
    f14c: float = Field(
        default=...,
        description="""The F14C value from the laboratory measurement, i.e. the fraction modern carbon.
For older determinations, generally equivalent to \"percent modern\" (pMC, or pM) divided by 100.""",
        ge=0,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.83756"}, {"value": "0.5371"}],
                "in_subset": ["measurement"],
                "slot_uri": "c14:000003",
            }
        },
    )
    f14c_error: float = Field(
        default=...,
        title="F14C radiocarbon error",
        description="""The 1-standard deviation uncertainty around the F14C (C14) measurement,
normally indicated as a ± after the main value. Must be in the same format.
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.00434"}, {"value": "0.023843"}],
                "in_subset": ["measurement"],
                "slot_uri": "c14:000004",
            }
        },
    )
    conventional_age: float = Field(
        default=...,
        title="Conventional radiocarbon age",
        description="""The uncalibrated age from the laboratory measurement. Also known as the
conventional radiocarbon age (CRA). Should be a conventional 14C age (i.e., 14C year BP)
NOT in AD/BC format. This is typically the 'raw' age reported by the radiocarbon lab, in
Before Present (BP) notation.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "4500"}, {"value": "37330"}],
                "in_subset": ["measurement"],
                "slot_uri": "c14:000005",
            }
        },
    )
    conventional_age_error: float = Field(
        default=...,
        title="Conventional radiocarbon age error",
        description="""The 1-standard deviation around the conventional radiocarbon age (C14) measurement,
normally indicated as a ± after the main age. Must be in the same format (i.e. 14C yr BP).
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "25"}, {"value": "620"}],
                "in_subset": ["measurement"],
                "slot_uri": "c14:000006",
            }
        },
    )
    delta_13_c_calculation_method: Optional[Delta13CMeasurementMethod] = Field(
        default=None,
        title="Delta 13C age calculation method",
        description="""Was the radiocarbon date calculated with an AMS derived δ13C, an IRMS derived δ13C,
an alternative δ13C measurement method or an assumed δ13C""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "AMS"},
                    {"value": "IRMS"},
                    {"value": "Assumed"},
                    {"value": "Other"},
                ],
                "in_subset": ["measurement"],
                "recommended": True,
                "slot_uri": "c14:000007",
            }
        },
    )
    sample_ids: list[str] = Field(
        default=...,
        title="Sample identifiers",
        description="""Any identifier associated with the sample under measurement
(e.g. sample collection ID, archive object accession, ICOM/CIDOC Museum ID).""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "PES001"},
                    {"value": "PES001.B1010"},
                    {"value": "Des 207 d"},
                    {"value": "Grave 78"},
                    {"value": "Box 427; Exc. year 1926 (small)"},
                    {"value": "KrSp E1/2012/E1/3775"},
                    {"value": "Iceman"},
                    {"value": "Tumba XVIII"},
                ],
                "in_subset": ["sample"],
                "slot_uri": "c14:000008",
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
                "examples": [{"value": "UBERON:0002481"}, {"value": "ENVO:01000560"}],
                "in_subset": ["sample"],
                "slot_uri": "c14:000009",
                "structured_pattern": {
                    "interpolated": True,
                    "partial_match": False,
                    "syntax": "^{termID}$",
                },
            }
        },
    )
    sample_taxon_id: list[str] = Field(
        default=...,
        title="Radiocarbon dating sample taxon",
        description="""A taxonomic ID of the organism from which the sample used to extract carbon used for
radiocarbon measurement originated. The taxonomic ID should come from an established
ontology or database.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "NCBITAXON:9606"},
                    {"value": "gbif:2441105"},
                    {"value": "bold.taxonomy:786175"},
                ],
                "in_subset": ["sample"],
                "slot_uri": "c14:000010",
                "structured_pattern": {
                    "interpolated": True,
                    "partial_match": False,
                    "syntax": "^{termID}$",
                },
            }
        },
    )
    sample_taxon_id_confidence: bool = Field(
        default=...,
        title="Confidence of taxon assignment",
        description="""Specify the level of confidence of an exact taxon identification.
If secure identification, indicate TRUE, if identification is unclear or
uncertain specify FALSE.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "true"}, {"value": "false"}],
                "in_subset": ["sample"],
                "slot_uri": "c14:000011",
            }
        },
    )
    sample_taxon_scientific_name: Optional[str] = Field(
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
                    {"value": "Homo sapiens sapiens"},
                    {"value": "Capra sp."},
                    {"value": "Ulmus davidiana var. japonica"},
                ],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000012",
            }
        },
    )
    sample_anatomical_part: Optional[str] = Field(
        default=None,
        title="Anatomical part from which the sample is derived.",
        description="""Anatomical part from which the sample is derived.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "UBERON:0000981"},
                    {"value": "PO:0009010"},
                    {"value": "BTO:0001411"},
                    {"value": "UBERON:3010209"},
                ],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000013",
                "structured_pattern": {
                    "interpolated": True,
                    "partial_match": False,
                    "syntax": "^{termID}$",
                },
            }
        },
    )
    suspected_sample_contamination: Optional[bool] = Field(
        default=None,
        title="Suspected sample contamination.",
        description="""Specify whether the sample has suspected contamination that may influence measurement
(organic glue, consolidant, rootlets, embalming solution, staining etc.)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "true"}, {"value": "false"}],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000014",
            }
        },
    )
    suspected_sample_contamination_description: Optional[str] = Field(
        default=None,
        title="Suspected sample contamination description",
        description="""If a sample has a suspected contamination (suspected_sample_contamination), provide a short
description of the contamination.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "glue"},
                    {"value": "organic glue made from horse"},
                    {"value": "staining"},
                    {"value": "bitumen"},
                    {"value": "rootlets"},
                    {
                        "value": "Consolidant was applied to the skull to stabilise the "
                        "bone."
                    },
                    {
                        "value": "Sample was preserved in a embalming solution "
                        "containing formaldehyde and alcohol."
                    },
                ],
                "in_subset": ["sample"],
                "recommended": False,
                "slot_uri": "c14:000015",
            }
        },
    )
    sample_location: Optional[str] = Field(
        default=None,
        title="Sample location",
        description="""Name of location from which the sample originated""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": ""}, {"value": ""}],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000016",
            }
        },
    )
    decimal_latitude: Optional[float] = Field(
        default=None,
        title="Decimal latitude",
        description="""The geographic latitude (in decimal degrees, using the spatial reference system) of the geographic center of a dcterms:Location. Positive values are north
of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive.""",
        ge=-90,
        le=90,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "51.34254"},
                    {"value": "51.75"},
                    {"value": "-13.163"},
                ],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000017",
            }
        },
    )
    decimal_longitude: Optional[float] = Field(
        default=None,
        title="Decimal longitude",
        description="""The geographic longitude (in decimal degrees, using the spatial reference system) of the
geographic center of a dcterms:Location. Positive values are east of the Greenwich Meridian,
negative values are west of it. Legal values lie between -180 and 180, inclusive.""",
        ge=-90,
        le=90,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "12.38067"},
                    {"value": "-1.24"},
                    {"value": "-72.545"},
                ],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000018",
            }
        },
    )
    coordinate_precision: Optional[float] = Field(
        default=None,
        title="Coordinate precision",
        description="""A decimal representation of the precision of the coordinates given in the decimal_latitude
and decimal_longitude.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "0.00005"},
                    {"value": "0.001"},
                    {"value": "0.0001"},
                ],
                "in_subset": ["sample"],
                "recommended": True,
                "slot_uri": "c14:000019",
            }
        },
    )
    pretreatment_methods: list[PretreatmentMethods] = Field(
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
                    {"value": "Col"},
                    {"value": "UF_Col"},
                    {"value": "XAD"},
                    {"value": "U"},
                ],
                "in_subset": ["method"],
                "slot_uri": "c14:000020",
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
                "examples": [{"value": "No pretreatment"}, {"value": ""}],
                "in_subset": ["method"],
                "slot_uri": "c14:000021",
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
                "examples": [
                    {
                        "value": "Samples were pretreated following Brock et al. "
                        "(2010). Briefly, bone was demineralised (0.5M HCl, "
                        "overnight), washed in base (0.1M NaOH, 30 min, RT) "
                        "and acid (0.5M HCl, 1 hour, RT) before gelatinisation "
                        "(0.001M HCl, 20 hours, 70oC), filtration (Ezee(TM)) "
                        "and ultrafiltration (Vivaspin(TM) 30 kDa MWCO)"
                    },
                    {
                        "value": "A dremel drill was used to remove visibly altered "
                        "shell leaving dense translucent carbonate;  Charcoal "
                        "was treated with HCl, NaOH and HCl."
                    },
                ],
                "in_subset": ["method"],
                "slot_uri": "c14:000022",
                "structured_pattern": {
                    "interpolated": True,
                    "partial_match": False,
                    "syntax": "^{PMID}|{DOI}|{URL}|{text}$",
                },
            }
        },
    )
    measurement_method: RadiocarbonMeasurementMethod = Field(
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
                "in_subset": ["method"],
                "slot_uri": "c14:000023",
            }
        },
    )
    sample_starting_weight: float = Field(
        default=...,
        title="Sample starting weight",
        description="""Amount of sample material used at beginning of  in measurement in mg.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "521"}, {"value": "56.7"}, {"value": "1"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000024",
            }
        },
    )
    pretreatment_yield: float = Field(
        default=...,
        title="Weight after pretreatment",
        description="""Amount of sample remaining after pretreatment in mg""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "22"}, {"value": "2.3"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000025",
            }
        },
    )
    pretreatment_percentage_yield: Optional[float] = Field(
        default=None,
        title="Percentage yield after pretreatment",
        description="""Ratio of weight after pretreatment to sample starting weight""",
        ge=0,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [
                    {"value": "012"},
                    {"value": "0.61"},
                    {"value": "0.015"},
                    {"value": "0.002"},
                ],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000026",
            }
        },
    )
    carbon_proportion: float = Field(
        default=...,
        title="Carbon proportion",
        description="""Proportion of carbon in a non-proteinaceous sample used for dating (such as charcoal),
expressed as a value between 0 and 1. Used as a quality control measurement.""",
        ge=0,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.41"}, {"value": "0.12"}, {"value": "0.70"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000027",
            }
        },
    )
    delta_13_c: Optional[float] = Field(
        default=None,
        title="Delta 13C value",
        description="""The delta carbon-13 value of the sample (δ13C), which is the ratio of the stable isotope
13C to 12C, expressed in per mil (‰) notation. Used as a quality control measurement.""",
        ge=-1000,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "-21.5"}, {"value": "-13.5"}, {"value": "1.2"}],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000028",
            }
        },
    )
    delta_13_c_error: Optional[float] = Field(
        default=None,
        title="Delta 13C error",
        description="""The error associated with the delta carbon-13 (δ13C) value expressed (‰) notation.
Used as a quality control measurement.""",
        ge=0,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.1"}, {"value": "0.2"}],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000029",
            }
        },
    )
    delta_13_c_method: Optional[Delta13CMeasurementMethod] = Field(
        default=None,
        title="Delta 13C measurement method",
        description="""Which spectrophotometry method was used to measure the delta carbon-13 value,
either with Isotope Ratio Mass Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "AMS"}, {"value": "IRMS"}],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000030",
            }
        },
    )
    suspected_reservoir_effect: bool = Field(
        default=...,
        title="Suspected reservoir effect",
        description="""Specify whether there is a suspected carbon reservoir effect that
should be accounted for in analysis.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "true"}, {"value": "false"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000031",
            }
        },
    )
    carbon_nitro_ratio: float = Field(
        default=...,
        title="Carbon to nitrogen ratio",
        description="""Atomic ratio of carbon to nitrogen. Used for quality control value in
proteinaceous samples for radiocarbon dating.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "3.2"}, {"value": "3.33"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000032",
            }
        },
    )
    delta_15_n: Optional[float] = Field(
        default=None,
        title="Delta 15N value",
        description="""The delta nitrogen-15 value of the sample (δ15N), which is the ratio of the stable isotope
15N to 14N, expressed in per mil (‰) notation. Used as a quality control measurement.""",
        ge=-1000,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "10.8"}, {"value": "5.1"}, {"value": "27.2"}],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000033",
            }
        },
    )
    delta_15_n_error: Optional[float] = Field(
        default=None,
        title="Delta 15N error",
        description="""The error associated with the delta nitrogen-15 (δ15N) value expressed (‰) notation.
Used as a quality control measurement.""",
        ge=0,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.3"}, {"value": "0.12"}],
                "in_subset": ["quality control"],
                "recommended": True,
                "slot_uri": "c14:000034",
            }
        },
    )
    delta_34_s: Optional[float] = Field(
        default=None,
        title="Delta 34S value",
        description="""The delta sulfur-34 value of the sample (δ34S), which is the ratio of the stable isotope
34S to 32S, expressed in per mil (‰) notation. Used as a quality control measurement.""",
        ge=-1000,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "18.4"}, {"value": "-5.2"}],
                "in_subset": ["quality control"],
                "recommended": False,
                "slot_uri": "c14:000035",
            }
        },
    )
    delta_34_s_error: Optional[float] = Field(
        default=None,
        title="Delta 34S error",
        description="""The error associated with the delta sulfur-34 (δ34S) value expressed (‰) notation.
Used as a quality control measurement.""",
        ge=0,
        le=1000,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "0.4"}, {"value": "0.2"}],
                "in_subset": ["quality control"],
                "recommended": False,
                "slot_uri": "c14:000036",
            }
        },
    )
    recrystalisation: bool = Field(
        default=...,
        title="Evidence of recrystalisation",
        description="""Sample shows evidence of recrystalisation which should be accounted for during analysis.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RadiocarbonDate"],
                "examples": [{"value": "true"}, {"value": "false"}],
                "in_subset": ["quality control"],
                "slot_uri": "c14:000037",
            }
        },
    )

    @field_validator("lab_id")
    def pattern_lab_id(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid lab_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid lab_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_ids")
    def pattern_sample_ids(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_ids format: {v}"
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

    @field_validator("suspected_sample_contamination_description")
    def pattern_suspected_sample_contamination_description(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid suspected_sample_contamination_description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid suspected_sample_contamination_description format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("sample_location")
    def pattern_sample_location(cls, v):
        pattern = re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_location format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_location format: {v}"
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
