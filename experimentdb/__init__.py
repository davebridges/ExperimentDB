"""The experimentDB is a web-based application for the storage, organization and communication of experimental data with a focus on molecular biology and biochemical data. This application also stores data regarding reagents, including antibodies, constructs and other biomolecules as well as tracks the distribution of reagents. There is also some preliminary interfaces to other web resources.

This project contains several sub-applications as described below:

Projects
--------
The intent of this app is to co-ordinate specific projects. Projects are intended to be large, grant-sized larger projects in the laboratory. Subprojects are intended to be smaller, potentially paper sized groups of experiments.  An experiment can be part of one, none or several projects or subprojects.

Data
----
This package defines experiments and the related data associated with them. The Experiment model is the focus of this entire project. It contains details about protocols, notes, reagents and project details. Results are associated with Experiment objects allowing for an Experiment to contain several results.

Cloning
-------
The cloning app defines the parameters for the synthesis and maintenance of constructs generated as part of an experiment.  Constructs can be generated via either cloning or mutagenesis and will result in a Cloning or Mutagenesis object respectively.

Proteins
--------
The proteins referenced by this application may be targets of an experiment or reagent.  This app also contains more detailed information about specific proteins, normally as accessed from public databases using either external databases or through Biopython tools.

Reagents
--------
The reagents app stores information about all tools used in research, most of which are defined by a particular Experiment object.  These include Primer, Cell (cell lines), Antibody, Strain, Chemical and Construct objects.  These models are abstract base classes of a superclass ReagentInfo which defines most of the common relevant information.

External
--------
The idea is to attribute particular models with references regarding external contacts or vendors or to link in specific references important to the experiments or projects.

Datasets
--------
The datasets app contains data and views for some external databases.  This may include external databases accessed directly or with a mirrored internal database.  This module is fairly research-interest specific and will likely be removed eventually.

"""
