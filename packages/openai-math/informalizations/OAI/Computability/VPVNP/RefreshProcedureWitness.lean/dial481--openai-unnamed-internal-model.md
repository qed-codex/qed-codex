---
{
  "module": "OAI/Computability/VPVNP/RefreshProcedureWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshProcedureWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshProcedureWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Refresh witnesses in the common template alphabet

Every scheduled refresh uses the second group of parameters in the fixed
equations. Its kernel witnesses record the label multiplicities at each port
for every choice of branch and half-wire arguments.


### `refreshProcedureWitnesses`

 Finite syntactic witnesses for each execution of the scheduled refresh,
in the same alphabet as the shrinking passes. 
