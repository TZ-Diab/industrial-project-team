# Technical standards regimes — which codes apply once the country is defined

## What this file is for

The role sheets are written **code-agnostic**: they name the *families* of standards a trade relies on (structural loads, pressure equipment, process piping, electrical installation, hazardous areas, functional safety, process safety, environmental permitting, construction safety, welding and material certification, contract forms). **Which set actually applies is decided by the project country** — and this file is the map: 24 regime columns covering the major industrial markets, and a rule for any other country. As soon as a project country is defined, every role reads its column below (and the country card, if one exists) before quoting a code. No column is a default: a project with no country defined gets the question, not an assumption.

Rules of use:
- The entries are **reference points**, not a legal opinion: codes are revised, adopted, withdrawn; national annexes and local authorities add requirements. Confirm with the local engineer of record, the authority having jurisdiction and the owner's standards before committing.
- **Owner and licensor standards sit on top** of the national regime (a major's engineering practices, a licensor's basis of design) and often decide which international code is used where the national one is silent.
- **Two regimes can coexist** on one project: national building and electrical codes on the site, ASME/API/ISO on the process units, IEC on the instrumentation — say which applies to what.
- Units follow the regime: SI almost everywhere, **US customary in the United States** (and in some Gulf operator specifications) — every interface document states its units.

## The regime map

| Discipline | EU / EEA (`eu`) | United Kingdom (`uk`) | United States (`us`) | Canada (`ca`) | Australia / NZ (`au-nz`) |
|---|---|---|---|---|---|
| Structural loads, concrete, steel, seismic | Eurocodes EN 1990–1999 **with national annexes**; EN product standards | Eurocodes with UK NA + BS; Building Regulations (Approved Docs) | IBC; ASCE 7 (loads); ACI 318 (concrete); AISC 360 (steel); ASCE 41 / IBC seismic | NBC + provincial codes; CSA A23.3 (concrete); CSA S16 (steel) | AS/NZS 1170 (loads); AS 3600 (concrete); AS 4100 (steel); NZS 1170.5 (seismic) |
| Geotechnical | EN 1997 (EC7) + national practice | EC7 + BS 5930 / BS 8004 | ASCE / local practice; AASHTO (linear works) | CFEM (Canadian Foundation Engineering Manual) | AS 2159 (piling); AS 1726 (site investigation) |
| Pressure equipment, boilers, tanks | PED 2014/68/EU; EN 13445 (vessels), EN 12952/12953 (boilers), EN 14015 (tanks); ASME accepted with PED conformity | PESR 2016 (UKCA) + PSSR 2000; BS EN / ASME | ASME BPVC (VIII vessels, I boilers); API 650/620 (tanks); state boiler laws; NBIC | CSA B51 + ASME BPVC with **CRN registration** per province | AS 1210 (vessels); AS 1228 (boilers); AS 1692 (tanks); AS 4343 (hazard levels) |
| Process piping, pipelines | EN 13480 (with PED); ASME B31.3 widely used; EN 1594 / EN 12007 (gas pipelines) | BS EN 13480 / ASME B31.3; IGEM standards (gas) | ASME B31.1 / B31.3; B31.4 / B31.8 (pipelines); 49 CFR 192/195 | ASME B31.3; CSA Z662 (oil & gas pipelines) | AS 4041 (piping); AS 2885 (pipelines) |
| Electrical installation, HV, grid | IEC 60364 / HD 60364 (LV); IEC 61936-1 / EN 50522 (HV); ENTSO-E network codes (RfG, DCC) + national grid codes | BS 7671 (IET Wiring Regulations); BS EN 61936; GB Grid Code, G99 / G98 | NEC (NFPA 70); NFPA 70E; IEEE C2 (NESC); IEEE 1547 / 2800; FERC / NERC + ISO/RTO interconnection | CEC (CSA C22.1); CSA Z462; provincial utility interconnection rules | AS/NZS 3000 (Wiring Rules); AS 2067 (HV); National Electricity Rules (NER), AEMO |
| Hazardous areas | ATEX 2014/34/EU + 1999/92/EC; IEC / EN 60079 (zones) | DSEAR 2002; BS EN 60079 | NEC Articles 500–506 (Class/Division or Zone); NFPA 497 / 499; API RP 500 / 505 | CEC Section 18; CSA C22.2 | AS/NZS 60079 |
| Instrumentation, functional safety | IEC 61511 / 61508; IEC 62443 (OT cyber); EN 50110 | IEC 61511; HSE guidance | ANSI/ISA 61511; ISA 84; ISA/IEC 62443 | IEC 61511 | AS IEC 61511 |
| Process safety, major hazards | Seveso III (2012/18/EU); IED (2010/75/EU) + BAT conclusions; EN 1127 | COMAH 2015; HSE regulation | OSHA PSM (29 CFR 1910.119); EPA RMP (40 CFR 68); NFPA codes | Provincial regulations; CSA Z767 (process safety management) | WHS Regulations — Major Hazard Facilities (MHF); state regulators |
| Environmental permitting, impact assessment | EIA Directive 2011/92/EU (as amended); national transposition (permit unique, BImSchG, ICPE, decyzja środowiskowa…) | EIA Regulations 2017; Environmental Permitting Regulations (EPR) 2016; planning permission | NEPA (federal nexus); Clean Air Act (Title V, NSR/PSD); Clean Water Act; state permits | Impact Assessment Act 2019; provincial EA processes | EPBC Act 1999 (federal matters); state EIA / development approvals |
| Construction safety | Directive 92/57/EEC (H&S coordinator) + national (SPS, SiGeKo, CDM-like) | CDM Regulations 2015 | OSHA 29 CFR 1926 | Provincial OHS Acts | WHS Act 2011 + Regulations |
| Welding, NDT, material certification | ISO 15614 / ISO 9606; EN 10204 3.1 / 3.2; ISO 17636 etc.; PED essential requirements | BS EN ISO; PESR | ASME IX; AWS D1.1; ASNT SNT-TC-1A; MTRs per ASTM | CSA W47.1 / W59; CWB certification | AS/NZS 1554; AS 4037 (pressure welding) |
| Contract forms (default usage) | FIDIC; national forms (VOB/B DE, CCAG FR public, UAV NL…) | NEC4; JCT; FIDIC (international) | AIA; ConsensusDocs; EJCDC; bespoke EPC | CCDC | AS 4000 / AS 4902; FIDIC |
| Units, language | SI; national language for permits | SI; English | **US customary** (psi, °F, ft); English | SI (dual common); English / French (QC) | SI; English |

