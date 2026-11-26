---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorEdgeValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEdgeValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEdgeValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successor values returned by the physical edge check

For a present edge the validity flag recognizes the entire canonical encoding.
The running bit, cumulative cost, state and record on a valid return agree with
the typed message. At a missing edge the only valid input is the zero clamp.


### `present_verdict_iff`

 The returning validity bit on a present edge agrees with successful decoding. 

### `present_values`

 On a successful present-edge check, the saved cost includes the possible
endpoint value `cap`. A halt supplies the zero state word. 

### `clamp_verdict_iff`

 On a missing edge the verdict bit tests every incident bit against zero. 

### `clamped_values`

 The only valid missing field supplies eight zero words, a zero record
of exactly five word widths, and the nonrunning flag before site normalization. 
