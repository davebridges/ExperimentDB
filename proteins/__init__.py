"""The proteins app contains details regarding proteins.

The proteins referenced by this application may be targets of an experiment or reagent.  This app also contains more detailed information about specific proteins, normally as accessed from public databases using either external databases or through Biopython tools.

The models used in this app are:
* Protein
* ProteinFamily
* ProteinDetail
* Species

These models are accessed by the following views:
* protein-list
* protein-detail
* protein-new
* protein-edit
* protein-delete
* protein-family-list
* protein-family-detail
* protein-family-new
* protein-detail-new
* protein-detail-edit
* protein-detail-delete
* protein-isoform-detail
* protein-name-slug
"""
