---
{
  "module": "OAI/Computability/VPVNP/EvaluatorScheduleCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The residue of the scheduler's actual index choices

The continuation of the nested digit loops stores the current basis ordinal
and the accumulated scalar. At termination its ordinary integer multiplicity
is the constant-coordinate residue at the unit ordinal and zero elsewhere.
Expanding the continuation over the chronological actions gives exactly the
matrix-index paths of the finite algebra.


### `finishWeight`

 The endpoint test used by the terminal field reader. 

### `indexTransition`

 A transition multiplies the old accumulator by row `j`, column `s.1`
of the current linear map. The index `j` is the next binary guess. 

### `nextIndex`

 The ordinal of a label is read from the scheduler's current unary counter.
All live ordinal values are in range. 

### `schedulerEffect_eq_card`

 The ordinary count of the nested digit loops is the number of accepting
index paths with their final residue multiplicities. 

### `schedulerEffect_mod`

 Equation (8.2) for the physical scheduler's ordinary path-count effect. 
