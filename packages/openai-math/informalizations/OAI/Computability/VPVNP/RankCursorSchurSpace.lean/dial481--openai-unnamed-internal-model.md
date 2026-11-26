---
{
  "module": "OAI/Computability/VPVNP/RankCursorSchurSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchurSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchurSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Rank-cursor queries with separate time and space for scalar entries

A streamed matrix-entry computation can use exponential time and polynomial
space. The caller retains the descriptor's own stack cap, while its time
bound enters the running time of the Schur recursion.


### `readClock`

 Step bound for one Schur coefficient query, charging the entry descriptor’s time allowance
at each recursive engine step. 

### `readSpace`

 Stack-height bound for one Schur coefficient query using the entry descriptor’s separate
peak-space allowance S. 

### `rootQuery_separate`

 Use the descriptor time only in the total clock. Its certified stack cap,
together with the live register and return stack caps, suffices throughout. 