| Discipline | Gulf / GCC (`gcc`) | India (`in`) | China (`cn`) | Japan (`jp`) | Brazil (`br`) |
|---|---|---|---|---|---|
| Structural loads, concrete, steel, seismic | Local building codes largely US-derived: Saudi Building Code (SBC), Abu Dhabi / Dubai codes, Qatar QCS — IBC / ACI / ASCE families | NBC 2016; IS 875 (loads); IS 456 (concrete); IS 800 (steel); IS 1893 (seismic) | GB 50009 (loads); GB 50010 (concrete); GB 50017 (steel); GB 50011 (seismic) | Building Standard Act; AIJ standards; JIS | ABNT NBR 6118 (concrete); NBR 8800 (steel); NBR 6123 (wind) |
| Geotechnical | Local practice, US / BS methods; operator specs | IS 6403; IS 1904 | GB 50007; GB 50021 (investigation) | JGS standards; Building Standard Act | NBR 6122 (foundations); NBR 6484 (SPT) |
| Pressure equipment, boilers, tanks | ASME BPVC / API dominant; operator standards (Aramco SAES, ADNOC, QatarEnergy) | IBR 1950 (boilers, mandatory); IS 2825 / ASME VIII (vessels); PESO approvals for petroleum / gas | TSG 21 (special equipment safety regulation); GB/T 150 (vessels); manufacturing licences | High Pressure Gas Safety Act; JIS B 8265 / B 8267; KHK standards | NR-13 (boilers and vessels); ASME BPVC |
| Process piping, pipelines | ASME B31.3 / B31.4 / B31.8; operator specs | ASME B31.3 common; OISD standards (petroleum); PNGRB (gas pipelines) | GB/T 20801 (process piping); GB 50316; GB 50251 (gas pipelines) | JIS / JPI standards; High Pressure Gas Safety Act | ASME B31.3 / B31.4; NBR / Petrobras N-standards |
| Electrical installation, HV, grid | IEC in most GCC states (DEWA, ADDC, Kahramaa regulations); NEC influence in some KSA / Aramco specs; SEC grid code | CEA Regulations (safety & electric supply); IS / IEC 60364; IS 3043 (earthing); CEA connectivity standards; IEGC | GB 50054 / GB 50060; GB 50052; grid codes GB/T 19963 (wind), GB/T 19964 (PV) | Electricity Business Act; JEAC / JIS C; **50 Hz east / 60 Hz west**; utility interconnection rules, OCCTO | NBR 5410 (LV); NBR 14039 (MV); NR-10; ONS grid procedures, ANEEL / PRODIST |
| Hazardous areas | IEC 60079 (some NEC); operator specs | IS / IEC 60079; PESO licensing | GB 50058; GB 3836 | JIS C 60079; Fire Service Act (hazardous materials) | NBR IEC 60079; NR-20 |
| Instrumentation, functional safety | IEC 61511; operator standards | IEC 61511 | GB/T 21109 (IEC 61511 adoption) | JIS C 0511 | IEC 61511 |
| Process safety, major hazards | Operator process safety standards; HCIS (KSA high-commission security); civil defence approvals | MSIHC Rules 1989; Factories Act 1948; OISD | Work Safety Law; hazardous chemicals regulation (State Council Decree 591); safety pre-assessment and acceptance | Industrial Safety and Health Act; High Pressure Gas Safety Act | NR-20; state civil defence; CETESB (SP) |
| Environmental permitting, impact assessment | National EIA: NCEC (KSA), EAD / Dubai Municipality (UAE), MECC (Qatar), EA (Oman) | EIA Notification 2006 (MoEFCC); CTE / CTO from State Pollution Control Boards | EIA Law; MEE approval (环评); "three simultaneities" | Environmental Impact Assessment Act; prefectural ordinances | CONAMA resolutions; licensing LP → LI → LO (IBAMA / state agencies) |
| Construction safety | Operator HSE standards; labour laws; civil defence | BOCW Act 1996; Factories Act | Construction safety regulations (MOHURD) | Industrial Safety and Health Act | NR-18 |
| Welding, NDT, material certification | ASME IX; AWS; operator specs | ASME IX / AWS / IS; IBR welder approvals | GB / NB/T 47014; TSG requirements | JIS Z 3801 / 3841 | ASME IX; AWS; FBTS qualification |
| Contract forms (default usage) | FIDIC (heavily amended); local law and courts / DIFC / QICDRC | FIDIC (often); CPWD / PPP model forms | MOHURD construction contract model; FIDIC for foreign parties | Four Associations standard form; FIDIC rare | Bespoke EPC; Petrobras / utility forms |
| Units, language | SI (US customary in some operator specs); English + Arabic for permits | SI; English (+ local languages) | SI; **Chinese mandatory** for approvals | SI; Japanese | SI; Portuguese |

