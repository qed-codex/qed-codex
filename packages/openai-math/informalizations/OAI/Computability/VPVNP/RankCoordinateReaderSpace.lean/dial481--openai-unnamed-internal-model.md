---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateReaderSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReaderSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReaderSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preserving the space bound of the evaluator's scalar reader

The native coordinate routine owns the live label, current and next ordinal,
result and private advice ports. Every other evaluator stack is unchanged and
has length bounded by the index word width, scalar degree or scalar word length.


### `callerPeak`

 Maximum height among the caller's stacks outside the installed routine. 

### `readsEntryWithin`

 The native core's cap and the caller's untouched stacks determine the
physical peak, independently of the time spent computing the coordinate. 

### `readsEntryWithin_of_suffix`

 Packed Cramer execution supplies the full time-and-space matrix callback
on the concrete basis of the reduced algebra. 
