---
{
  "module": "OAI/Computability/VPVNP/RankQueryExecutionSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryExecutionSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryExecutionSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Peak storage through a full rank scan

The Schur engine releases its traversal stack at every coefficient. The
outer scan reuses one scalar and a fixed register bank. Its space cap
depends on the cap of a single root query and on the short cursor-update
clock, independently of the number or total time of the root queries.


### `RootBoundedRead`

 A root may take `B` instructions while its intermediate stacks fit `C` bits each. 

### `outerRankSpace`

 Per-stack cap for the entire rank loop, taking the maximum of the root-query peak `C` and
the space for the returned scalar and cursor check above auxiliary height `A`. 

### `rankMachine_boundedRun`

 Every intermediate stack through all coefficient requests fits the same
cap. In particular no part of the exponentially long rank loop is stored
as a list of instructions or scalar outputs. 
