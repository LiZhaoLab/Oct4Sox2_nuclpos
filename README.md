# Oct4Sox2_nuclpos

This repository supports the manuscript "Nonreciprocal and Conditional Cooperativity Directs the Pioneer Activity of Pluripotency Transcription Factors", by Sai Li<sup>1</sup>, Eric Bo Zheng<sup>2</sup>, Li Zhao<sup>2</sup>, and Shixin Liu<sup>1</sup>.

1) Laboratory of Nanoscale Biophysics and Biochemistry, The Rockefeller University, New York, NY 10065, USA
2) Laboratory of Evolutionary Genetics and Genomics, The Rockefeller University, New York, NY 10065, USA

# Notebooks
[Mouse Genomic Data Preparation](ipynb/bioc-mouse-preparation-public.ipynb): Data preparation for mouse.

[Mouse Motif Matching](ipynb/py3_motif-matching-mouse-public.ipynb): FIMO coordinate conversion for mouse.

[**Mouse Genomic Data Analysis**](ipynb/bioc-mouse-genomic-analysis_public.ipynb): Data analysis for mouse, resulting in **Figures 7B-F**.

[Human Genomic Data Preparation](ipynb/bioc-human-preparation-public.ipynb): Data preparation for human.

[Human Motif Matching](ipynb/py3_motif-matching-human-public.ipynb): FIMO coordinate conversion for human.

[**Human Genomic Data Analysis**](ipynb/bioc-human-analysis-public.ipynb): Data analysis for human, resulting in **Supplemental Figures S7A-E**.

[Figure 7A Schematic](ipynb/PanelA_public.ipynb): Generates the curves used in the schematic in Figure 7A.

# Scripts
[`danpos_xls_process.py`](scripts/danpos_xls_process.py) - converts the raw XLS output from DANPOS dpos to a bedgraph. Also filters peaks to only those with a summit height 1.5X the genomic mean.

[`wig2rle.R`](scripts/wig2rle.R) - a slight misnomer; converts a **BigWig** to a Bioconductor GRanges RleList, saving it as a RDS.
