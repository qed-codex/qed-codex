---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRowPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRowPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRowPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical row-data preparation for the global basis assembler

The persistent inputs are type index 32, packing metadata 33, vertex index
34, universal types 37, color count 38, and the current type's local-search
batch 40.  Canonical scalar frames on 13--15 are framed
by every call.  A covered row is populated by actual metadata lookup,
head-color decoding, Side filtering/rank lookup, and local-table decoding.

This module is the concrete composition layer.  The full assembler must
establish the input-table equalities from their physical producers.


### `command`

 The branch is selected by the Boolean produced by the physical metadata
parser. An uncovered row needs only its actual leftover rank. 

### `headColor_eval`

 The head color is read from the stored one-hot type, rather than
supplied by a semantic row map. 

### `side_eval`

 The Side pass is a genuine physical filter. This local statement keeps
its input-state condition explicit for the covered-row composition. 

### `rank_eval`

 The actual first-match index of the row type in the freshly generated
Side list becomes its local coordinate. 

### `localTable_eval`

 Selecting a real local-search record exposes its stored matrix and
dimensions. Only four result ports change. 
