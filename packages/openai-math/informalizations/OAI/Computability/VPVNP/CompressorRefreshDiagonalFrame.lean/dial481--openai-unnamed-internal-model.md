---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshDiagonalFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshDiagonalFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshDiagonalFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native setup of the two diagonal comparisons at a refresh site

The six computed registers contain both old half-wire intervals and both starts in the
parent's external bundles. All offsets come from the constructed segment tables. The
expression program hands control directly to the linked comparison code.


### `fields`

 Computes the old outgoing and incoming interval endpoints and the corresponding segment
starts in the new external half-wires. 

### `register`

 The output-bank indices in the existing diagonal comparison program. 

### `values`

 Evaluating the fixed setup formulas uses the actual old and new slot layouts.
Incoming half-wires keep their own lengths and their source-bundle ordering. 

### `setup_trace`

 The native setup's exit satisfies the six-register ABI consumed by
`RefreshDiagonal.compare_arguments`. Its only external accesses are reads. 

### `setup`

 Register and continuation postconditions for the physical operand setup. 
