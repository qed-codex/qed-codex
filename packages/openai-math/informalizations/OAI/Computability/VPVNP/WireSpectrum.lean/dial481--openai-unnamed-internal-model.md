---
{
  "module": "OAI/Computability/VPVNP/WireSpectrum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireSpectrum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireSpectrum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectral points on finite multipartite tensors

A spectral point of Section 2 of *VP and VNP differ over every field* is a
nonnegative, normalized, additive and multiplicative function that is monotone
under local linear restriction. This presentation uses coefficient arrays and
derives invariance under mutual restrictions from monotonicity.


### `SpectralPoint`

 A spectral point on finite multipartite tensors over `k`. 

### `SpectralPoint.value`

 The nonnegative real value assigned to each tensor by this point of the asymptotic
  spectrum. 

### `diagonal_reindex_mutual`

 A bijection of labels gives mutual restrictions between the diagonals. 

### `diagonal_sum_mutual`

 The diagonal on a disjoint union and the direct sum of the diagonals have
the same coefficients in the sum basis. 

### `diagonal_unit_mutual`

 A one-dimensional diagonal is mutually restrictable with the unit. 

### `value_eq_of_mutual`

 Mutual restrictions give equal spectral values. 

### `value_add_le`

 Ordinary addition of arrays in common bases is subadditive at a spectral point. 

### `one_le_value`

 The unit restriction bounds each nonzero tensor's spectral value from below. 

### `value_sum_le`

 Subadditivity for finite ordinary sums in common bases. 

### `value_diagonal_congr`

 Changing the finite index set of a diagonal by a bijection preserves its value. 

### `value_diagonal_sum`

 The diagonal indexed by a disjoint union is the direct sum of its two diagonals. 

### `value_diagonal_fin`

 Every spectral point has value `n` on the `n`-dimensional all-parties diagonal. 

### `value_diagonal`

 The diagonal value counts its finite index set. 

### `value_le_basis_product`

 The coordinate rank bound controls the spectral value of every tensor. 

### `tensorFamilyProduct`

 Product of a finite family of tensors, regrouping all factors at each party. 

### `value_tensorFamilyProduct`

 Finite multiplicativity, including the empty product. 

### `value_wireNetwork`

 The value of an equality-wire network is the product of the values of its individual
edges, even if endpoints repeat or different wires have different index types. 

### `value_wire_equiv`

 Equal wire index cardinalities give equal spectral values. 

### `wireDimension`

 The spectral value of a wire as a multiplicative function of its dimension. 

### `wireDistance`

 Base-two logarithm of the two-dimensional wire value, as in Section 2.1. 

### `wirePseudoMetric`

 The wire pseudometric induced by a spectral point on the party set. 

### `value_wire_eq_rpow`

 Every positive-dimensional wire follows the same power law at this spectral point. 

### `value_cutFactorization_le`

 The spectral value of a matrix factorization is bounded by the product of the
wire values between terminals and centers and the wire between centers. 

### `value_wireNetwork_eq_prod_rpow`

 Each edge contributes its index cardinality raised to the distance between
its endpoints. This includes parallel edges and loops. 

### `value_binary_wireNetwork`

 The value of binary wires with varying bit widths, as used in Section 6. 

### `log2_value_binary_wireNetwork`

 The base-two logarithm of a binary wire network's spectral value is the
sum of edge widths weighted by wire distances. 
