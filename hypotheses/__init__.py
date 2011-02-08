"""The hypotheses app contains more detail about specific testable hypotheses.

The purpose of this app is to organize results and observations or summaries of experimental hypotheses in a systematic way.  A hypothesis is something that is observed about a biological process or biological entity.  It is supported by evidence, which could be an external publication or an experiment contained in this database.  The goal is to be able to say "X causes Y in this context, with the following evidence" 
	
The models in this app are:
* Hypothesis
* Manipulation
* Affects
* Process
* Entity
* Context
* Evidence
* CitationType

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