| Discipline | South Africa (`za`) | International oil & gas / offshore default (`intl-og`) | Norway (`no`) | Switzerland (`ch`) |
|---|---|---|---|---|
| Structural loads, concrete, steel, seismic | SANS 10160 (loads); SANS 10100 (concrete); SANS 10162 (steel) | Owner / IOC standards on top of ISO 19900 series (offshore), API RP 2A, DNV, NORSOK (North Sea) | Eurocodes with Norwegian NA (NS-EN); NORSOK N-001 / N-003 (offshore structures); DNV | SIA 260–267 (Eurocode-aligned; SIA 261 loads and seismic, SIA 262 concrete, SIA 263 steel) |
| Geotechnical | SANS 10161 | ISO 19901-4; API RP 2GEO | EC7 with Norwegian NA; NGI practice | SIA 267 |
| Pressure equipment, boilers, tanks | OHS Act Pressure Equipment Regulations 2009; SANS 347; ASME / EN accepted | ASME BPVC; API 650 / 620; ISO 16528 | PED via EEA; NS-EN 13445; NORSOK M-001 / R-002 | Pressure Equipment Ordinance (DGVV, PED-aligned); SVTI inspection; SN EN 13445 |
| Process piping, pipelines | ASME B31.3; SANS 347 | ASME B31.3; API 5L; ISO 13623 (pipelines) | NS-EN 13480 / ASME B31.3; NORSOK L-001 / L-002; DNV-ST-F101 (subsea) | SN EN 13480 / ASME B31.3 |
| Electrical installation, HV, grid | SANS 10142; OHS Act Electrical Installation Regulations; NERSA Grid Code | IEC 60364 / 61936; IEC 61892 (offshore) | NEK 400 (IEC 60364); FSE regulations; NORSOK E-001; Statnett grid code, NVE regulator | NIN / SN 411000 (IEC 60364-based); ESTI; Swissgrid, ElCom regulator |
| Hazardous areas | SANS 60079 | IEC 60079; API RP 505 | ATEX (EEA); IEC 60079 | ATEX-aligned ordinances; SN EN 60079; SUVA |
| Instrumentation, functional safety | IEC 61511 | IEC 61511; ISO 10418 | IEC 61511; NORSOK I-002 / S-001 | IEC 61511 |
| Process safety, major hazards | Major Hazard Installation Regulations (OHS Act) | ISO 17776; API RP 75 (SEMS); operator process safety management | Major Accident Regulation (Seveso III via EEA); Havtil (petroleum safety authority) for petroleum | Major Accidents Ordinance (StFV / OPAM); cantonal enforcement |
| Environmental permitting, impact assessment | NEMA 1998 + EIA Regulations 2014 | Host-country EIA + IFC Performance Standards / Equator Principles when financed | Planning and Building Act; Pollution Control Act permits (Miljødirektoratet); EIA regulations | Environmental Protection Act; EIA Ordinance (UVPV); cantonal permits |
| Construction safety | Construction Regulations 2014 (OHS Act) | Operator HSE management system; ISO 45001 | Client Regulations (Byggherreforskriften, Directive 92/57); Working Environment Act | Construction Work Ordinance (BauAV); SUVA |
| Welding, NDT, material certification | SANS / ISO; SAIW | ASME IX; ISO 15614; EN 10204 3.1 / 3.2 | NS-EN ISO; NORSOK M-101 / M-601 | SN EN ISO; SVS |
| Contract forms (default usage) | JBCC; NEC3 / NEC4; GCC 2015; FIDIC | FIDIC Silver / Yellow (amended); bespoke IOC forms | NS 8405 / 8407 (onshore construction); NTK / NF (offshore fabrication) | SIA 118 (general conditions); Code of Obligations |
| Units, language | SI; English | SI with dual units on interfaces; English | SI; Norwegian, English widely accepted | SI; German / French / Italian by canton |

