---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFieldNodes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldNodes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldNodes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable nonzero nodes for the selected quartic field

The execution data are four coefficients. The list order is the explicit
QuarticSearch vector order, with exactly the zero vector filtered out.
Abstract field values occur only in the mathematical interpretation.


### `allData`

 Enumerate all coefficient vectors in explicit recursive list order. 

### `nodeData`

 The actual executable node list, with the zero coefficient vector removed. 

### `nodeData_length`

 Every nonzero vector occurs once, so there are exactly p^4 - 1 nodes. 

### `coefficientNodeEquiv`

 Index the actual list. Both directions are executable: the inverse
searches this same list with idxOf. No arbitrary finite enumeration is used. 

### `nodeCoefficients`

 Executable coefficient data of the node at a given list index. 

### `filterWithCount`

 Filtering with an actual counter for the number of zero-vector tests.
This counts predicate invocations, not machine instructions or bit time. 

### `enumerateNodes`

 Executable enumeration together with the exact zero-test count. 

### `interpret`

 Proof interpretation of four coefficient words in the selected field. 

### `nonzeroInterpretation`

 Coefficient vectors and abstract field elements have the same nonzero
test; this equivalence is only used to prove the node specification. 

### `nodeEquiv`

 The layout's node equivalence in the executable list order.
It does not refer to the earlier semantic arbitrary enumeration. 

### `interpretedData_nodup`

 Distinct executable node data interpret as distinct field elements. 

### `nodeQuad`

 Four residue coefficients, stored without constructing an abstract field value. 

### `liftCoefficients`

 Lift the four standard integer representatives into the prime-power base. 

### `liftCoefficients_val`

 Lifting retains each coefficient's integer value without reduction. 

### `liftQuad`

 The executable record implementing the coefficientwise residue section. 

### `quotientDenote_nodeQuad`

 The executable node record denotes the node in the layout's list order. 

### `quotientDenote_liftQuad`

 Coefficientwise lifting of an input record realizes the semantic section. 

### `quotientDenote_liftedNodeQuad`

 This is the node-lift refinement used by the explicit lifted layout. 

### `liftedNodeData`

 The complete array of lifted records preserves the explicit node-list order. 

### `encodedNodeData`

 Each entry is four fixed-width binary coefficient words. 

### `encodedNode_eq_encodeSelected`

 Encoding a generated record is exactly the canonical encoding of its
interpreted section value. The executable side performs no quotient extraction. 

### `encodedNodeTape`

 A contiguous, executable output tape containing the entire lifted-node table. 

### `encodedNodeArray`

 An actual random-access array, in the same explicitly generated order. 

### `encodeCoefficients`

 Residue-field coefficient encoding uses the same four words at exponent one. 

### `encodedFieldData`

 The residue-field table is produced directly from its coefficient vectors. 
