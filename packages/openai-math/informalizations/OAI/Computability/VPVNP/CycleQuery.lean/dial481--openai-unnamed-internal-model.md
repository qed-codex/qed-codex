---
{
  "module": "OAI/Computability/VPVNP/CycleQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact query budget for the Hamiltonian matrix check

Starting from the distinguished root, the finite-control program scans one row
per vertex in the putative cycle. A successful traversal uses exactly one read
per column of each of its `m` rows.


### `passesFrom`

 The row and first-return checks that are still pending at the start of row `t`. 

### `cycleQuery_eval_iff`

 The matrix query program decides the directed spanning-cycle predicate with
a budget of exactly `m * m` payload queries. 
