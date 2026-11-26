---
{
  "module": "OAI/Computability/VPVNP/EvaluatorIndexRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorIndexRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorIndexRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The basis index registers of the evaluator

Each step preserves the advised dimension and the old ordinal while it
generates the new ordinal in the little-endian format used by the query
routines. Once the entry has been used, committing the new ordinal clears
the scratch stacks and prepares the registers for another step.


### `Port`

 Stacks for the basis dimension, current ordinal, bounded guess and the scratch used to
commit the next ordinal. 

### `bank`

 The two index words available during an entry query. At a step boundary
the next index is empty. 

### `select`

 Guess once below the dimension and restore the chosen word to the
same bit order as the old index. 

### `select_safe`

 The selection code preserves a polynomial storage bound on both branches
of every choice. All returning branches supply an in-range ordinal. 

### `commit`

 Replace the old ordinal by the new one after the matrix entry query. 
