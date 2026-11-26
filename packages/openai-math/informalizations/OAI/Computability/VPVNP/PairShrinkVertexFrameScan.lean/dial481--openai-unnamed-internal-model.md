---
{
  "module": "OAI/Computability/VPVNP/PairShrinkVertexFrameScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVertexFrameScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVertexFrameScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Retaining the vertex geometry through the resident map scan

The geometry array and cached verifier words lie after the histogram and
before the hidden scratch. The pointer at the live length lies below the
histogram. The exterior identity of each map therefore preserves the whole
vertex frame through the deterministic list of actions.


### `VertexFrameData.after_map`

 The exterior clause of a shrinking map preserves every word in the
tree decoder's vertex frame, including all cached verifier operands. 

### `VertexFrameData.scan`

 Word-by-word transfer through the exact pure map scan. This induction
uses the actual scratch returned by the preceding occurrence. 