| Discipline | Turkey (`tr`) | Egypt (`eg`) | Francophone Africa (`africa-fr`) | Anglophone Africa (`africa-en`) |
|---|---|---|---|---|
| Structural loads, concrete, steel, seismic | TS EN (Eurocode-aligned) with Turkish NA; TBDY 2018 (seismic); TS 498 (loads); TS 500 (concrete) | ECP (Egyptian Code of Practice): ECP 201 (loads and seismic), ECP 203 (concrete), ECP 205 (steel) | Eurocodes / French standards (NF, DTU) commonly referenced; national annexes rarely published → the annex used must be stated | BS (legacy, e.g. BS 8110) and Eurocodes via national adoption (KS EN Kenya…); SANS influence in Southern Africa |
| Geotechnical | TBDY; TS EN 1997 | ECP 202 | EC7 / French practice (PMT frequent) | BS 5930 / EC7; SANS 10161 (south) |
| Pressure equipment, boilers, tanks | PED transposed (Pressure Equipment Regulation); TSE certification; ASME accepted | ASME; EOS (Egyptian Organization for Standardization) | EU / French rules referenced; ASME in oil & gas | ASME / BS; national boiler regulations |
| Process piping, pipelines | TS EN 13480 / ASME B31.3; BOTAŞ specs (gas) | ASME B31.3 / B31.8; GASCO / EGAS specs | ASME / EN | ASME |
| Electrical installation, HV, grid | Electrical Indoor Installations Regulation; TS HD 60364; TEİAŞ (TSO), EPDK regulator, distribution companies | ECP electrical code (IEC-based); EETC (transmission) / EEHC; EgyptERA regulator; Egyptian Transmission Grid Code | NF C 15-100 / IEC 60364 referenced; national utilities (SENELEC, CIE, SONABEL…); regional pools (WAPP) | BS 7671 / IEC 60364 referenced; national regulators and grid codes (NERC Nigeria, EPRA Kenya, GRIDCo Ghana) |
| Hazardous areas | ATEX transposed; TS EN 60079 | IEC 60079 | ATEX / IEC 60079 | IEC 60079 |
| Instrumentation, functional safety | IEC 61511 | IEC 61511 | IEC 61511 | IEC 61511 |
| Process safety, major hazards | Major Industrial Accidents Regulation (Seveso transposition) | Environmental Law 4/1994; Civil Defence approvals | National environmental and hydrocarbons codes; operator standards | National factories / OSH acts; operator standards |
| Environmental permitting, impact assessment | EIA Regulation (ÇED); Ministry of Environment, Urbanisation and Climate Change | EEAA (Egyptian Environmental Affairs Agency) EIA | National environmental codes and EIA (étude d'impact); ministries of environment | NEMA-type agencies (NESREA Nigeria, NEMA Kenya, EPA Ghana) |
| Construction safety | OSH Law 6331; Construction Works OSH Regulation | Labour Law 12/2003 | National labour codes; OHADA framework | National OSH acts |
| Welding, NDT, material certification | TS EN ISO | ASME IX / AWS | EN / ASME | BS / ASME |
| Contract forms (default usage) | FIDIC (international); Code of Obligations; Public Procurement Law 4734 | FIDIC (widely used); Public Procurement Law 182/2018 | OHADA Uniform Acts; FIDIC (donor-funded: World Bank, AfDB); CCAG-type public forms | FIDIC (dominant on donor projects); JBCC (Southern Africa) |
| Units, language | SI; Turkish | SI; Arabic (permits) / English | SI; French | SI; English |

| Discipline | Singapore (`sg`) | Malaysia (`my`) | Indonesia (`id`) | South Korea (`kr`) |
|---|---|---|---|---|
| Structural loads, concrete, steel, seismic | SS EN Eurocodes with Singapore NA; BCA approval | MS EN Eurocodes with Malaysian NA; Uniform Building By-Laws (UBBL) | SNI (ASCE / ACI / AISC-derived): SNI 1727 (loads), SNI 2847 (concrete), SNI 1729 (steel), SNI 1726 (seismic) | KDS / KCS (Korea Design / Construction Standards); KBC; seismic KDS 41 17 |
| Geotechnical | SS EN 1997 | MS EN 1997 | SNI 8460 | KDS 11 |
| Pressure equipment, boilers, tanks | WSH (Workplace Safety and Health) regulations — authorised examiners; SS / ASME | DOSH design approval (OSH Act, ex-FMA 1967); ASME / BS | Ministry of Manpower (Permenaker) regulations; MIGAS approvals for oil & gas; ASME / API | High-Pressure Gas Safety Control Act (KGS codes); Energy Use Rationalization Act (boilers); KOSHA; ASME accepted |
| Process piping, pipelines | ASME B31.3 | ASME B31.3 | ASME B31.3; MIGAS | ASME B31.3; KGS |
| Electrical installation, HV, grid | SS 638 (electrical installations); EMA licensing; SP PowerGrid, Transmission Code | Electricity Supply Act 1990 / Regulations 1994; MS IEC 60364; Suruhanjaya Tenaga; TNB Grid Code (Peninsular), SESB / SEB | PUIL 2011 (IEC 60364-based); SLO certificate; ESDM; PLN Grid Code (Aturan Jaringan) | KEC (Korea Electrical Code, IEC-based, 2021); KESCO inspections; KEPCO grid rules, KPX |
| Hazardous areas | SS 60079 / IEC | MS IEC 60079; DOSH | SNI IEC 60079 | KS C IEC 60079 |
| Instrumentation, functional safety | IEC 61511 | IEC 61511 | IEC 61511 | IEC 61511; KOSHA guides |
| Process safety, major hazards | Major Hazard Installations regulations (WSH); SCDF / NEA | CIMAH Regulations 1996 (major accident hazards); DOSH | Permenaker; MIGAS; BNPB | PSM under the OSH Act; Chemical Substances Control Act (off-site consequence analysis) |
| Environmental permitting, impact assessment | NEA / URA planning; EIA case-by-case | Environmental Quality Act 1974; DOE EIA | AMDAL / UKL-UPL (Ministry of Environment KLHK); OSS licensing | Environmental Impact Assessment Act (Ministry of Environment) |
| Construction safety | WSH Act; Design for Safety regulations | OSH Act 1994; CIDB | Construction Services Law 2/2017; SMK3 | OSH Act; Serious Accidents Punishment Act 2022 |
| Welding, NDT, material certification | ISO / ASME | ASME / MS | ASME / AWS; BNSP certification | KS / ASME |
| Contract forms (default usage) | PSSCOC (public); SIA / REDAS forms; FIDIC | PAM; PWD 203A (public); FIDIC | FIDIC (international); local forms | MOLIT standard forms; FIDIC overseas |
| Units, language | SI; English | SI; Malay / English | SI; **Bahasa Indonesia mandatory** for contracts (Law 24/2009) | SI; Korean |

| Discipline | Mexico (`mx`) | Chile (`cl`) |
|---|---|---|
| Structural loads, concrete, steel, seismic | NTC (Normas Técnicas Complementarias, CDMX) and state codes; CFE Manual de Diseño de Obras Civiles (seismic, wind) | NCh 1537 (loads); NCh 430 (concrete); NCh 427 (steel); NCh 433 (seismic, buildings); **NCh 2369 (seismic, industrial)**; OGUC |
| Geotechnical | NTC | NCh 433 / NCh 3394 |
| Pressure equipment, boilers, tanks | NOM-020-STPS (pressure vessels); ASME | DS 10/2012 (boilers and pressure vessels); ASME |
| Process piping, pipelines | ASME B31.3; NOM for hydrocarbons (ASEA) | ASME B31.3 |
| Electrical installation, HV, grid | NOM-001-SEDE (NEC-based); CRE regulator; CENACE (grid operator); CFE; Código de Red | SEC regulations; RIC (Reglamento de Instalaciones de Consumo, 2020); NSEG; Coordinador Eléctrico Nacional (CEN); NTSyCS |
| Hazardous areas | NOM-001-SEDE Art. 500 (NEC Class / Division) | IEC 60079 / NEC (mixed practice) |
| Instrumentation, functional safety | ISA / IEC 61511 | IEC 61511 |
| Process safety, major hazards | NOM-028-STPS (process safety); ASEA (hydrocarbons) | DS 43 (hazardous substances storage); Seremi de Salud |
| Environmental permitting, impact assessment | MIA (Manifestación de Impacto Ambiental) — SEMARNAT; ASEA for hydrocarbons | SEIA (Law 19.300); SEA |
| Construction safety | NOM-031-STPS | Law 16.744; DS 594 |
| Welding, NDT, material certification | ASME IX / AWS | ASME IX / AWS |
| Contract forms (default usage) | Public works law forms; bespoke; FIDIC rare | Bespoke; concessions law; FIDIC occasional |
| Units, language | SI (US customary influence); Spanish | SI; Spanish |

## Any other country

Start from the nearest column (same code family: Eurocodes, ASCE/ACI/AISC, BS, GB…), name the local codes as "to be confirmed", and create the country card with `new-country`. Common anchors: Gulf-neighbouring and Central Asian markets often mix EU/IEC and US/API practice under operator standards; Latin American markets outside Mexico and Chile follow ASCE/ACI-derived national codes with ASME/API in oil & gas; South Asian markets outside India follow BS / IS lineages.

## How each role uses this file

- **Civil / structural, geotechnical**: the loads-concrete-steel-seismic row, always with the **national annex or local seismic map** — never a calculation under another country's annex.
- **Mechanical, piping, materials**: the pressure-equipment and piping rows decide the design code, the third-party inspection body (notified body, ASME AI, TSG) and the manufacturing licences; the certification row decides what a material certificate must show.
- **Electrical, instrumentation, DCS**: the electrical row decides the installation code, the hazardous-area system (Zone vs Class/Division), the grid code; the functional-safety row is near-universal (IEC 61511) but the enforcement body is national.
- **HSE, technical safety, permitting**: the process-safety and permitting rows decide the regime (Seveso / COMAH / PSM / MHF…), the authority and the calendar — the axis that changes most at the border.
- **Construction manager, quality**: the construction-safety and welding rows decide site rules, welder qualifications and NDT personnel certification.
- **Contract manager, procurement, financing**: the contract row decides the default form and the law; the units row decides how interfaces with foreign vendors are written.
- **Project manager, planner**: a regime change is a schedule and cost item (approvals, third-party inspection, translations) — plan it, do not discover it.

Cross-references: `multi-country.md` (the nine axes), `country-cards.md` (per-country detail where a card exists), `_template-country.md` (to add a country — its first line is the regime).
