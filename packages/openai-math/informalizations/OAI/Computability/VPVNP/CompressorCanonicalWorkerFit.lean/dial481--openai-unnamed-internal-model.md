---
{
  "module": "OAI/Computability/VPVNP/CompressorCanonicalWorkerFit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCanonicalWorkerFit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCanonicalWorkerFit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform word bounds for the canonical dense term-worker input

Demand rows begin at zero and the strided term rows begin at the end of
the demand array. Both shrink and refresh grids have template-fixed row
widths. Their storage, including the two header words and the independent
stride operands, is polynomially bounded in the original cursor length.


### `eventually_fit`

 Every origin of every selected execution satisfying the current position
and maximum-width bounds has the exact dense addresses, private operand
width and input word range required by the canonical worker. 
