---
{
  "module": "OAI/Computability/VPVNP/CompressionSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing one fixed compression block

Section 7.4 chooses the number of shrinking steps before their output
degrees. The refresh multiplier depends only on the common expander bound,
the expander degree and the fixed initial degree. Each subsequent power of
two can therefore be chosen large enough to represent the four supply masses,
and the last one can be an order of the common expander family.


### `shrinkComparison`

 An admissible strict version of the six-party squared-distance bound. 

### `shrinkLoss`

 The relative mass lost in replacing real weights by integral slots. 

### `shrinkMultiplier`

 Leading energy factor of a shrinking step with the chosen constants. 

### `packingFactor`

 The exact position-count ratio in the dyadic packing at degree `2^a`. 

### `AllowsShrink`

 A transition between exponents meets the mass and slot capacity bounds
of the actual regularized shrinking step. 

### `refreshMultiplier`

 The leading refresh factor (7.3), independent of the port count. 

### `BlockSchedule`

 A fixed block of shrinking degrees followed by an expander refresh. 

### `BlockSchedule.expanderExponent`

 Binary logarithm of the common expander degree used in the final refresh. 

### `BlockSchedule.poincare`

 Uniform Poincaré bound required of the port graph at the end of the block. 

### `BlockSchedule.steps`

 Number of shrinking substeps before the degree refresh. 

### `BlockSchedule.degreeExponent`

 Base-two degree exponent at each boundary of the shrinking sequence, including its
  initial and final boundaries. 

### `BlockSchedule.graph`

 Regular port graph on the final shrinking degree's ports, with degree fixed by
  `expanderExponent`. 

### `exists_blockSchedule`

 All the constants and the graph in the schedule are selected before
the network, its lane count, and its widths. 

### `baseDegree`

 Initial and final restored degree. 

### `laneBits`

 Number of lane bits consumed by the whole block, including the port index. 

### `positionFactor`

 Number of old positions per final position; refresh keeps all the positions. 

### `exponentAt`

 The scheduled exponent at an index, with later indices held at the
last exponent. This permits sums over ordinary half-open index ranges. 

### `remainingBits`

 Lane coordinates required by the suffix starting at shrink `i`.
Extra unused coordinates can be appended to every suffix. 
