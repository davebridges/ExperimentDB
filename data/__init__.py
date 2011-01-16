"""This package describes experimental data.

This package defines experiments and the related data associated with them.  The Experiment model is the focus of this entire project.  It contains details about protocols, notes, reagents and project details.  Results are associated with Experiment objects allowing for an Experiment to contain several results.

There are three models in this package:
* Experiment
* Result
* Protocol
* Sequencing

These models are accessed via several views:
* protocol-list
* protocol-detail
* protocol-new
* protocol-edit
* protocol-delete
* experiment-new
* result-new
* experiment-edit
* experiment-detail
* experiment-list
"""
