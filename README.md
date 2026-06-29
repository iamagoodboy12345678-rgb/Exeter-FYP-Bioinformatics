# Exeter-FYP-Bioinformatics
Automated virulence gene scanner for Candida albicans mutant library screen.
# Exeter Final Year Project - Bioinformatics Scanner

An automated computational workflow designed to parse genomic sequence strings and screen for established virulence factors in human fungal pathogens. 

## 🧬 Biological Context
This tool maps directly to the screening of the **Candida albicans 'Noble Library'** (~670 single-gene deletion mutants) within the *Galleria mellonella* (wax moth larvae) infection model. 

## 🛠️ Features Completed
- **Targeted Screening:** Automates string-matching to isolate specific disrupted mutant strains.
- **Feature Extraction:** Dynamically extracts the exact position indexes and sequence size lengths of target genes.
- **Duplication Tracking:** Includes a built-in counter mechanism to calculate virulence factor repetition frequencies (`.count()` functionality).

## 🚀 Target Genes Tracked (Table 2 Reference)
- `DUN1` (DNA damage response pathway)
- `CRZ1` (Transcription factor regulation)
- `MID1` (Calcium homeostasis mediator)
- `CYB1` & `HAK1` (Virulence-associated targets)
