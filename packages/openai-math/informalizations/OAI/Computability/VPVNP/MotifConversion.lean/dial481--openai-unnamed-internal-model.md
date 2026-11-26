---
{
  "module": "OAI/Computability/VPVNP/MotifConversion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifConversion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifConversion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Conversion of a fixed wire motif

Theorem 6.1 of *VP and VNP differ over every field* converts the spectral
inequality (6.1) into ordinary tensor identities. All scalar parameters and
their integer equations are chosen before the input widths. A local matrix
entry is represented independently of the coefficient ring by either failure
or the list of parameter indices whose product is the entry.


### `parameterData`

 The integral demand and supply arrays used in the fixed polynomial equations. 

### `Selector`

 A base-identity selector, comprising a copy index and one supply-grid choice per
tensor-power factor. 

### `basePayload`

 Supply widths of one selected copy of the base identity. 

### `selectorCode`

 One fixed finite encoding of the base selectors, including invalid bit words. 

### `repetitions`

 Compute the block repetitions using integer arithmetic. 

### `outerIndices`

 The set of admitted outer supply payloads. Testing one supplied index uses
only the fixed integer mass coefficients, without enumerating this set. 

### `supplyWidths`

 Total widths, including a complete selector list on each supply edge. 

### `demandGrid`

 Rounded demand grid point found by scanning the fixed table of grid points. 

### `baseDemand`

 Demand width for edge `e` at grid point `z`, scaled by the block multiplier and tensor
power. 

### `entry`

 A local entry description before substituting any scalar parameters. 

### `evalEntry`

 An absent description evaluates to zero. A successful description evaluates
to one parameter per copy. 

### `entry_monomial`

 The local description specializes to zero or a single monomial of degree at
most the number of base copies, including when that number is zero. 

### `identity`

 The ordinary sum identity in (6.2), over any commutative ring and every
assignment satisfying the fixed integral equations. 

### `linear_index_bound`

 The fixed number of outer coordinates, and the degree of every evaluated
monomial, use at most linearly many bits of wire payload per input-width unit. 

### `selectorTable`

 The fixed finite selector table used in the local entry evaluator. 

### `lookup`

 A base matrix entry's index in the fixed parameter vector. 

### `runEntry`

 The bit-string evaluator specialized to this block, with fixed finite table
and code. The count records bit probes and word operations of the local scan. 

### `runEntry_correct`

 The actual bit-string evaluator returns the matrix entry used in (6.2)
after evaluating the reported parameter list. 

### `runEntry_cost`

 With the motif and its tables fixed, the number of bit probes and word
operations has absolute exponent two in the largest demand width. 

### `sequential_entry_cost`

 With sequential storage one can rescan a string from its beginning for
every indexed bit probe. The resulting allowance is cubic in the maximum
input width, with a coefficient fixed before seeing the input. 

### `exists_conversion`

 The spectral bound (6.1) yields fixed integral equations, a solution in
the given field, and the identities (6.2) over every ring satisfying those
equations. The block and its additive error are fixed before the input widths.
The entry descriptions and outer indices are shared across all assignments. 
