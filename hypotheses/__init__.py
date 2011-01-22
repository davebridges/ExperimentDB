"""The hypothesis app contains more detail about specific testable hypotheses.

The purpose of this app is to organize results and observations or summaries of experimental hypotheses in a systematic way.  A hypothesis is something that is observed about a biological process or biological entity.  It is supported by evidence, which could be an external publication or an experiment contained in this database.  The goal is to be able to say "X causes Y in this context, with the following evidence" 
	
The models in this app are:
* Hypothesis (Manipulation(m2m) - Affects - Process/Entity in Context(m2m) + Evidence(m2m))
* Manipulation (Manipulation or Treatment, could be several things, could be with a chemical.  May refer to a protein.  This could be a knockout of a protein/knockout with a siRNA, overexpression with a construct, treatment with a chemical)
* Affects (stimulates, has no effect, inhibits as instances (initial data fixture); needs ontologies specified and description)
* Process (can be a biological entity or a process, could include sameas links to GO)
* Entity (can be a protein, phosphorylation site, could be the same as a readout of a biological process, must be linked to a protein)
* Context (under what conditions, includes cell line or model system)
* Evidence (paper or experiment, can disagree or agree, can be public or not, include createdate, edit date and user)

The views in this app are in hypothesis.py, manipulation.py, process.py, entity.py, context.py and evidence.py.  There are no views for affects, but these can be set at the admin site.

In hypothesis.py:
* hypothesis-new
* hypothesis-detail
* hypothesis-edit
* hypothesis-list
* hypothesis-delete

In manipulation.py:
* manipulation-new
* manipulation-detail
* manipulation-edit
* manipulation-list
* manipulation-delete

In process.py:
* process-new
* process-detail
* process-edit
* process-list
* process-delete

In entity.py:
* entity-new
* entity-detail
* entity-edit
* entity-list
* entity-delete

In context.py:
* context-new
* context-detail
* context-edit
* context-list
* context-delete

In evidence.py:
* evidence-new
* evidence-detail
* evidence-edit
* evidence-list
* evidence-delete

"""
