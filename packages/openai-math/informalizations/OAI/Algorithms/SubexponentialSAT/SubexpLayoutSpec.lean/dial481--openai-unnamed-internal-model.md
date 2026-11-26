---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLayoutSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Semantic interface for the multicolor interpolation layout

This is the output specification of Lemma 3.2 in `subexponential-sat.txt`.
It does not assert the existence of these layouts or a running-time bound.
The numerical parameters may grow with the input, and quantitative construction
costs are separate from this finite algebraic interface.

A factor of color `g` annihilates the subspaces of every **other** color.
Rows remain incidence-specific. All subspaces and dimensions are over `ZMod p`;
only interpolation coefficients and points use the extension field.


### `Parameters`

 Semantic numerical parameters. The formula for `R` and the binomial-tail
and block-packing hypotheses belong to the construction, not to this output
specification. `tau` is rational to retain exact quantitative inequalities. 

### `Layout`

 The multicolor layout on a bounded factor pattern. Rational dimension
inequalities and the integer support inequality avoid any rounding weakening. 

### `fieldEquiv`

 Adding zero to the node enumeration enumerates the extension field. 

### `rowMap`

 Every row evaluation is linear over the base field. 

### `localK`

 The same subspace expressed only on its support coordinates. 

### `dimension_le_support`

 Subspace dimension cannot exceed the number of supporting coordinates. 

### `dimensions_sum_lower`

 Summing the individual lower bounds retains the full `(1-tau)^2 D`. 

### `Outside`

 Complement coordinates outside all color supports. 

### `Outer`

 Complement coordinates and one quotient class per color. 

### `Inner`

 An actual point of the specified color's coset. 

### `coordinateOuterFiberEquiv`

 All actual assignments, partitioned into outer choices and the dependent
product of their color-coset points. 

### `reconstruct_components`

 Reconstruction has exactly the complement and color coordinates supplied
to it; this is the interface for factorizing the actual moment weights. 

### `Iterations`

 One outer choice and one term from one of its individual inner sums. 

### `iteration_bound`

 The exact iteration type satisfies (4.7). This is a cardinality theorem,
not a claim about the bit cost of creating or traversing its elements. 

### `EnumerationData`

 Explicit finite-array data consumed by a separated evaluator. The stored
functions return actual vectors. `assignmentEquiv` certifies complete, unique
enumeration; its inverse must have the displayed additive form.

This is a consumer contract, not an asserted construction. In particular, no
choice-based basis selection is represented as an executable-cost proof. 

### `increment`

 The actual within-coset vector at one array index. 

### `zeroIndex`

 An index for the zero increment, without assuming a particular array order. 

### `innerCount_eq`

 Inner array lengths are derived from the supplied equivalences. 

### `outerCount_eq`

 The exact outer length follows from unique enumeration and the dimensions;
it is not a cost assertion stored as a field. 

### `iterationCount`

 The exact number of individual inner terms scanned across all outer data. 

### `rowMap_base_add_sum`

 A row can be evaluated at just the basepoint and its own color increment;
the other color increments make zero contribution to its residue. 

### `LiftedLayout`

 Node and incidence-polynomial lifts for multicolor counting. 

### `ofSurjective`

 Algebraic construction from a surjective residue map; no executable cost
is claimed for the classical preimage selections in this definition. 

### `beta_eq_of_sub_mem`

 A factor's beta ignores translations in any subspace of another color. 

### `beta_reconstruct_eq`

 With all outer data fixed, beta depends on just its factor's own color
component, even when every other component changes within its coset. 

### `beta_enumeration_eq`

 The explicit-array evaluator likewise needs only one color increment to
compute a factor's beta value. It never needs the product of all inner arrays. 
