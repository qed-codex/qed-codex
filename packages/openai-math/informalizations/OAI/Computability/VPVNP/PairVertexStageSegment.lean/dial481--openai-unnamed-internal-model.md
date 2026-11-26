---
{
  "module": "OAI/Computability/VPVNP/PairVertexStageSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStageSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStageSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking the stage selector to a heterogeneous family of shrink handlers

The selector and each handler have separate code ranges. The locator and every
handler share the same fourteen-word header bank. The selector's scratch words
and the variable-length handler tails occupy disjoint ranges.


### `familyCount`

 Size of the scheduled dispatch family, including the selector table and every stage body's
instructions. 

### `selectorPC`

 Place stage-selection instructions before the concatenated bodies of the dispatch family. 

### `bodyPC`

 Place an instruction of a particular scheduled body using its dependent ordinal in the
concatenated family. 

### `family`

 Any explicit bank placement can host the family. Every selected handler
returns to the enclosing role continuation. 

### `family_link`

 Split the concrete image into its selector table and its individually
relocated branch bodies, with the exact native jump destinations. 

### `bankCount`

 The shared locator prefix is followed by four selector scratch words
and by the private tails in increasing order of shrink stage. 

### `bankIndex`

 Number the shared locator and selector scratch registers followed by each body's private
tail bank. 

### `locatorBank`

 Embed the common fourteen-register locator bank in the dispatch family's register layout. 

### `scratchBank`

 Embed the selector's four scratch registers beside the common locator bank. 

### `tailBank`

 Embed only the indicated stage's tail registers in the dependent family of private tail
banks. 

### `bodyBank`

 A handler sees the locator in its first fourteen registers and sees
only its own tail in the remaining registers. 

### `locatedFamily`

 The full shrink role starts by recovering its level and then dispatches
its zero-based producing ordinal to the selected handler. 

### `locatedCount`

 Total instruction count of a family preceded by the level locator. 

### `locatorPC`

 Program counters of the locator at the beginning of the combined locator-and-dispatch
image. 

### `familyPC`

 Program counters of the dispatch family after the locator's 35 instructions. 

### `locatedFamily_link`

 Both the 35 locator rows and every selector and stage-body row occur at
their indicated PCs in the single hosted role. 
