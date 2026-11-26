---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/IncidencePlanSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/IncidencePlanSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/IncidencePlanSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordered incidence plans from finite scope lists

The numeric producer records incident factors in their input order. The
typed refinement uses the rank in that same list as the local slot.


### `incidenceFrom`

 Record incident factor positions while advancing through the scope list. 

### `vertexPlan`

 Head seed, incident factor seeds, then private unused-slot seeds. 

### `producedPlan`

 The stack producer emits this reverse order. 

### `pattern`

 The finite typed pattern obtained by testing membership in the actual
scope lists. Repeated entries and their inner order do not change incidence. 

### `incidentAt`

 Lookup by occurrence rank in the list emitted by the numeric producer. 

### `incidentEquiv`

 Incident factors and their explicitly computed occurrence ranks. 

### `slots`

 The actual rank-based slot assignment. It is constructed from scope lists,
not supplied as an arbitrary runtime object. 

### `vertexPlan_eq_readPlan`

 The computed numeric plan is exactly the typed read plan for the explicit
occurrence-rank slot assignment. No arbitrary SlotMap is an input. 

### `gather_vertexPlan`

 Gathering the actual numeric plan recovers the same local type encoding
used by the collision selector. 
