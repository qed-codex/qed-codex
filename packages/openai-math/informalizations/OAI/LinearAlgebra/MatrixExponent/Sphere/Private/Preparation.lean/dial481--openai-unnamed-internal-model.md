---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Preparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Preparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Preparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fermionic pairing sums

The recursion pairs the first generator with one of the remaining ones.
Moving the partner left by one position changes its sign. Cancellation
of repeated generators uses a square-zero contraction, even in characteristic two.


### `contract`

 Sum over deletions of one generator, with alternating signs. 

### `wick`

 The signed perfect matching sum in list order. 

### `wick_reverse_sign`

 Reversing a list exchanges its first and last element, then its second
and penultimate element, and so on. 


# Splitting a Wick pairing sum

A partial matching contracts some pairs and applies a residual weight to
the unmatched generators in their original order. The decomposition only
uses commutative ring operations.


### `partialWick`

 Signed sum over partial matchings, weighted by the residual list. 

### `partialWick_contract`

 Deletion commutes with the partial matching sum because each contracted
pair crosses an unmatched generator with sign one. 

### `wick_add`

 Choose which pairs use the first kernel. All other pairs use the second. 

### `partialWick_append`

 When no contraction crosses a boundary, the two partial matchings
can be chosen independently. The remaining generators stay in site order. 

### `wick_add_append`

 Expand only the internal contractions of a single cluster. 

### `partialWick_congr`

 The residual generator list always has the original parity. 

### `wick_linear`

 Linearity in one row and its corresponding column. 

 Additive degrees of perfect pairing monomials. 

### `BinaryForm`

 Two charts of a homogeneous binary form of degree `n`. 


# Ordered wedge coordinates

Adjacent swaps contribute minus signs. Vanishing on repeated generators is a
separate condition so normalization is valid also in characteristic two.


### `energy_mod_two`

 Every mode contributes an odd amount of doubled energy. 

### `normalize`

 The same ordered basis coordinates work for every alternating evaluation. 


# Factoring a Wick sum through an ordered wedge basis

After contracting a partial matching inside a cluster, each remaining
row is a finite linear combination of the center rows. The coefficients
of the resulting ordered wedges are uniform in the exterior list.


### `wick_factor`

 A cluster in a kernel with an internal and a residual part factors
through finitely many basis wedges. Each spectator list may be chosen
after the coefficients have been fixed. 


# Changing generators in a wedge

The expansion in the ordered basis is independent of all spectator
insertions. It preserves length and respects additive energy bounds.


 # Preparing a coefficient tensor at one auxiliary site 

### `preparation_lower`

 Sending all legs of a common binary label costs at least one bit. 
