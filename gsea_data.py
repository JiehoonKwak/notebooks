import json



data  = {
  "neural_progenitor_cell_maintenance": {
    "Neurogenesis": "GO:0022008",
    "Neuron fate commitment": "GO:0048663",
    "Neuron development": "GO:0048666"
  },
  "glioma_and_tumor_development": {
    "Apoptotic process involved in morphogenesis": "GO:0010623",
    "Positive regulation of cell migration": "GO:0030335",
    "Negative regulation of cell proliferation": "GO:0008285"
  },
  "stem_cell_maintenance_and_differentiation": {
    "Stem cell maintenance": "GO:0019827",
    "Stem cell differentiation": "GO:0048863",
    "Cell fate commitment": "GO:0045165"
  },
  "cell_cycle_and_division": {
    "Cell cycle": "GO:0007049",
    "Cell division": "GO:0051301",
    "Chromosome segregation": "GO:0007059"
  },
  "cell_cycle_regulation": {
    "Cell cycle": "GO:0007049",
    "Regulation of cell cycle": "GO:0051726",
    "Mitotic cell cycle": "GO:0000278"
  },
  "dna_repair_and_replication": {
    "DNA repair": "GO:0006281",
    "DNA replication": "GO:0006260",
    "Telomere maintenance": "GO:0000723"
  },
  "signal_transduction_pathways": {
    "Signal transduction": "GO:0007165",
    "Neurotrophin TRK receptor signaling pathway": "GO:0048011",
    "Smoothened signaling pathway": "GO:0007224",
    "Epidermal growth factor receptor signaling pathway": "GO:0007173",
    "Ephrin receptor signaling pathway": "GO:0048013"
  },
  "apoptosis_and_survival": {
    "Apoptotic process": "GO:0006915",
    "Regulation of apoptotic process": "GO:0042981",
    "Intrinsic apoptotic signaling pathway": "GO:0008630"
  },
  "metabolic_pathways": {
    "Glycolytic process": "GO:0006096",
    "Fatty acid metabolic process": "GO:0006631",
    "Aerobic respiration": "GO:0009060"
  },
  "microenvironment_interaction": {
    "Skeletal system development": "GO:0001501",
    "Regulation of locomotion": "GO:0040012",
    "Cell-cell signaling": "GO:0007267"
  },
  "chromosome_7_gain": {
    "Cell cycle regulation": "GO:0007049",
    "DNA repair": "GO:0006281",
    "EGFR signaling pathway": "GO:0007173"
  },
  "chromosome_19_loss": {
    "Apoptotic process": "GO:0006915",
    "Cell differentiation": "GO:0030154",
    "Neuron projection development": "GO:0031175"
  }
}

with open("go_terms.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
