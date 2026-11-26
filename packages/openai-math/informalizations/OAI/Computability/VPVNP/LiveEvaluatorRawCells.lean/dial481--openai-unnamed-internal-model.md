---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRawCells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRawCells.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRawCells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Raw cell words on successful live evaluator calls

On a successful group the source check examines every word, even the
overwritten head cell. Destination words are either zero (for a halt) or
equal to a legal written symbol. The old-cell permutation covers every
destination, so an accepting computation forces both configuration arrays
to have canonical symbol fields.


### `cellWord`

 Read the machine word for a given tape cell from the physical configuration array. 

### `configAt_of_valid`

 The actual state and symbol words determine a canonical cut configuration
if the state and symbol ranges and halt padding pass. 

### `rawCells_force_images`

 An occupied scratch instruction and successful scan force all old and
new tape fields to encode canonical evaluator symbols. 
