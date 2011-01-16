"""The reagents application stores information about specific tools used in research.

The reagents app stores information about all tools used in research, most of which are defined by a particular Experiment object.  These include Primer, Cell (cell lines), Antibody, Strain, Chemical and Construct objects.  These models are abstract base classes of a superclass ReagentInfo which defines most of the common relevant information.

The models are ReagentInfo, which is an abstract superclass of:
* Primer
* Cell
* Antibody
* Strain
* Chemical
* Construct

There are many views in this app, generally consisting of the names model-list, model-detail, model-new, model-edit and model-delete, with the model name in lowercase.
"""
