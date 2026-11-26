---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticConstant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticConstant.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticConstant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning the field constants zero and one on bit stacks

The advised defining polynomial occupies exactly as many limbs as a scalar.
Its packed representation supplies the width template for a literal scan.
The scan restores the template and writes the selected constant in the
extension field's packed power-basis format.


### `machine`

 Scan a packed width template to write the extension-field literal zero or one according to
`b`. 

### `literal`

 Chosen coefficient vector of the returned field literal. 

### `machine_runs`

 Initialize or overwrite a scalar result on `.out`. The advised
polynomial on `.left` is preserved and both temporary stacks return empty. 
