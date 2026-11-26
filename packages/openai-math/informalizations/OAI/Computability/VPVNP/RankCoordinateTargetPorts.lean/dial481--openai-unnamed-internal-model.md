---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateTargetPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateTargetPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateTargetPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Dynamic inputs to the powered target row

The enclosing coordinate query stages the source monomial ordinal, the
marked variable, and the power scale. The other monomial address is the
column requested by the scalar reader. The auxiliary bank also retains
encoded constants zero and one.


### `Extra`

 Additional powered-reader ports for the encoded zero and one scalars and a temporary stack. 

### `Work`

 Private workspace combining the monomial pair scan, two scalar literals and a temporary
stack. 

### `Port`

 Matrix entry interface whose auxiliary stacks run the powered target scan. 

### `sourcePort`

 Workspace address holding the source monomial's ordinal in the pair scan. 

### `markPort`

 Workspace address holding the one-based variable mark, with zero denoting an unmarked
target. 

### `scalePort`

 Workspace address holding the exponent scale used by the powered monomial test. 

### `flagPort`

 Reader address of the equality flag produced by the powered monomial scan. 

### `storage`

 The full flag word belongs to the powered scan until the scalar copy
has completed. The caller's column is the only aliased pair-scan port. 

### `bank`

 Initial powered-reader bank with the supplied scalar literals and an empty result flag. 

### `setDynamic`

 Updates the source ordinal, power scale and variable mark while preserving the column
ordinal and degree bounds. 

### `slot`

 The staging slots, in source ordinal, marked variable, and scale order. 

### `words`

 The three fixed-width staging words, ordered as source ordinal, variable mark and exponent
scale. 

### `blankDynamic`

 Powered-reader template with the three dynamic argument stacks emptied for staging. 
