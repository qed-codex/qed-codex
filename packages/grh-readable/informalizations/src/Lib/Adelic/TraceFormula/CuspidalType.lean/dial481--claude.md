---
{
  "module": "src/Lib/Adelic/TraceFormula/CuspidalType.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CuspidalType.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CuspidalType.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An irreducible label in a tuple gives a cuspidal test function

Green's class function of a monic irreducible polynomial is cuspidal: over a finite field, it has
mean zero on the unipotent radical of every proper parabolic subgroup of `GL_n` that is cut out by
coordinates. If the polynomial is a label of degree `n` (so its constant term is nonzero), it
follows that the coefficients of its idempotent have sum zero over each coset of such a radical.
Inflated to the finite adelic group, the idempotent of a tuple of polynomials, one of which is an
irreducible label, gives a test function that is cuspidal at the place of that member.

Notions from other files:
* `labelChar θ c` is the class function of Green that belongs to the polynomial `c` and the
  multiplicative character `θ`, here always the chosen `faithfulChar k`; `labelIdem n c`
  is its idempotent in the group algebra of `GL_n`, and `tupleIdem n c` the tensor product of these.
* `radicalHom` at the projector `p` on a set `T` of coordinates sends `Z` to the element
  `1 + p Z (1-p)` of the unipotent radical of the parabolic subgroup of `T`. Sums over the radical
  are taken over all matrices `Z`, so that every element is counted equally often.
* `levelOf w ⊥` is the kernel of the reduction `stdLevel.reduceFamily w` of `stdLevel E n`, the
  maximal compact subgroup of the finite adelic unitary group `Gf E n`, at the places `w i`;
  `liftResidue` is a section of that reduction.
* `convIndicator _ _ a` is the convolution of `a` with the indicator of an open compact subgroup,
  and `IsCuspidalAt _ φ` says that all translates of `φ` have sum zero over the cosets of the proper
  radicals at a split place.

## Relation to the literature

The finite-field input is part of Green's theory of the characters of `GL_n(F_q)`; see
`Lib.LocalGL.Green.TauFunctions`.


### `upperRightBlock`

 For a set `T` of coordinates, the block of a matrix with rows in `T` and columns outside `T`,
as a linear map. 

### `upperRightBlock_surjective`

 Every linear map from the coordinates outside `T` to those in `T` is the upper right block of
some matrix. 

### `simClassOf_radicalHom`

 The element `radicalHom _ (ofAdd Z)` of the radical of `T` has the similarity class of the block
triangular endomorphism with identity blocks on the diagonal and the upper right block of `Z` off
it. 

### `finMean_comp_upperRightBlock`

 A function of the upper right block of a matrix has the same mean over all matrices as over all
linear maps. 

### `finMean_labelChar_radicalHom`

 For a monic irreducible polynomial `c` over a finite field and a set `T` of coordinates that is
neither empty nor everything, Green's class function `labelChar (faithfulChar k) c` of `c`,
evaluated on `GL n k`, has mean zero on the unipotent radical of the parabolic subgroup of `T`
(the range of `radicalHom`). 

### `sum_coeff_labelIdem_radicalHom`

 For a finite field `k`, let `c` be an irreducible label of degree `card n` (a monic squarefree
polynomial of that degree with nonzero constant term), and let `labelIdem n c` be the idempotent
e_c = ∑ (Ξ_c(1)/|G|)·conj Ξ_c(g)·g of the complex group algebra ℂ[G], G = GL_n(k), where Ξ_c is the
character attached to `c`. For a proper nonempty set `T` of coordinates, let ε be the coordinate
projector onto `T`; the elements `1 + ε Z (1 - ε)` form the unipotent radical of the parabolic
subgroup keeping the span of the coordinates in `T`. Then for all `y z : GL n k`, the coefficients
of e_c at `y (1 + ε Z (1 - ε)) z` sum to zero as `Z` runs over all `n × n` matrices. 

### `convIndicator_mapDomain_liftResidue`

 For places `w i`, none conjugate to another or to itself, lift an element `a` of the group
algebra of their finite groups by `liftResidue` and convolve it with the indicator of `levelOf w ⊥`.
On the maximal compact subgroup, this test function is the coefficient function of `a`, composed
with reduction. 

### `convIndicator_mapDomain_liftResidue_of_notMem`

 For places `w i`, none conjugate to another or to itself, the test function `convIndicator` of
an element of the group algebra of their finite groups, lifted by the section `liftResidue` of
reduction and convolved with the indicator of `levelOf w ⊥`, vanishes off the maximal compact
subgroup `stdLevel E n`. 

### `sum_coeff_tupleIdem_radicalHom`

 Let `c` be a tuple of polynomials over finite fields `k i` whose member at `x` is an irreducible
label of degree `card n` (monic, squarefree, nonzero constant term), and `T` a proper nonempty set
of coordinates. Then the coefficients of `tupleIdem n c`, the tensor product of the idempotents of
the `c i`, have sum zero over each coset of the radical of `T` in the factor at `x`. 

### `isCuspidalAt_convIndicator_tupleIdem`

 Let `w` be a family of places, none conjugate to another or to itself, and `c` a tuple of
polynomials over their residue fields whose member at `x` is an irreducible label of degree
`card n`. Then for every element `b` of the group algebra of the finite adelic unitary group, the
product of `b` with the lift of `tupleIdem n c` by `liftResidue`, convolved with the indicator of
the kernel `levelOf w ⊥` of reduction, gives a test function that is cuspidal at the split place
`w x` (`IsCuspidalAt`: the translates have sum zero over each coset of each proper radical). 
