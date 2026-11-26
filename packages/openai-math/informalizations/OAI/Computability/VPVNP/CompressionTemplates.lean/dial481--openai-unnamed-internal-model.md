---
{
  "module": "OAI/Computability/VPVNP/CompressionTemplates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionTemplates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionTemplates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed equations for one compressor block

The shrinking identities all use the same six-party template, independently
of the base degree. The degree refresh uses one template on the chosen
port graph. Tagging their parameter and equation indices gives a single
finite system over the integers, fixed before the input network or the
number of iterations.


### `portExponent`

 Port order exponent at the last shrinking step. 

### `portComparison`

 Comparison constant for the internal port demands, before the unit slack. 

### `portSupply`

 The expander as the connected supply motif for the fixed refresh graph. 

### `Templates`

 The two families of base maps and all their widths. 

### `Templates.shrink`

 Fixed six-party block used for the local wire identity at each shrinking substep. 

### `Templates.refresh`

 Fixed block implementing the refresh identity on the schedule's chosen port graph. 

### `exists_templates`

 Both templates exist over the field in which the spectral bound was established. 

### `Entry`

 Parameter indices of the joint equation system, tagged by the shrinking or refresh block
they belong to. 

### `EquationIndex`

 Output-equation indices of the joint system, tagged by which of the two fixed blocks
supplies the equation. 

### `equation`

 Distinct variable names for the two sets of integral equations. 

### `IsSolution`

 Simultaneous vanishing of the fixed template equations in a coefficient ring. 
