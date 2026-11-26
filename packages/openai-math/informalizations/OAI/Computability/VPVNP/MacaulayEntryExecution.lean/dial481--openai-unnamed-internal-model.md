---
{
  "module": "OAI/Computability/VPVNP/MacaulayEntryExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayEntryExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayEntryExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Execution of the shifted and powered coefficient arms

The two ordinal scans run on the source and column words issued by the row
decoder. The divisibility and equality flags below come from the actual scans
and determine the subsequent bit-stack computation.


### `equation_execution`

 Complete shifted-monomial matrix read. The chosen leaf receives exactly
the coordinatewise difference and is skipped when the multiplier fails to
divide the column. 

### `powered_execution`

 Complete powered-monomial read. The successful equality flag emits the
stored unit scalar, and an unequal exponent emits zero. This code also
handles marked or Frobenius targets via the scan's `scale` and `mark` words. 
