---
{
  "module": "OAI/Computability/VPVNP/CursorBranchBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBranchBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBranchBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Budgets of a selected compressed cursor network

Section 12 bounds the shared bits, local records and total number of
history occurrences on each branch. Here the input carries the real
sorting and successor fields of the virtual RAM. The threshold precedes
the lane labeling, coefficient assignment and compressor branch.


### `pairInput`

 Place the virtual RAM at the cursor-zero positions and reserve the
successor and sorting message fields on both physical routing arcs. 

### `PairExponents`

 The fixed growth constant determines rational parameters as in Section 9.1. 

### `PairExponents.θ`

 Positive rational exponent governing the number of compression blocks, chosen to control
  growth under iteration. 

### `PairExponents.δ`

 Positive rational slack exponent chosen smaller than one tenth of the compression
  exponent `θ`. 

### `pairExponents`

 Choose the two exponents for the compressed pair using only the fixed block's growth
constant. 

### `totalOccurrences`

 Count local map, field and child occurrences over all final positions
using the actual placement fibers on a selected branch. 

### `eventually_pairBranchBounds`

 Section 12 on the actual cursor graph and selected terms. The last
strict inequality bounds the sum over all final sites if each of their
recorded map occurrences contributes its allowed degree. 
