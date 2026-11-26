---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowAssemblyPrepared.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowAssemblyPrepared.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowAssemblyPrepared.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete, ordered cache tables for the universal-row producer. 

### `computedTables`

 The value array is defined from the matrix entries actually computed by
the vector program. All field caches follow the same increasing Fin Q order. 

### `PreparedInput`

 Physical input invariants for one row. The matrix coefficients are the
normalized scalar-search output. The three field caches are raw arrays in
the established node order, not a supplied interpolation expression. 

### `command_eval_prepared`

 The complete fixed command computes the row from the physical masters,
generates its mismatch list, and returns all scratch stacks to empty. 

### `caller_eval_prepared`

 The 25-register dispatcher receives the exact source word and retains
its nine high metadata registers. Its type metadata and caches are framed. 
