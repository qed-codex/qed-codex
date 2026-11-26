---
{
  "module": "OAI/Computability/VPVNP/RefreshProcedureRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshProcedureRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshProcedureRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform record bounds for the scheduled expander refresh

The actual refresh in a compression block has one substep. Its local resource
constant depends only on the chosen degrees, expander and fixed motif template.
It can therefore be fixed before specializing the parameter values.


### `refreshRecordConstant`

 Uniform count and growth constant for the refresh in this schedule. 

### `refreshProcedureRecords`

 All branches of the scheduled refresh retain the actual port records and satisfy
one bound, independent of the specialization ring, lane count and input widths. 
