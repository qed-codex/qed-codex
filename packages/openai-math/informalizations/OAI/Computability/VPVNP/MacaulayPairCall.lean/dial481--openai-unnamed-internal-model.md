---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical Macaulay entry arms with restored scratch banks

Both arms preserve the two ordinal words, the degree and cardinality
parameters, and the unary label counter. The equation arm prepends the
ordered residual exponent words and a full-word divisibility flag. The
powered-monomial arm prepends one full-word equality flag. Temporary raw
keys are erased before returning to the matrix reader.


### `scans`

 Perform the source ordinal lookup and then the column ordinal lookup, retaining both raw
keys. 

### `clearKeys`

 Erase the two temporary raw-key stacks before returning to the caller. 

### `equation`

 Return the packed column-minus-source exponents and a divisibility flag after looking up
both monomials and clearing their keys. 

### `powered`

 Return the equality flag comparing the column with the shifted and scaled source monomial,
then clear both temporary keys. 

### `Monomial`

 A bounded-degree exponent vector on the input variables, with its degree bound taken from
the source or column side. 

### `Ordinals`

 Valid indices into the bounded-monomial enumerations for the source and column. 

### `monomial`

 The bounded monomial at the selected ordinal on the indicated side of the entry query. 

### `scanClock`

 Combined tick allowance for the source and column ordinal searches at their respective
degree bounds. 

### `clearCost`

 Tick allowance to clear two raw-key stacks of at most w bits each and return. 

### `equationSpace`

 Maximum stack allowance for ordinal lookup, residual packing and final cleanup in the
equation arm. 

### `poweredSpace`

 Maximum stack allowance for ordinal lookup, powered-exponent comparison and final cleanup
in the powered arm. 
