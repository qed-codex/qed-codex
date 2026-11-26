---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenSegmentRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSegmentRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSegmentRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Header and field execution in the hosted hidden segment 

### `segment_prepare_raw`

 The live header sets up the hidden loop without changing any private
memory cell or register outside the installed header bank. 

### `segment_run`

 A full hosted scan on a valid row, returning to the caller's exact PC.
Registers outside its private bank remain available to the next segment. 
