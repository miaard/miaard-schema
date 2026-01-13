from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'c14',
     'default_range': 'string',
     'description': 'Minimum Information about any Radiocarbon Determination',
     'id': 'https://w3id.org/MIxS-MInAS/miaard',
     'imports': ['linkml:types', 'enums/lab_code_ids'],
     'license': 'MIT',
     'name': 'miaard',
     'prefixes': {'c14': {'prefix_prefix': 'c14',
                          'prefix_reference': 'https://w3id.org/MIxS-MInAS/miaard/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://MIxS-MInAS.github.io/miaard'],
     'settings': {'DOI': {'setting_key': 'DOI',
                          'setting_value': '^https:\\/\\/doi\\.org\\/10.\\d{2,9}/.*$'},
                  'PMID': {'setting_key': 'PMID', 'setting_value': '^PMID:\\d+$'},
                  'URL': {'setting_key': 'URL',
                          'setting_value': '^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$'},
                  'termID': {'setting_key': 'termID',
                             'setting_value': '[a-zA-Z]{2,}:[a-zA-Z0-9]\\d+'}},
     'source_file': 'src/c14/schema/c14.yaml',
     'title': 'miaard'} )

class LabCodeId(str, Enum):
    """
    Enumeration of unique laboratory code designations of institutions that make radiocarbon measurements.
    """
    A = "a"
    """
    Carbon-14 Age Determination Laboratory, University of Arizona (Arizona,USA, https://ams.arizona.edu/)
    """
    AA = "aa"
    """
    Accelerator Mass Spectrometry Lab, University of Arizona (Arizona (AMS),USA, https://ams.arizona.edu/)
    """
    AAR = "aar"
    """
    Aarhus AMS Centre, Aarhus University (Aarhus, Aarhus, Denmark, https://c14websub.au.dk/)
    """
    AC = "ac"
    """
    INGEIS, University of Buenos Aires (INGEIS, Buenos Aires, Argentina, http://www.ingeis.uba.ar/)
    """
    AECV = "aecv"
    """
    Alberta Environmental Center of Vegreville (Canada)
    """
    AERIK = "aerik"
    """
    Atomic Energy Research Institute (Korea)
    """
    ALG = "alg"
    """
    Algiers (Algeria)
    """
    ANAS = "anas"
    """
    Applied Nuclear-Atomic South Science Lab (Korea)
    """
    ANL = "anl"
    """
    Argonne National Laboratory (USA)
    """
    ANTW = "antw"
    """
    Antwerp (Antwerp, Belgium)
    """
    ANU = "anu"
    """
    ANU Radiocarbon Laboratory, Australian National University (ANU, Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    ANUA = "anua"
    """
    ANU Radiocarbon Laboratory, Australian National University (AMS) (ANU (AMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    SANU = "sanu"
    """
    ANU Radiocarbon Laboratory, Australian National University (SSAMS) (ANU (SSAMS), Canberra, Australia, https://earthsciences.anu.edu.au/research/facilities/anu-radiocarbon-laboratory)
    """
    AU = "au"
    """
    University of Alaska (USA)
    """
    AURIS = "auris"
    """
    Ahmedabad (India)
    """
    Aix = "aix"
    """
    Centre de Recherche et d'Enseignement de Geosciences de l'Environment (CERAGE), Aix-en-Provence (France)
    """
    BE = "be"
    """
    Laboratory for the Analysis of Radiocarbon with AMS, University of Bern (LARA Bern, Bern, Switzerland, https://www.14c.unibe.ch/)
    """
    B = "b"
    """
    Radiocarbon Lab, Climate and Environmental Physics, University of Bern (Bern, Bern, Switzerland, https://www.climate.unibe.ch/services/services_of_cep/radiocarbon_dating/index_eng.html)
    """
    BC = "bc"
    """
    Brooklyn College (USA)
    """
    BGS = "bgs"
    """
    Brock University (Canada)
    """
    BIOCAMS = "biocams"
    """
    Miami (Miami, USA)
    """
    BM = "bm"
    """
    British Museum (London, England)
    """
    BONN = "bonn"
    """
    Universität Bonn (Bonn, Germany)
    """
    BRAMS = "brams"
    """
    University of Bristol (Bristol, UK)
    """
    BS = "bs"
    """
    Birbal Sahni Institute (India)
    """
    Ba = "ba"
    """
    Bratislava (Bratislava, Slovakia)
    """
    Beta = "beta"
    """
    Beta Analytic (USA)
    """
    Birm = "birm"
    """
    Birmingham (Birmingham, UK)
    """
    Bln = "bln"
    """
    Berlin (Berlin, Germany)
    """
    C = "c"
    """
    Chicago (Chicago, USA)
    """
    CAMS = "cams"
    """
    Lawrence Livermore National Laboratory (USA)
    """
    CAR = "car"
    """
    University College, Cardiff (Wales)
    """
    CENA = "cena"
    """
    Centro Energia Nuclear na Agricultura, Universidade de São Paulo (São Paulo, São Paulo, Brazil)
    """
    CG = "cg"
    """
    Institute of Geology (China)
    """
    CH = "ch"
    """
    Chemistry Laboratory (India)
    """
    CIRAM = "ciram"
    """
    CIRAM, Martillac (France)
    """
    CN_XX = "cn_xx"
    """
    Chinese Academy of Sciences (China)
    """
    CAN = "can"
    """
    Centro Nacional de Aceleradores (Spain)
    """
    CNL = "cnl"
    """
    Institute of Geology and Geophysics, Chinese Academy of Sciences (China)
    """
    COL = "col"
    """
    Köln AMS (Germany)
    """
    CRCA = "crca"
    """
    Cairo (Cairo, Egypt)
    """
    CRL = "crl"
    """
    Czech Radiocarbon Laboratory, Czech Academy of Sciences (Řež, Czechia, https://www.ujf.cas.cz/en/our-services/Radiocarbon_laboratory/About_us/)
    """
    CSIC = "csic"
    """
    Geochronology Lab, IQFR-CSIC, Madrid (Spain)
    """
    CSM = "csm"
    """
    Cosmochem. Lab., USSR Acad. of Sci. (USSR)
    """
    CT = "ct"
    """
    Caltech, Calif. Inst. Tech. (USA)
    """
    CU = "cu"
    """
    Department of Hydrology and Geology, Charles University (Prague, Czechia)
    """
    D = "d"
    """
    Dublin, Trinity College (Ireland)
    """
    D_AMS = "d_ams"
    """
    Direct AMS (USA)
    """
    DAL = "dal"
    """
    Radiocarbon Dating Laboratory, Dalhousie University (Dalhousie, Halifax, Canada)
    """
    DE = "de"
    """
    USGS, Denver (USA)
    """
    DEM = "dem"
    """
    NCSR Demokritos (Greece)
    """
    DGC = "dgc"
    """
    Dalhousie Geochronology Centre, Dalhousie University (Dalhousie (DGC), Halifax, Canada)
    """
    DIC = "dic"
    """
    Dicar Corp and Dicarb (USA)
    """
    DK = "dk"
    """
    Univ. de Dakar (Sénégal)
    """
    DRI = "dri"
    """
    Desert Research Institute (USA)
    """
    DSA = "dsa"
    """
    CIRCE, Caserta (Italy)
    """
    Dak = "dak"
    """
    Univ. of Dakar (Sénégal)
    """
    Deb = "deb"
    """
    Debrecen (Hungary)
    """
    DebA = "deba"
    """
    Debrecen (AMS) (Hungary)
    """
    ENEA = "enea"
    """
    ENEA, Bologna (Italy)
    """
    ETH = "eth"
    """
    Laboratory of Ion Beam Physics, ETH Zürich (ETH Zürich, Zürich, Switzerland, https://ams.ethz.ch/LIPServices/c14.html)
    """
    Erl = "erl"
    """
    Erlangen AMS Facility (Germany)
    """
    F = "f"
    """
    Florence (Italy)
    """
    FSU = "fsu"
    """
    Florida State University (USA)
    """
    FTMC = "ftmc"
    """
    Vilnius AMS Lab (Lithuania)
    """
    FZ = "fz"
    """
    Department of Physics, University of Fortaleza (Fortaleza, Fortaleza, Brazil)
    """
    Fi = "fi"
    """
    Florence INFN (Italy)
    """
    Fr = "fr"
    """
    Freiberg (Germany)
    """
    Fra = "fra"
    """
    Frankfurt (Germany)
    """
    G = "g"
    """
    Göteborg (Sweden)
    """
    GAK = "gak"
    """
    Gakushuin University (Japan)
    """
    GC = "gc"
    """
    Guiyang Institute of Geochemistry (China)
    """
    GD = "gdansk"
    """
    Gdansk (Gdansk, Poland)
    """
    GIN = "gin"
    """
    Geological Institute (Russia)
    """
    GL = "gl"
    """
    Geochronological Lab (England)
    """
    GSC = "gsc"
    """
    Geological Survey (Canada)
    """
    GU = "gu"
    """
    Scottish Universities Research & Reactor Centre (Scotland)
    """
    GV = "gv"
    """
    AMS Golden Valley, Novosibirsk (Russia)
    """
    GX = "gx"
    """
    Geochron Laboratories (USA)
    """
    GXNUAMS = "gxnuams"
    """
    Guangxi Normal Univ. AMS Lab (China)
    """
    GZ = "gz"
    """
    Key Laboratory of Isotope Geochronology and Geochemistry (Guangzhou) (China)
    """
    Gd = "gliwice"
    """
    Gliwice (Poland)
    """
    GdA = "gda"
    """
    Gliwice (Poland)
    """
    GdS = "gds"
    """
    Gliwice (Poland)
    """
    Gif = "gif"
    """
    Gif-sure-Yvette (France)
    """
    GifA = "gifa"
    """
    Gif-sure-Yvette and Orsay (France)
    """
    GrA = "gra"
    """
    Groningen AMS (Netherlands)
    """
    GrM = "grm"
    """
    Groningen AMS (Netherlands)
    """
    GrN = "grn"
    """
    Groningen (Netherlands)
    """
    GrO = "gro"
    """
    Groningen (Netherlands)
    """
    H = "h"
    """
    Heidelberg (Germany)
    """
    HAM = "ham"
    """
    Hamburg (Germany)
    """
    HAR = "har"
    """
    Harwell (England)
    """
    HIG = "hig"
    """
    Hawaii Inst. of Geophys. (USA)
    """
    HL = "hl"
    """
    Second Inst. of Oceanography (China)
    """
    HNS = "hns"
    """
    Hasleton-Nuclear, Palo Alto (USA)
    """
    Hd = "hd"
    """
    Heidelberg (Germany)
    """
    Hel = "hel"
    """
    Laboratory of Chronology, University of Helsinki (Helsinki, Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)
    """
    HelA = "hela"
    """
    Laboratory of Chronology, University of Helsinki (AMS) (Helsinki (AMS), Helsinki, Finland, https://www.helsinki.fi/en/luomus/analytical-services/radiocarbon-analyses)
    """
    Hv = "hv"
    """
    Hannover (Germany)
    """
    I = "i"
    """
    Teledyne Isotopes (USA)
    """
    IAA = "iaa"
    """
    Institute of Accelerator Analysis (beta counting) (Japan)
    """
    IAAA = "iaaa"
    """
    Institute of Accelerator Analysis (AMS) (Japan)
    """
    IAEA = "iaea"
    """
    International Atomic Energy Agency (Austria)
    """
    IAEA_MEL = "iaea_mel"
    """
    Marine Environmental Lab. (Monaco)
    """
    ICA = "ica"
    """
    International Chemical Analysis (USA)
    """
    ICEN = "icen"
    """
    Institution Tecnológico e Nuclear (Portugal)
    """
    IEMAE = "iemae"
    """
    Institute of Evolutionary Morphology & Animal Ecology (Russia)
    """
    IFAO = "ifao"
    """
    Laboratoire de Datation par le Radiocarbone, Institut français d’archéologie orientale (IFAO, Cairo, Egypt)
    """
    IGAN = "igan"
    """
    Institute of Geography (Russia)
    """
    IGS = "igs"
    """
    Institute of Geological Sciences (UK) (London, UK)
    """
    IGSB = "igsb"
    """
    Institute of Geochemistry and Geophysics, National Academy of Sciences of Belarus (Minsk, Belarus)
    """
    IHME = "ihme"
    """
    Marzeev Inst. of Hygiene Med. Ecol. (Ukraine)
    """
    II = "ii"
    """
    Isotopes, Inc., Palo Alto (USA)
    """
    IMTA = "imta"
    """
    Inst. Mexicano de Tecnología del Agua (Mexico)
    """
    IOAN = "ioan"
    """
    Inst. of Oceanography (Russia)
    """
    IOP = "iop"
    """
    Ionplus AG (Ionplus, Dietikon, Switzerland, https://www.ionplus.ch/)
    """
    IORAN = "ioran"
    """
    Institute of Oceanology (Russia)
    """
    IRPA = "irpa"
    """
    Royal Institute for Cultural Heritage (Belgium)
    """
    ISGS = "isgs"
    """
    Illinois State Geological Survey (USA)
    """
    IUACD = "iuacd"
    """
    Inter University Accelerator Centre (India)
    """
    IVAN = "ivan"
    """
    Institute of Volcanology (Ukraine)
    """
    IVIC = "ivic"
    """
    Caracas (Venezuela)
    """
    IWP = "iwp"
    """
    Institute of Water Problems (Russia)
    """
    JAT = "jat"
    """
    Tono Geoscience Center (JAEA) (Japan)
    """
    K = "k"
    """
    Copenhagen (Denmark)
    """
    KATRI = "katri"
    """
    Korea Apparel Testing (Korea)
    """
    KEEA = "keea"
    """
    Kyushu Environ. Eval. Assoc. Property Research Inst. (Japan)
    """
    KF = "kf"
    """
    State Key Laboratory of Lake Science and Environment, Chinese Academy of Sciences (China)
    """
    KGM = "kgm"
    """
    Korea Institute of Geoscience & Mineral Resources (KIGAM) (Korea)
    """
    KI = "kiel"
    """
    Kiel (Kiel, Germany)
    """
    KIA = "kia"
    """
    Kiel (AMS) (Kiel, Germany)
    """
    KIK = "kik"
    """
    Royal Institute for Cultural Heritage (Belgium)
    """
    KN = "kn"
    """
    Köln (Cologne, Germany)
    """
    KR = "kr"
    """
    Kraków (Kraków, Poland)
    """
    KRIL = "kril"
    """
    Krasnoyarsk Institute (Russia)
    """
    KSU = "ksu"
    """
    Kyoto Sangyo University (Japan)
    """
    KiLEFT_PARENTHESISKIEVRIGHT_PARENTHESIS = "kiev"
    """
    (KIEV) Institute of Radio-Geochemistry of the Environment (Kyiv, Ukraine)
    """
    L = "l"
    """
    Lamont-Doherty (USA)
    """
    LACUFF = "lacuff"
    """
    Radiocarbon Laboratory, Fluminense Federal University (Fluminense, Rio de Janeiro, Brazil, https://lac.uff.br/eng/home/)
    """
    LAEC = "laec"
    """
    Lebanese Atomic Energy Commission (LAEC) (Lebanon)
    """
    LAR = "lar"
    """
    Liège State University (Belgium)
    """
    LE = "le"
    """
    St. Petersburg (Russia)
    """
    LEMA = "lema"
    """
    Lab. de Espectrometría de Masas con Aceleradores (Mexico)
    """
    LIH = "lih"
    """
    NCSR Demokritos (Greece)
    """
    LJ = "lj"
    """
    Scripps (UCSD) La Jolla (USA)
    """
    LP = "lp"
    """
    Laboratorio de Tritio y Radiocarbono, National University of La Plata (Argentina)
    """
    LTL = "ltl"
    """
    University of Lecce (Italy)
    """
    LU = "st_petersburg"
    """
    St. Petersburg State University (Russia)
    """
    LZ = "lz"
    """
    Umweltforschungszentrum Leipzig-Halle (Germany)
    """
    LZU = "lzu"
    """
    Lanzhou University (China)
    """
    Lu = "lund"
    """
    Radiocarbon Dating Laboratory, Lund University (Lund, Sweden)
    """
    LuA = "lua"
    """
    Radiocarbon Dating Laboratory, Lund University (AMS) (Lund (AMS), Sweden)
    """
    LuS = "lus"
    """
    Radiocarbon Dating Laboratory, Lund University (SSAMS) (Lund (SSAMS), Sweden, https://www.geology.lu.se/research/laboratories-equipment/radiocarbon-dating-laboratory)
    """
    Lv = "lv"
    """
    Louvain-la-Neuve (Belgium)
    """
    Ly = "ly"
    """
    University of Lyon (France)
    """
    M = "m"
    """
    University of Michigan (USA)
    """
    MAG = "mag"
    """
    Quaternary Geology (Russia)
    """
    MAMS = "mams"
    """
    Curt-Engelhorn-Zentrum Archaeom. (Germany)
    """
    MC = "mc"
    """
    Centre Scientifique (Monaco)
    """
    METU = "metu"
    """
    Middle East Technical Univ. (Turkey)
    """
    MKL = "mkl"
    """
    Lab. of Absolute Dating (Poland)
    """
    MTC = "mtc"
    """
    University of Tokyo (Japan)
    """
    Ma = "ma"
    """
    University of Winnepeg (Canada)
    """
    N = "n"
    """
    Nishina Memorial (Japan)
    """
    NB = "nb"
    """
    Nanjing Museum (China)
    """
    NIST = "nist"
    """
    National Institute of Standards and Technology (USA)
    """
    NPL = "npl"
    """
    National Physical Laboratory, Middlesex (England)
    """
    NS = "ns"
    """
    Nova Scotia Research Foundation (Canada)
    """
    NSRL = "nsrl"
    """
    INSTAAR, University of Colorado (USA)
    """
    NSTF = "nstf"
    """
    Nuclear Science and Technology Facility, State University of New York (USA)
    """
    UNSW = "unsw"
    """
    Chronos Radiocarbon Laboratory, University of New South Wales (New South Wales, Sydney, Australia, https://www.analytical.unsw.edu.au/facilities/x-ray-facilities/radiocarbon-laboratory)
    """
    NTU = "ntu"
    """
    National Taiwan University (Taiwan)
    """
    NU = "nu"
    """
    Nihon University (Japan)
    """
    NUTA = "nuta"
    """
    Tandetron AMS Lab (Japan)
    """
    NZ = "nz"
    """
    Rafter Radiocarbon Lab (New Zealand)
    """
    NZA = "nza"
    """
    Rafter Radiocarbon Lab (AMS) (New Zealand)
    """
    Ny = "ny"
    """
    Nancy, Centre de Recherches Radiogéologiques (France)
    """
    O = "o"
    """
    Humble Oil & Refining (USA)
    """
    OBDY = "obdy"
    """
    ORSTOM Bondy (France)
    """
    OR = "or"
    """
    Research Center of Radioisotopes (Japan)
    """
    ORINS = "orins"
    """
    Oak Ridge Institute of Nuclear Studies (USA)
    """
    OS = "os"
    """
    National Ocean Sciences, AMS Facility Woods Hole Oceanographic Inst. (USA)
    """
    OWU = "owu"
    """
    Ohio Wesleyan Univ. (USA)
    """
    OX = "ox"
    """
    USDA (Oxford, Missouri) (USA)
    """
    OZ = "oz"
    """
    Centre for Accelerator Science, Australian Nuclear Science and Technology Organisation (ANSTO, Canberra, Australia, https://www.ansto.gov.au/our-facilities/centre-for-accelerator-science)
    """
    OxA = "oxa"
    """
    Oxford Radiocarbon Accelerator Unit (Oxford, England)
    """
    P = "p"
    """
    University of Pennsylvania (USA) or Max-Planck-Institut Geochronology Lab (Germany)
    """
    PAL = "pal"
    """
    Palynosurvery Co. (Japan)
    """
    PI = "permafrost_institute"
    """
    Permafrost Institute (Russia)
    """
    PIC = "pic"
    """
    Packard (USA)
    """
    PITT = "pitt"
    """
    University of Pittsburgh (USA)
    """
    PKU = "pku"
    """
    Peking University (China)
    """
    PKUAMS = "pkuams"
    """
    Peking Univ. AMS lab (China)
    """
    PL = "pl"
    """
    Purdue Rare Isotope Measurement Lab (USA)
    """
    PLD = "pld"
    """
    Paleo Labo. Co., Ltd. (Japan)
    """
    PRI = "pri"
    """
    PaleoResearch Institute (USA)
    """
    PRL = "prl"
    """
    Radiocarbon Dating Research Unit (India)
    """
    PRLCH = "prlch"
    """
    Physical Research Lab (India)
    """
    PSU = "psu"
    """
    Penn State University (USA)
    """
    PSUAMS = "psuams"
    """
    Penn State University (AMS) (USA)
    """
    Pi = "pisa"
    """
    Pisa (Italy)
    """
    Poz = "poz"
    """
    Poznan (Poland)
    """
    Pr = "pr"
    """
    Prague Czech (Republic)
    """
    Pta = "pta"
    """
    Pretoria South (Africa)
    """
    PV = "pv"
    """
    Institute of Vertebrate Paleontology and Paleoanthropology (China)
    """
    Q = "q"
    """
    Cambridge (England)
    """
    QC = "qc"
    """
    Queens College (USA)
    """
    QL = "ql"
    """
    Quaternary Isotope Lab. (USA)
    """
    QU = "qu"
    """
    Centre de Recherches Canada Minérales, (Québec)
    """
    R = "r"
    """
    Rome (Italy)
    """
    RCD = "rcd"
    """
    Radiocarbon Dating (England)
    """
    RCMib = "rcmib"
    """
    Milano Bicocca University (Italy)
    """
    RI = "ri"
    """
    Radiochemistry Inc. (USA)
    """
    RICH = "rich"
    """
    Royal Institute for Cultural Heritage (KIK-IRPA, Brussels, Belgium, https://www.kikirpa.be/en/)
    """
    RIDDL = "riddl"
    """
    Simon Fraser University (Canada)
    """
    RL = "rl"
    """
    Radiocarbon, Ltd. (USA)
    """
    RT = "rt"
    """
    Rehovot (Israel)
    """
    RTK = "rtk"
    """
    Rehovot (Israel)
    """
    RU = "ru"
    """
    Rice University (USA)
    """
    Riga = "riga"
    """
    Institute of Science (Latvia)
    """
    RoAMS = "roams"
    """
    National Institute for Physics and Nuclear Engineering (Romania)
    """
    Rome = "rome"
    """
    Dept. of Earth Sciences, Rome (Italy)
    """
    S = "s"
    """
    Saskatchewan (Canada)
    """
    SFU = "sfu"
    """
    Simon Fraser Univ. (Canada)
    """
    SH = "sh"
    """
    State Key Laboratory of Estuarine and Coastal Research (China)
    """
    SI = "si"
    """
    Smithsonian Institution (USA)
    """
    SL = "sl"
    """
    Sharp Laboratories (USA)
    """
    SM = "sm"
    """
    Mobil Oil Corp., Dallas (USA)
    """
    SMU = "smu"
    """
    Southern Methodist Univ. (USA)
    """
    SNU = "snu"
    """
    Seoul National University South (Korea)
    """
    SPb = "spb"
    """
    Herzen State University (Russia)
    """
    SUERC = "suerc"
    """
    Scottish Universities Environmental Research Centre (United Kingdom)
    """
    Sa = "sa"
    """
    Saclay, Gif-sure-Yvette (France)
    """
    Sac = "sac"
    """
    Institution Tecnológico Portugal e (Nuclear)
    """
    SacA = "saca"
    """
    Gif sure Yvette (Saclay) (France)
    """
    Sh = "shell"
    """
    Shell Development Company (USA)
    """
    T = "t"
    """
    Trondheim (Norway)
    """
    Ta = "ta"
    """
    University of Tartu (Tartu, Tartu, Estonia)
    """
    TB = "tb"
    """
    Tblisi (Georgia)
    """
    TBNC = "tbnc"
    """
    Kaman Instruments (USA)
    """
    TEM = "tem"
    """
    Temple University (USA)
    """
    TF = "tf"
    """
    Tata Institute of Fundamental Research (India)
    """
    TK = "tk"
    """
    University of Tokyo (Japan)
    """
    TKA = "tokyo_museum"
    """
    University Museum, Univ. of Tokyo (Japan)
    """
    TKU = "tku"
    """
    Turku (Finland)
    """
    TKa = "tokyo_ams"
    """
    University of Tokyo (AMS) (Japan)
    """
    TO = "to"
    """
    Isotrace Radiocarbon Facility, University of Toronto (Isotrace, Toronto, Canada)
    """
    TRa = "tra"
    """
    Trondheim (AMS) (Norway)
    """
    TUBITAK = "tubitak"
    """
    National 1MV Accelerator Mass Spectrometry Laboratory, Scientific and Technological Research Council of Turkey (TÜBİTAK, Marmara, Turkey, https://mam.tubitak.gov.tr/en/teknoloji-transfer-ofisi/national-1mv-accelerated-mass-spectroscopy-ams-laboratory)
    """
    TUNC = "tunc"
    """
    Tehran Univ. Nuclear Centre (Iran)
    """
    TUa = "tua"
    """
    Trondheim (AMS) (Norway)
    """
    Tln = "tln"
    """
    Radiocarbon Laboratory, Tallinn University of Technology (Talinn, Talinn, Estonia)
    """
    Tx = "tx"
    """
    Texas (USA)
    """
    U = "u"
    """
    Uppsala University (Uppsala, Uppsala, Sweden)
    """
    Ua = "ua"
    """
    Tandem Laboratory, Uppsala University (Uppsala (AMS), Uppsala, Sweden, https://www.uu.se/en/centre/tandemlab)
    """
    UB = "ub"
    """
    Belfast Northern (Ireland)
    """
    UBA = "uba"
    """
    Belfast Northern (AMS) (Ireland)
    """
    UBAR = "ubar"
    """
    University of Barcelona (Spain)
    """
    UCD = "ucd"
    """
    University College, Dublin (Ireland)
    """
    UCI = "uci"
    """
    Univ. of California, Irvine (USA)
    """
    UCLA = "ucla"
    """
    Univ. of California, Los Angeles (USA)
    """
    UCR = "ucr"
    """
    Univ. of California, Riverside (USA)
    """
    UD = "ud"
    """
    Udine (Italy)
    """
    UGRA = "ugra"
    """
    University of Granada (Spain)
    """
    UGa = "uga"
    """
    University of Georgia (USA)
    """
    UL = "ul"
    """
    Radiochronology Laboratory, Université Laval (Laval, Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)
    """
    ULA = "ula"
    """
    Radiochronology Laboratory, Université Laval (AMS) (Laval (AMS), Quebec, Canada, https://www.cen.ulaval.ca/en/infrastructures/radiocarbon/)
    """
    UM = "um"
    """
    University of Miami (USA)
    """
    UNAM = "unam"
    """
    National Autonomous Univ. of Mexico (Mexico)
    """
    UOC = "uoc"
    """
    André E. Lalonde National Facility in Accelerator Mass Spectrometry, University of Ottawa (Ottawa, Ottawa, Canada, https://ams.uottawa.ca/)
    """
    UQ = "uq"
    """
    Univ. of Quebec at Montréal (Canada)
    """
    URCRM = "urcrm"
    """
    Ukrainian Research Ctr. for Radiation Medicine (Ukraine)
    """
    URU = "uru"
    """
    University of Uruguay (Uruguay)
    """
    USGS = "usgs"
    """
    USGS, Menlo Park (USA)
    """
    UTCAG = "utcag"
    """
    University of Tennessee (USA)
    """
    UW = "uw"
    """
    University of Washington (USA)
    """
    UZH = "uzh"
    """
    Geochronology Group, University of Zurich (Zurich, Zurich, Switzerland, https://www.geo.uzh.ch/en/units/gch.html)
    """
    UtC = "utc"
    """
    Utrecht van de Graaff (Netherlands)
    """
    V = "v"
    """
    Melbourne, Victoria (Australia)
    """
    VERA = "vera"
    """
    Vienna Environmental Research Accelerator, University of Vienna (VERA, Vienna, Austria, https://isotopenphysik.univie.ac.at/en/)
    """
    VIE = "vie"
    """
    Higham Lab, University of Vienna (Higham Lab, Vienna, Austria, https://highamlab.univie.ac.at/)
    """
    VRI = "vri"
    """
    Vienna Radium Institute, University of Vienna (Vienna Radium Institute, Vienna, Austria)
    """
    Vs = "vs"
    """
    Vilnius, Nat. Res. Ctr. (Vilnius, Lithuania)
    """
    W = "w"
    """
    USGS, National Center (USA)
    """
    WAT = "wat"
    """
    University of Waterloo (Canada)
    """
    WB = "wb"
    """
    Institute for Preservation Technology of Cultural Relics (China)
    """
    WIS = "wis"
    """
    University of Wisconsin (USA)
    """
    WRD = "wrd"
    """
    USGS Washington, D.C. (USA)
    """
    WSU = "wsu"
    """
    Washington State Univ. (USA)
    """
    Wk = "wk"
    """
    University of Waikato (New Zealand)
    """
    X = "x"
    """
    Whitworth College (USA)
    """
    XZ = "xz"
    """
    Xinjiang Institute of Disaster Prevention and Relief (China)
    """
    XLLQ = "xllq"
    """
    Xi’an Lab. of China Loess & Quat. Geol. (China)
    """
    Y = "y"
    """
    Yale University (USA)
    """
    YU = "yu"
    """
    Yamagata University (Japan)
    """
    Ya = "ya"
    """
    Yale University (USA)
    """
    Z = "zz"
    """
    Laboratory for Low-level Radioactivities, Ruđer Bošković Institute (Zagreb, Zagreb, Croatia, https://www.irb.hr/eng/Divisions/Division-of-Experimental-Physics/Laboratory-for-Low-level-Radioactivities)
    """
    ZK = "zk"
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MIxS-MInAS/miaard'})

    lab_code: LabCodeId = Field(default=..., title="Laboratory code designation", description="""Unique laboratory code designation of the institution that made the measurement.
This is the prefix used for each determination ID. The prefix should be
derived from: https://radiocarbon.webhost.uits.arizona.edu/laboratories.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'OxA'},
                      {'value': 'CAMS'},
                      {'value': 'Beta'},
                      {'value': 'CN-XX'}],
         'slot_group': 'Identifier',
         'slot_uri': 'c14:000001'} })
    lab_id: str = Field(default=..., title="Radiocarbon determination identifier", description="""The unique identifier associated with a specific radiocarbon determination,
without the radiocarbon laboratory identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '982744'},
                      {'value': 'i238493'},
                      {'value': '9800507B'},
                      {'value': '-X-1045-13'},
                      {'value': '1415(a)'}],
         'slot_group': 'Identifier',
         'slot_uri': 'c14:000002'} })
    conventional_age: float = Field(default=..., title="Conventional radiocarbon age", description="""The uncalibrated age from the laboratory measurement. Also known as the
conventional radiocarbon age (CRA). Should be a conventional 14C age (i.e., 14C year BP)
NOT in AD/BC format. This is typically the 'raw' age reported by the radiocarbon lab, in
Before Present (BP) notation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '4500'}, {'value': '37330'}],
         'slot_group': 'Measurement',
         'slot_uri': 'c14:000005'} })
    conventional_age_error: float = Field(default=..., title="Conventional radiocarbon age error", description="""The 1-standard deviation around the conventional radiocarbon age (C14) measurement,
normally indicated as a ± after the main age. Must be in the same format (i.e. 14C yr BP).
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '25'}, {'value': '620'}],
         'slot_group': 'Measurement',
         'slot_uri': 'c14:000006'} })
    f14c: float = Field(default=..., description="""The F14C value from the laboratory measurement, i.e. the fraction modern carbon.
For older determinations, generally equivalent to \"percent modern\" (pMC, or pM) divided by 100.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.83756'}, {'value': '0.5371'}],
         'slot_group': 'Measurement',
         'slot_uri': 'c14:000003'} })
    f14c_error: float = Field(default=..., title="F14C radiocarbon error", description="""The 1-standard deviation uncertainty around the F14C (C14) measurement,
normally indicated as a ± after the main value. Must be in the same format.
Sometimes referred to as the \"error\" or \"sigma\" of the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.00434'}, {'value': '0.023843'}],
         'slot_group': 'Measurement',
         'slot_uri': 'c14:000004'} })
    delta_13_c_calculation_method: Optional[Delta13CMeasurementMethod] = Field(default=None, title="Delta 13C age calculation method", description="""Was the radiocarbon date calculated with an AMS derived δ13C, an IRMS derived δ13C,
an alternative δ13C measurement method or an assumed δ13C""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'AMS'},
                      {'value': 'IRMS'},
                      {'value': 'Assumed'},
                      {'value': 'Other'}],
         'recommended': True,
         'slot_group': 'Measurement',
         'slot_uri': 'c14:000007'} })
    sample_ids: list[str] = Field(default=..., title="Sample identifiers", description="""Any identifier associated with the sample under measurement
(e.g. sample collection ID, archive object accession, ICOM/CIDOC Museum ID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'PES001'},
                      {'value': 'PES001.B1010'},
                      {'value': 'Des 207 d'},
                      {'value': 'Grave 78'},
                      {'value': 'Box 427; Exc. year 1926 (small)'},
                      {'value': 'KrSp E1/2012/E1/3775'},
                      {'value': 'Iceman'},
                      {'value': 'Tumba XVIII'}],
         'slot_group': 'Sample',
         'slot_uri': 'c14:000008'} })
    sample_material: str = Field(default=..., title="Radiocarbon dating sample material", description="""Material of the sample used to extract carbon used for radiocarbon dating measurements.
Use ontology terms where possible, e.g. from UBERON for anatomical parts, or ENVO for other
organic samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'UBERON:0002481'}, {'value': 'ENVO:01000560'}],
         'slot_group': 'Sample',
         'slot_uri': 'c14:000009',
         'structured_pattern': {'interpolated': True,
                                'partial_match': False,
                                'syntax': '^{termID}$'}} })
    sample_taxon_id: list[str] = Field(default=..., title="Radiocarbon dating sample taxon", description="""A taxonomic ID of the organism from which the sample used to extract carbon used for
radiocarbon measurement originated. The taxonomic ID should come from an established
ontology or database.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'NCBITAXON:9606'},
                      {'value': 'gbif:2441105'},
                      {'value': 'bold.taxonomy:786175'}],
         'slot_group': 'Sample',
         'slot_uri': 'c14:000010',
         'structured_pattern': {'interpolated': True,
                                'partial_match': False,
                                'syntax': '^{termID}$'}} })
    sample_taxon_id_confidence: bool = Field(default=..., title="Confidence of taxon assignment", description="""Specify the level of confidence of an exact taxon identification.
If secure identification, indicate TRUE, if identification is unclear or
uncertain specify FALSE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'true'}, {'value': 'false'}],
         'slot_group': 'Sample',
         'slot_uri': 'c14:000011'} })
    sample_taxon_scientific_name: Optional[str] = Field(default=None, title="Scientific name of the sample taxon", description="""A scientific name of the taxon corresponding to the taxonomic ID, or when a
taxonomic ID does not currently exist for the specific taxon.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'Mammathus primigenius'},
                      {'value': 'cf Mammathus'},
                      {'value': 'Homo sapiens sapiens'},
                      {'value': 'Capra sp.'},
                      {'value': 'Ulmus davidiana var. japonica'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000012'} })
    sample_anatomical_part: Optional[str] = Field(default=None, title="Anatomical part from which the sample is derived.", description="""Anatomical part from which the sample is derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'UBERON:0000981'},
                      {'value': 'PO:0009010'},
                      {'value': 'BTO:0001411'},
                      {'value': 'UBERON:3010209'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000013',
         'structured_pattern': {'interpolated': True,
                                'partial_match': False,
                                'syntax': '^{termID}$'}} })
    suspected_sample_contamination: Optional[bool] = Field(default=None, title="Suspected sample contamination.", description="""Specify whether the sample has suspected contamination that may influence measurement
(organic glue, consolidant, rootlets, embalming solution, staining etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'true'}, {'value': 'false'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000014'} })
    suspected_sample_contamination_description: Optional[str] = Field(default=None, title="Suspected sample contamination description", description="""If a sample has a suspected contamination (suspected_sample_contamination), provide a short
description of the contamination.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'glue'},
                      {'value': 'organic glue made from horse'},
                      {'value': 'staining'},
                      {'value': 'bitumen'},
                      {'value': 'rootlets'},
                      {'value': 'Consolidant was applied to the skull to stabilise the '
                                'bone.'},
                      {'value': 'Sample was preserved in a embalming solution '
                                'containing formaldehyde and alcohol.'}],
         'recommended': False,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000015'} })
    sample_location: Optional[str] = Field(default=None, title="Sample location", description="""Name of location from which the sample originated""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': ''}, {'value': ''}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000016'} })
    decimal_latitude: Optional[float] = Field(default=None, title="Decimal latitude", description="""The geographic latitude (in decimal degrees, using the spatial reference system) of the geographic center of a dcterms:Location. Positive values are north
of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive.""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '51.34254'}, {'value': '51.75'}, {'value': '-13.163'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000017'} })
    decimal_longitude: Optional[float] = Field(default=None, title="Decimal longitude", description="""The geographic longitude (in decimal degrees, using the spatial reference system) of the
geographic center of a dcterms:Location. Positive values are east of the Greenwich Meridian,
negative values are west of it. Legal values lie between -180 and 180, inclusive.""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '12.38067'}, {'value': '-1.24'}, {'value': '-72.545'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000018'} })
    coordinate_precision: Optional[float] = Field(default=None, title="Coordinate precision", description="""A decimal representation of the precision of the coordinates given in the decimal_latitude
and decimal_longitude.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.00005'}, {'value': '0.001'}, {'value': '0.0001'}],
         'recommended': True,
         'slot_group': 'Sample',
         'slot_uri': 'c14:000019'} })
    pretreatment_methods: list[PretreatmentMethods] = Field(default=..., title="Radiocarbon pretreatment methods", description="""Specify the types of general pretreatment methods applied for decontamination.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'ABA'},
                      {'value': 'A'},
                      {'value': 'BABA'},
                      {'value': 'Col'},
                      {'value': 'UF_Col'},
                      {'value': 'XAD'},
                      {'value': 'U'}],
         'slot_group': 'Method',
         'slot_uri': 'c14:000020'} })
    pretreatment_method_description: str = Field(default=..., title="Radiocarbon pretreatment method description", description="""Description of specific pretreatment method used for decontamination of sample prior determination.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'No pretreatment'}, {'value': ''}],
         'slot_group': 'Method',
         'slot_uri': 'c14:000021'} })
    pretreatment_method_protocol: list[str] = Field(default=..., title="Radiocarbon pretreatment method protocol", description="""A DOI or URL to a publication describing the specific method of pretreatment applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'Samples were pretreated following Brock et al. '
                                '(2010). Briefly, bone was demineralised (0.5M HCl, '
                                'overnight), washed in base (0.1M NaOH, 30 min, RT) '
                                'and acid (0.5M HCl, 1 hour, RT) before gelatinisation '
                                '(0.001M HCl, 20 hours, 70oC), filtration (Ezee(TM)) '
                                'and ultrafiltration (Vivaspin(TM) 30 kDa MWCO)'},
                      {'value': 'A dremel drill was used to remove visibly altered '
                                'shell leaving dense translucent carbonate;  Charcoal '
                                'was treated with HCl, NaOH and HCl.'}],
         'slot_group': 'Method',
         'slot_uri': 'c14:000022',
         'structured_pattern': {'interpolated': True,
                                'partial_match': False,
                                'syntax': '^{PMID}|{DOI}|{URL}|{text}$'}} })
    measurement_method: RadiocarbonMeasurementMethod = Field(default=..., title="Radiocarbon measurement method", description="""Type of measurement method the determination was made by.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'AMS'}, {'value': 'Conventional'}, {'value': 'PIMS'}],
         'slot_group': 'Method',
         'slot_uri': 'c14:000023'} })
    sample_starting_weight: float = Field(default=..., title="Sample starting weight", description="""Amount of sample material used at beginning of  in measurement in mg.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '521'}, {'value': '56.7'}, {'value': '1'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000024'} })
    pretreatment_yield: float = Field(default=..., title="Weight after pretreatment", description="""Amount of sample remaining after pretreatment in mg""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '22'}, {'value': '2.3'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000025'} })
    pretreatment_percentage_yield: Optional[float] = Field(default=None, title="Percentage yield after pretreatment", description="""Ratio of weight after pretreatment to sample starting weight""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '012'},
                      {'value': '0.61'},
                      {'value': '0.015'},
                      {'value': '0.002'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000026'} })
    carbon_proportion: float = Field(default=..., title="Carbon proportion", description="""Proportion of carbon in a non-proteinaceous sample used for dating (such as charcoal),
expressed as a value between 0 and 1. Used as a quality control measurement.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.41'}, {'value': '0.12'}, {'value': '0.70'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000027'} })
    delta_13_c: Optional[float] = Field(default=None, title="Delta 13C value", description="""The delta carbon-13 value of the sample (δ13C), which is the ratio of the stable isotope
13C to 12C, expressed in per mil (‰) notation. Used as a quality control measurement.""", ge=-1000, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '-21.5'}, {'value': '-13.5'}, {'value': '1.2'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000028'} })
    delta_13_c_error: Optional[float] = Field(default=None, title="Delta 13C error", description="""The error associated with the delta carbon-13 (δ13C) value expressed (‰) notation.
Used as a quality control measurement.""", ge=0, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.1'}, {'value': '0.2'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000029'} })
    delta_13_c_method: Optional[Delta13CMeasurementMethod] = Field(default=None, title="Delta 13C measurement method", description="""Which spectrophotometry method was used to measure the delta carbon-13 value,
either with Isotope Ratio Mass Spectrometer (IRMS) or Accelerated Mass Spectrometer (AMS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'AMS'}, {'value': 'IRMS'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000030'} })
    suspected_reservoir_effect: bool = Field(default=..., title="Suspected reservoir effect", description="""Specify whether there is a suspected carbon reservoir effect that
should be accounted for in analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'true'}, {'value': 'false'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000031'} })
    carbon_nitro_ratio: float = Field(default=..., title="Carbon to nitrogen ratio", description="""Atomic ratio of carbon to nitrogen. Used for quality control value in
proteinaceous samples for radiocarbon dating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '3.2'}, {'value': '3.33'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000032'} })
    delta_15_n: Optional[float] = Field(default=None, title="Delta 15N value", description="""The delta nitrogen-15 value of the sample (δ15N), which is the ratio of the stable isotope
15N to 14N, expressed in per mil (‰) notation. Used as a quality control measurement.""", ge=-1000, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '10.8'}, {'value': '5.1'}, {'value': '27.2'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000033'} })
    delta_15_n_error: Optional[float] = Field(default=None, title="Delta 15N error", description="""The error associated with the delta nitrogen-15 (δ15N) value expressed (‰) notation.
Used as a quality control measurement.""", ge=0, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.3'}, {'value': '0.12'}],
         'recommended': True,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000034'} })
    delta_34_s: Optional[float] = Field(default=None, title="Delta 34S value", description="""The delta sulfur-34 value of the sample (δ34S), which is the ratio of the stable isotope
34S to 32S, expressed in per mil (‰) notation. Used as a quality control measurement.""", ge=-1000, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '18.4'}, {'value': '-5.2'}],
         'recommended': False,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000035'} })
    delta_34_s_error: Optional[float] = Field(default=None, title="Delta 34S error", description="""The error associated with the delta sulfur-34 (δ34S) value expressed (‰) notation.
Used as a quality control measurement.""", ge=0, le=1000, json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': '0.4'}, {'value': '0.2'}],
         'recommended': False,
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000036'} })
    recrystalisation: bool = Field(default=..., title="Evidence of recrystalisation", description="""Sample shows evidence of recrystalisation which should be accounted for during analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDate'],
         'examples': [{'value': 'true'}, {'value': 'false'}],
         'slot_group': 'Quality control',
         'slot_uri': 'c14:000037'} })

    @field_validator('lab_id')
    def pattern_lab_id(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid lab_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid lab_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_ids')
    def pattern_sample_ids(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_ids format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_taxon_scientific_name')
    def pattern_sample_taxon_scientific_name(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_taxon_scientific_name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_taxon_scientific_name format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('suspected_sample_contamination_description')
    def pattern_suspected_sample_contamination_description(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid suspected_sample_contamination_description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid suspected_sample_contamination_description format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_location')
    def pattern_sample_location(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_location format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_location format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pretreatment_method_description')
    def pattern_pretreatment_method_description(cls, v):
        pattern=re.compile(r"")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pretreatment_method_description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pretreatment_method_description format: {v}"
            raise ValueError(err_msg)
        return v


class RadiocarbonDateCollection(ConfiguredBaseModel):
    """
    A collection of radiocarbon determinations with associated metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MIxS-MInAS/miaard', 'tree_root': True})

    entries: Optional[list[RadiocarbonDate]] = Field(default=[], description="""A list of multiple radiocarbon determinations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RadiocarbonDateCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RadiocarbonDate.model_rebuild()
RadiocarbonDateCollection.model_rebuild()
