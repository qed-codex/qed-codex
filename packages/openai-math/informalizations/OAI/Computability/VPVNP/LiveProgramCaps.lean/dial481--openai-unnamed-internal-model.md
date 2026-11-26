---
{
  "module": "OAI/Computability/VPVNP/LiveProgramCaps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCaps.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCaps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Combining the auxiliary pair charge with the outer live program

The small-o estimate for the compressed pair can be used with constant
one quarter. Dispatch adds at most two probes per pair call. The rest of
the group costs at most one physical processor array. These two estimates
suffice for the total transcript cap, while the two-probe and finite
instruction margins account for every individual dispatch.


### `withinCaps_pair_group`

 The physically charged prefix, linked pair, and suffix all satisfy the
same `withinCaps` condition used by the parsimonious transcript theorem. 

### `linked_pair_clock`

 For the fixed outer table, a pair trace with a finite additive clock
margin executes within the live `n^10000` private-work budget. 
