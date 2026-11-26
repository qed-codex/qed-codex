---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorScalars.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorScalars.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorScalars.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the six level scalars for the online compressor

A header describes the current graph and the fixed pass that will consume it.
The initial burst reads the generated cursor parameter frame. Each subsequent
burst reads the preceding level header. Its vertex count grows by the tag radix
for a shrink and by the old degree for a refresh. Its lane count is the preceding
residual radix. The destination address is the worker's first public operand.


### `Pass`

 The input and output indices are degree exponents. A terminal level spends
no lanes and records its current degree as the output degree. 

### `Pass.spent`

 Number of binary lane coordinates consumed by this pass, with zero consumption at a
terminal level. 

### `Pass.baseFactor`

 Multiplier for the input base-vertex count when publishing the successor header. Shrinking
uses the tag radix and refresh uses the old degree. 

### `Pass.expanderDegree`

 Expander degree published for a refresh, with zero in the corresponding header field for
other passes. 

### `values`

 Vertex count, degree, lane radix, residual radix, output degree, expander degree. 

### `Fits`

 All six scalar values for this pass and input size fit in words of width `w`. 

### `Present`

 Each scalar can be recovered by its ordinary header load without truncation. 

### `initialRow`

 The source state points at the eight-word frame installed by the cursor
parameter program. Frame cells 3, 4 and 5 are the cursor count and the two radices. 

### `advanceRow`

 Read old header cells 0, 1, 3 and 4 as needed. In particular the old
output degree is the new input degree. 

### `ofOrigin`

 Link the natural scalar count to the mathematical state selected by a real
kernel. The growth of the base is independent of all term choices. 

### `fieldIndex`

 Scalar fields occupy the first six words of the persistent level header. 

### `Publishes`

 Complete normal-entry specification, including the six natural values,
the frame for the next pass, and preservation of all other addresses. 

### `fits_state`

 The fixed pass's scalars fit whenever the current graph and the two
degree bounds fit. No condition on the remaining lane length is needed. 

### `fits_selected`

 Every selected input level fits under the schedule's common maximum degree. 

### `initialize_from_parameters`

 The cursor generator supplies the scalar publisher directly from its real
normal-entry report. Both calls use the external memory produced by their
predecessor. 

### `advance_selected`

 The next published vertex count is the base cardinality of the actual
output state, even when its topology and widths depend on the selected term. 
