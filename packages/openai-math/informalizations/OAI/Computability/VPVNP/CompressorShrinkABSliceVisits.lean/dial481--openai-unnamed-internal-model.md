---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceVisits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceVisits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceVisits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native whole-bundle segments of the AB calendar 

### `Stage.pass`

 The local worker template executed at this AB stage before compilation into a whole-bundle
scan. 

### `Stage.localIdx`

 The fixed endpoint or field-pair index that this stage processes at every bundle. 

### `Stage.fuel`

 Local call fuel for an AB stage, with 8 steps for clearing, 38 for a field pair and 36 for
references. 

### `Stage.affineParams`

 Select the clear, intersection or reference operand expressions for the stage's local
worker. 

### `Stage.data`

 The local worker's concrete operand words for a single bundle, using its actual input
columns and bank address. 

### `Source`

 Executing the stage's flat worker from zero with one empty choice stream per bundle
produces the specified source reports. 

### `one`

 Lifting one local instruction-table execution to the calendar's global
bundle cursor preserves its entire memory effect. 

### `banks_disjoint`

 Distinct bundle ordinals have disjoint output banks, including when the
fixed shape has zero occupied fields. 

### `phase_run`

 Every whole-level visit threads actual native reports through the banks
and preserves the shared inputs. 
