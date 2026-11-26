---
{
  "module": "OAI/Computability/VPVNP/WireTensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireTensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireTensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multipartite tensors and local restrictions

Finite coefficient arrays implement the restriction preorder of Section 2 of
*VP and VNP differ over every field*. Each party has its own finite basis. A
local restriction independently applies one matrix at each party. The ordinary
sum of arrays in the same bases differs from the direct sum, which uses separate
local coordinate blocks at every party.


### `Array`

 A scalar for every simultaneous choice of one basis index at each party. 

### `Tensor`

 A tensor given by its entries in a finite basis at each party. 

### `Tensor.Basis`

 The basis-index type for the tensor factor at each party. 

### `Tensor.coeff`

 The coefficients of the tensor in the specified product basis. 

### `applyLocal`

 Apply a linear map at each party, contracting its old index against the
corresponding column of the matrix. 

### `Restricts`

 The tensor restriction preorder, oriented from supply to demand. 

### `tensorProduct`

 Product with parallel factors regrouped at each party. 

### `unit`

 The simple unit tensor with singleton bases. 

### `diagonal`

 The all-parties equality tensor. 

### `directSum`

 The direct sum includes the first array in the left block and the second
array in the right block. The coefficient vanishes on every mixed block. 

### `wire`

 A wire has one endpoint index at `a`, one at `b`, and trivial factors at
other parties. The proof-indexed functions keep both local factors even when
the two endpoints coincide. 

### `applyLocal_pullback`

 Selecting one old coordinate at each party pulls back the coefficient array. 

### `applyLocal_comp`

 Composing two local restrictions multiplies the matrices at each party. 

### `restricts_of_reindex`

 Relabeling the finite bases at every party gives mutual local restrictions. 

### `Restricts.tensorProduct`

 Independent restrictions of two tensors combine after the parallel local
factors are regrouped, by taking their Kronecker products at each party. 

### `directSum_coeff_inl`

 Coefficients on the first block of the direct sum. 

### `directSum_coeff_inr`

 Coefficients on the second block of the direct sum. 

### `directSum_coeff_mixed`

 An entry using the left block at one party and the right block at another is zero. 

### `applyLocal_directSum`

 A local map on a direct sum acts separately on the two blocks, after which
the resulting arrays are added in the ordinary sense. 

### `directSum_restricts_add`

 Merging corresponding coordinates of the two blocks realizes the
ordinary sum as a restriction of the direct sum. 

### `directSum_restricts`

 Local restrictions on the two summands act independently on the corresponding
blocks at each party. 

### `directSum_restricts_left`

 Projection onto the first coordinate block restricts a direct sum to its first summand. 

### `directSum_restricts_right`

 Projection onto the second coordinate block restricts a direct sum to its second summand. 

### `placedTensor`

 Move the factors indexed by `R` to the prescribed parties, grouping all
factors at the same party into one local basis. 

### `wireNetwork`

 The tensor enforcing equality of the indices at both ends of every edge.
The local basis lists its incoming and outgoing endpoint indices separately. 

### `edgeAssignment`

 Encode a global assignment of indices to edges as the local half-wire
assignments at a party. This is the point on the diagonal of the wire tensor. 

### `applyLocal_wireNetwork`

 Contraction of the equality network leaves exactly one sum per edge,
including when there are parallel edges or repeated parties. 

### `restricts_unit_of_ne_zero`

 A nonzero coefficient gives a restriction to the unit tensor. Each party
selects its coordinate, and one party divides by the selected coefficient. 

### `diagonal_restricts_of_card`

 The diagonal indexed by all tuples of basis coordinates restricts to
the tensor, giving the product of the local dimensions as a rank bound.
One party contributes the selected coefficient, and all parties check their
component of the tuple. 

### `monotone_dimension_power_law`

 In Section 2.1, the monotonicity and multiplicativity of the value on
integer-dimensional wires force the power law. For each power of `q`, compare
the adjacent powers of two and then apply the same comparison to their images. 

### `wire_swap`

 Swapping the endpoints of a wire permutes the local bases. 

### `wire_restricts_of_embedding`

 A wire on a smaller index set is obtained by coordinate selection at its endpoints. 

### `wire_tensorProduct`

 The two coordinate components of an ordered pair give the two parallel wires. 

### `diagonal_restricts_wire`

 Sending each copy of the unit to the matching pair of endpoint basis
vectors produces a wire of the same dimension. 

### `wire_one`

 A one-dimensional wire is the simple unit, including when its endpoints coincide. 

### `unit_restricts_loop`

 A loop carries both endpoint indices at a single party, so its Kronecker
delta can be created by a linear map from that party's one-dimensional leg. 

### `restricts_wire_triangle`

 Contracting the common endpoint of two wires produces the wire between
their outside endpoints. This works even when some of the three parties coincide. 

### `cutBasis`

 The extra edge in `Option R` carries the factorization index. 

### `cutSource`

 The terminals feed into the center on their own side. The remaining edge
carries the common matrix-factorization index from the first center to the second. 

### `cutTarget`

 Send each routed wire to the center on its selected side of the cut, and the auxiliary wire
to the true-side center. 

### `cutFactorization_restricts`

 Any matrix factorization across a cut of the terminal roles can be realized
by terminal-to-center wires plus a rank wire between the two centers. Roles and
centers may coincide as parties. Used for both shifted cuts in Lemma 3.2. 
