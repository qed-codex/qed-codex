---
{
  "module": "src/New/Determinant/Exchange/OneSquare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/OneSquare.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/OneSquare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One square: up then down against down then up

The exchange identity `New.Exchange.exchange_identity` for the space `U₁ ⊕ U₂`, read as a statement
on theta lifts of forms from `U₁` to `U₂`: its kernels are products of kernels for `U₁` and `U₂`.

* `New.Exchange.pairTransposedLift_comp_pairLift_mul`,
  `New.Exchange.pairLift_comp_pairTransposedLift_mul`: the path up to `A` and down, and the path
  down to `A'` and up, transform by the tame character.
* `New.Exchange.IsSquare`: the conditions on the four pairs of a square.
* `New.Exchange.exists_sum_pairLift_comp_pairTransposedLift_eq_smul`: for four pairs with their own
  splitting characters, the two paths agree on matched functions up to the factor `κ / c`, where `κ`
  may be zero.
* `New.Exchange.one_square_identity_of_isEdgeFamily`: the case of two families of characters indexed
  by finite types, in the form of the relation `New.Exchange.SquareLaw`.

Notions from other files:
* `New.modDatum S T 𝔪 Ψ v`: the theta datum on `Hom(S, T)` with real part the Fock vector `v`, given
  by the function `Ψ` on matrices modulo `𝔪` at the places dividing `𝔪` and by the vacuum elsewhere.
  The point datum at `x` is the case `Ψ = Pi.single x 1`, the indicator function of `x`;
* `New.Fock.fockMoment N v` is `∫ (1 + ‖z‖) ^ N * |v z| dz`, the moment of order `N` of the Fock
  vector `v`;
* a type of forms on a space is a function on its real unitary group, which prescribes the
  behavior of a form at the infinite places;
* `New.AutChar E`: the continuous characters of `[U(1)]`, the norm-one ideles of `E` modulo those
  from `E`;
* `New.Exchange.pairLift`, `New.Exchange.pairTransposedLift`: the lift and the transposed lift;
* `New.Exchange.IsPairEdge a b e e' P`, an edge `e → e'`: each of the families of characters `a`,
  `b` has a fixed weight, and for these weights the types `e`, `e'` and the Fock vector of `P` are
  such that the theta integral lifts forms of type `e` to forms of type `e'`;
  `New.Exchange.IsEdgeFamily` asks this of one family of characters indexed by finite types;

## Relation to the literature

A transposed lift followed by a lift is a multiple, possibly zero, of a lift followed by a
transposed lift. For forms on two unitary groups, the theta liftings through a group `A` and through
a group `A'` of no larger rank agree on matched ramified data, up to the L-value constant of the
exchange theorem and a factor free of the twist that may be zero. This moves lifts past each other
in chains. The seesaw principle and a rank-one exchange of periods are known in the literature.
Related work: Kudla, Seesaw dual reductive pairs, 1984; Chan, Period identities of CM forms on
quaternion algebras, 2020; He, Compositions of theta correspondences, 2005.


 ### Point data and characters 

### `pairWeil_modDatum_single_mul_left`

 Let `k = liftMod g` be the chosen integral finite adelic point of `U(T)` with residue `g` modulo
`𝔪`. In the Weil representation `pairWeil S T α β` of `U(S) × U(T)`, twisted by the characters `α`,
`β`, let `k⁻¹` act in the finite part of `U(T)`, all other components being `1`. It sends the point
datum at `g x` to `(α (det k))⁻¹` times the point datum at `x`. 

### `pairWeil_modDatum_single_mul_right`

 Let `k = liftMod g` be the chosen integral finite adelic point of `U(S)` with residue `g` modulo
`𝔪`. In the Weil representation `pairWeil S T α β` of `U(S) × U(T)`, twisted by the characters `α`,
`β`, let `k` act in the finite part of `U(S)`, all other components being `1`. It sends the point
datum at `y g` to `(β (det k))⁻¹` times the point datum at `y`. 

### `hasLeftInv_transpose_of_areMatched`

 Let `Ψ`, `Ψ'` be matched for the character `χ` over the whole residue ring (`⊤`), the indices
being split by `σ`; in particular `Ψ` vanishes off the blocks of rows `n'` of invertible matrices.
Then `Ψ` vanishes off the onto matrices, those whose transpose has a left inverse. 

### `hasLeftInv_of_areMatched`

 Let `Ψ`, `Ψ'` be matched for the character `χ` over the whole residue ring (`⊤`), the indices
being split by `σ`; in particular `Ψ'` vanishes off the blocks of columns `n` of invertible
matrices. Then `Ψ'` vanishes off the left invertible matrices. 

### `IsTameFor.exists_inv_rankTwist_inv`

 Let the character `ν` of `[U(1)]` be tame of weight `μ` for `(𝔪, χ)`: `𝔪 ≠ 1`, `ν` has weight
`μ` at the infinite places, its tame part is nontrivial exactly at the places dividing `𝔪`, and `χ`
is the character of the residue ring that the tame part defines. Then the inverse of
`rankTwist ν⁻¹ N = ν⁻¹ * upsilonU1 ^ (card N / 2)` is tame for `(𝔪, χ)`, of some weight `μ'`. 

### `integral_integral_sum_eq`

 Suppose each `F i` with nonzero coefficient `c i` is integrable for the product of the quotient
measures of `U₁`, `U₂` and `A`, with integral `r i`. Then the iterated integral of `∑ i, c i • F i`
equals `∑ i, c i • r i`. The inner integral is over `A` and the outer one over `U₁ × U₂`. 

### `exists_integrable_kernel_bound`

 Let `s` be any sign vector and `fockSpace s` its Fock space. For `v` in it with finite moment
`fockMoment N v = ∫ (1 + ‖z‖) ^ N * |v z| dz`, let `K v` be a continuous kernel on `U₁ ⊕ U₂` and
`A`, bounded by a multiple of that moment times a power of the height on `U₁ ⊕ U₂`, uniformly in the
variable of `A`. Let `φ₁`, `φ₂` be rapidly decreasing functions on the adelic unitary groups of
`U₁`, `U₂`, and `ν₀` a character of `[U(1)]`. Then `φ₁ g₁ * φ₂ g₂ * ν₀ (det g₂) * K v (g₁ ⊕ g₂) z`,
as a function on `(U₁ × U₂) × A`, is integrable and bounded by a constant times a moment of `v`. 

### `exists_eq_mul_of_forall_polyVector`

 Let `s` be a sign vector on a finite index type `n`, so that a polynomial `P` in variables
indexed by `n` has a Fock vector `polyVector s P`. Let numbers `Λ j v` depend on a Fock vector `v`,
each being Lipschitz for one moment `fockMoment N v = ∫ (1 + ‖z‖) ^ N * |v z| dz`. If, for every
polynomial `P`, the numbers `Λ j (polyVector s P)` are one multiple of given numbers `ρ j`, the same
holds for every vector `x` whose moments are all finite. 

 ### The kernels multiply 

### `modKernel_single_sum_left`

 Let `U₁`, `U₂`, `A` be hermitian spaces, `ν₀` and `aᵢ`, `bᵢ` characters of `[U(1)]` with
`b₂ * ν₀ = b₁`. Take the indicator function of `x` and the product of `P₁` and `P₂`, read by
`renameRowsCols` in the variables of the two column blocks. Then the kernel of `(U₁ ⊕ U₂, A)` at
`g₁ ⊕ g₂`, for the characters `a₁ a₂` and `b₁`, is the product of the kernels of `(U₁, A)` and
`(U₂, A)`, for the column blocks of `x`, divided by `ν₀ (det g₂)`. 

### `modKernel_single_sum_right`

 Let `A'`, `U₁`, `U₂` be hermitian spaces, `ν₀` and `aᵢ`, `bᵢ` characters of `[U(1)]` with
`b₁ * ν₀ = b₂`. Take the indicator function of `y` and the product of `P₁` and `P₂`, read by
`renameRowsCols` in the variables of the two row blocks. Then the kernel of `(A', U₁ ⊕ U₂)` at
`g₁ ⊕ g₂`, for the characters `b₁` and `a₁ a₂`, is the product of the kernels of `(A', U₁)` and
`(A', U₂)`, for the row blocks of `y`, divided by `ν₀ (det g₂)`. 

### `upIntegrand`

 The theta kernel of `(U₁ ⊕ U₂, A)` for the point datum at `x` with real part `w`, at
`(g₁ ⊕ g₂, h)`, times `f₁ g₁ * f₂ g₂ * ν₀ (det g₂)`. The characters `γ`, `b` of `[U(1)]` twist the
Weil representation in the kernel by `γ (det h) * (b (det (g₁ ⊕ g₂)))⁻¹`. 

### `downIntegrand`

 The theta kernel of `(A', U₁ ⊕ U₂)` for the point datum at `y` with real part `w`, at
`(h, g₁ ⊕ g₂)`, times `f₁ g₁ * f₂ g₂ * ν₀ (det g₂)`. The characters `γ`, `b` of `[U(1)]` twist the
Weil representation in the kernel by `(γ (det h))⁻¹ * b (det (g₁ ⊕ g₂))`. 

### `upIntegrand_add`

 The function `upIntegrand` is additive in its real datum, the Fock vector in
`PairFock E (s₁ ⊕ᵥ s₂) s'`: its value at `v + w` is the sum of its values at `v` and at `w`. 

### `upIntegrand_sub`

 The function `upIntegrand` respects differences in its real datum, the Fock vector in
`PairFock E (s₁ ⊕ᵥ s₂) s'`: its value at `v - w` is its value at `v` minus its value at `w`. 

### `exists_upIntegrand_bound`

 Let `x` be onto modulo an ideal `𝔪` with at least one prime divisor (`𝔪 ≠ 1`), let `f₁`, `f₂`
be automorphic functions of rapid decay for the hermitian spaces `U₁`, `U₂`, and let `ν₀`, `γ`, `b`
be any characters of `[U(1)]`. At `((g₁, g₂), h)`, `upIntegrand` is `f₁ g₁ * f₂ g₂ * ν₀ (det g₂)`
times the theta kernel of `(U₁ ⊕ U₂, A)`, twisted by `γ (det h) * (b (det (g₁ ⊕ g₂)))⁻¹`, for the
point datum at `x` with real part `w`: the theta datum whose part at `𝔪` is the indicator function
of `x` and whose part at infinity is `w`, a vector of the Fock space of the pair (`PairFock`).
There are `N` and `D` such that, whenever `fockMoment N w = ∫ (1 + ‖z‖) ^ N * |w z| dz` is finite,
this function is integrable for the product of the quotient measures of `U₁`, `U₂`, `A` and
bounded by `D * fockMoment N w`. 

### `integrable_upIntegrand`

 Let `𝔪` have at least one prime divisor (`𝔪.places` nonempty), and let `x` be a matrix modulo
`𝔪` whose transpose `xᵀ` has a left inverse. Let `f₁`, `f₂` be automorphic functions of rapid decay
for `U₁`, `U₂`. Let all moments `fockMoment N w` of the Fock vector `w` be finite. Then
`upIntegrand` at `x` and `w`, for any characters `ν₀`, `γ`, `b` of `[U(1)]`, is integrable for the
product of the quotient measures of `U₁`, `U₂`, `A`. 

### `exists_norm_integral_upIntegrand_sub_le`

 Let `x` be onto modulo `𝔪 ≠ 1`, let `f₁`, `f₂` be automorphic functions of rapid decay for `U₁`,
`U₂`, and let `ν₀`, `γ`, `b` be any characters of `[U(1)]`. Here `upIntegrand` is the product of
`f₁ g₁`, `f₂ g₂`, `ν₀ (det g₂)` and the theta kernel of `(U₁ ⊕ U₂, A)`, twisted by `γ`, `b`, for the
indicator of `x` modulo `𝔪` and a vector `v` of the Fock space, the real part of the datum. Let
`J v` be its integral for `μA`, the product of the quotient measures of `U₁`, `U₂`, `A`. There are
`N` and `D` with `‖J v - J v'‖ ≤ D * fockMoment N (v' - v)` whenever `v`, `v'` and `v' - v` have a
finite moment of order `N`. 

### `integrable_downIntegrand`

 Let `y` be left invertible modulo `𝔪 ≠ 1`, let `f₁`, `f₂` be automorphic functions of rapid
decay for `U₁`, `U₂`, and let `ν₀`, `γ`, `b` be any characters of `[U(1)]`. At `((g₁, g₂), h)`,
`downIntegrand` is `f₁ g₁ * f₂ g₂ * ν₀ (det g₂)` times the theta kernel of `(A', U₁ ⊕ U₂)`, twisted
by `(γ (det h))⁻¹ * b (det (g₁ ⊕ g₂))`, for the point datum at `y` with real part the Fock vector
`w`. If all moments `fockMoment N w = ∫ (1 + ‖z‖) ^ N * |w z| dz` are finite, it is integrable for
the product of the quotient measures of `U₁`, `U₂`, `A'`. 

### `integral_upIntegrand`

 Let `b₂ * ν₀ = b₁`, let `x` be a matrix modulo `𝔪` and let `P₁`, `P₂` be polynomials on the
pairs `(U₁, A)`, `(U₂, A)`. `upIntegrand` is `f₁ g₁ * f₂ g₂ * ν₀ (det g₂)` times the theta kernel of
`(U₁ ⊕ U₂, A)`. Here it is taken for the point datum at `x`, the Fock vector of `P₁ P₂` and the
characters `a₁ a₂`, `b₁`. If it is integrable, its integral is the integral over `A` of the product
of the theta lifts of `f₁`, `f₂`. 

### `integral_downIntegrand`

 Let `b₂ = b₁ ν₀`, let `y` be a matrix modulo `𝔪` and let `P₁`, `P₂` be polynomials on the pairs
`(A', U₁)`, `(A', U₂)` of spaces. Suppose `downIntegrand` is integrable for `y` and the Fock vector
`polyVector` of `P₁ P₂`, with the characters `a₁ a₂` and `b₁`. Then its integral is the integral
over `A'` of a product of two transposed lifts (`swap`). These are the lifts of `f₁` and `f₂` for
the theta kernels `pairThetaKer A' Uᵢ bᵢ aᵢ`. 

### `integral_sum_upIntegrand_eq_mul`

 Suppose that at `g = (g₁, g₂)` the theta integral `thetaIntegral` of `(U₁ ⊕ U₂, A)` with the
datum `modDatum` of `Ψ` and `w` is `c` times the integral over `A'` of the theta kernel `pairTheta`
of `(A', U₁ ⊕ U₂)` with the datum of `Ψ'` and `v`. Then the integral over `A` in `k` of
`∑ x, Ψ x • upIntegrand … x w (g, k)` is `c` times the integral over `A'` in `k` of
`∑ y, Ψ' y • downIntegrand … y v (g, k)`. 

### `exists_integral_upIntegrand_eq_mul_integral_lift`

 Let `(U₁, A)` and `(U₂, A)` be edges `e₁ → e` and `ē₂ → ē`: with the real data of the
polynomials `P₁`, `P₂`, the theta integrals lift forms of type `e₁`, `ē₂` to forms of type `e`, `ē`
on `A`. Let `w` be a real datum with finite moments, and let `b₂ i * ν₀ i = b₁ i` and `𝔪 i ≠ 1` for
all `i`. There is one number `κ` such that for every member `i` of the family, every `x` onto modulo
`𝔪 i` and all forms `f₁`, `f₂`, the integral of `upIntegrand` is `κ` times the pairing of `f₂` with
the lift of `f₁` to `A` followed by the transposed lift to `U₂`. 

### `pairTransposedLift_comp_pairLift_mul`

 Let `U₁`, `U₂`, `A` be hermitian spaces, `I` a set and, for `i` in `I`, let `(a₁ i, b₁ i)`,
`(a₂ i, b₂ i)` be the characters of `[U(1)]` on the pairs `(U₁, A)`, `(U₂, A)`. Let these pairs be
edges `e₁ → e` and `ē₂ → ē` (`IsPairEdge`): with the real data of the polynomials `P₁`, `P₂`, theta
integrals lift forms of the first type to forms of the second, a bar being complex conjugation. Take
the lift from `U₁` to `A` followed by the transposed lift to `U₂`, the data modulo `𝔪` being the
indicator functions of the two column blocks of a matrix `x` with rows `n'`, the index set of `A`.
Replacing `x` by `g x` multiplies this map by `χ (det g)`, if `(a₁ i * a₂ i)⁻¹` is tame for
`(𝔪, χ)`: it has some weight `μ` at the infinite places, and its tame part is nontrivial exactly at
the places dividing `𝔪 ≠ 1` and defines `χ` on the residue ring. 

### `pairLift_comp_pairTransposedLift_mul`

 Let `A'`, `U₁`, `U₂` be hermitian spaces, `I` a set and, for `i` in `I`, let `(b₁' i, a₁' i)`,
`(b₂' i, a₂' i)` be the characters of `[U(1)]` on the pairs `(A', U₁)`, `(A', U₂)`. Let these pairs
be edges `ē' → ē₁` and `e' → e₂` (`IsPairEdge`): with the real data of the polynomials `P₁'`, `P₂'`,
theta integrals lift forms of the first type to forms of the second, a bar being complex
conjugation. Take the transposed lift from `U₁` to `A'` followed by the lift to `U₂`, the data
modulo `𝔪` being the indicator functions of the two row blocks of a matrix `y` with columns `n`,
the index set of `A'`. Replacing `y` by `y g` multiplies this map by `χ (det g)`, if
`(a₁' i * a₂' i)⁻¹` is tame for `(𝔪, χ)`: it has some weight `μ` at the infinite places, and its
tame part is nontrivial exactly at the places dividing `𝔪 ≠ 1` and defines `χ` on the residue
ring. 

### `integral_transposedLift_mul_transposedLift`

 Let `A'`, `U₁`, `U₂` be hermitian spaces with signs `s`, `s₁`, `s₂`, let the characters
`(b₁' i, a₁' i)`, `(b₂' i, a₂' i)` of `[U(1)]` be attached to the pairs `(A', U₁)`, `(A', U₂)`, and
let these be edges `ē' → ē₁` and `e' → e₂` (`IsPairEdge`): with the real data of `P₁'`, `P₂'`, theta
integrals lift forms of the first type to forms of the second. For forms `f₁`, `f₂` on `U₁`, `U₂` of
types `e₁`, `ē₂`, the integral over the adelic unitary group of `A'`, for its quotient measure
`quotMeasure`, of the product of the transposed lifts of `f₁` and `f₂` is the pairing on `U₂` of
`f₂` with the transposed lift of `f₁` to `A'` followed by the lift to `U₂`. 

### `integral_integral_sum_downIntegrand`

 Let `A'`, `U₁`, `U₂` be hermitian spaces with pairs `(A', U₁)`, `(A', U₂)` that are edges
`star e' → star e₁`, `e' → e₂` for the characters `(b₁' i, a₁' i)`, `(b₂' i, a₂' i)` of `[U(1)]`.
Let `b₁' i * ν₀ = b₂' i`, let `𝔪 ≠ 1`, let `Ψ'` vanish off the left invertible matrices, and let the
forms `f₁`, `f₂` of types `e₁`, `star e₂` be rapidly decreasing (`rapidFunctions`). Here
`downIntegrand` at `y` is the theta kernel of `(A', U₁ ⊕ U₂)` for the point datum at `y` with real
part the Fock vector of `P₁' P₂'`, the variables renamed to the two row blocks by `renameRowsCols`,
times `f₁`, `f₂` and `ν₀ ∘ det`. The integral over `U₁ × U₂` and `A'` (quotient measures) of its sum
over `y`, weighted by `Ψ'`, is the sum, weighted by `Ψ'`, of the pairings of `f₂` with the
transposed lift of `f₁` to `A'` followed by the lift to `U₂`. 

### `IsSquare`

 A family of squares with the same real data. The corners are spaces `U₁`, `U₂`, `A`, `A'` with
signs `s₁`, `s₂`, `s'`, `s`, and `W = U₁ ⊕ U₂`. The pairs `(U₁, A)`, `(U₂, A)`, `(A', U₁)`,
`(A', U₂)` carry the characters `(a₁, b₁)`, `(a₂, b₂)`, `(b₁', a₁')`, `(b₂', a₂')`, which depend on
the member `i` of the family, and the polynomials `P₁`, `P₂`, `P₁'`, `P₂'`. For a character `α` of
`[U(1)]`, `α.baseChange` is the Hecke character `x ↦ α (x / x̄)`, and the splitting character of a
space of rank `m` that carries `α` is `α.spaceChar m = α.baseChange * υ⁻¹ ^ m`. 

### `IsSquare.negCount_eq`

 `W` has as many negative signs as `A` and `A'` together. 

### `IsSquare.card_eq`

 The ranks of `A` and `A'` differ by `2 t`. 

### `IsSquare.negCount_lt_half`

 Half the rank of `W` exceeds the number of its negative signs. 

### `IsSquare.card_le_weight`

 The weights are at least this excess. 

### `IsSquare.tame`

 The character `ν i` of `[U(1)]` is tame of weight `μ` for `(𝔪 i, χ i)`. 

### `IsSquare.edge₁`

 The pair `(U₁, A)` is an edge `e₁ → e`. 

### `IsSquare.edge₂`

 The pair `(U₂, A)` is an edge `ē₂ → ē`. 

### `IsSquare.edge₁'`

 The pair `(A', U₁)` is an edge `ē' → ē₁`. 

### `IsSquare.edge₂'`

 The pair `(A', U₂)` is an edge `e' → e₂`. 

### `IsSquare.spaceChar_mul_up`

 On the side of `A`, the splitting characters of `U₁`, `U₂` multiply to `ν̃⁻¹`, the inverse
  base change of `ν`. 

### `IsSquare.spaceChar_mul_down`

 So do those on the side of `A'`. 

### `IsSquare.spaceChar_mul_first`

 At `U₁`, the splitting characters of `A`, `A'` multiply to `ν̃⁻¹`. 

### `IsSquare.spaceChar_mul_second`

 So do those at `U₂`. 

### `exists_sum_pairLift_comp_pairTransposedLift_eq_smul`

 On matched functions, a transposed lift followed by a lift is a multiple, possibly zero, of a
lift followed by a transposed lift.

The family satisfies `IsSquare`: the four pairs are edges; `ν i` is tame for `𝔪 i ≠ 1`: weight `μ`
at infinity, tame part nontrivial exactly at the places dividing `𝔪 i`, defining `χ i` on the
residue ring; `card n' = card n + 2 t`; the number `N` of negative signs of `W = U₁ ⊕ U₂` is that of
`A` and `A'` together, with `2 N + 2 ≤ card (n₁ ⊕ n₂) ≤ 2 μ τ + 2 N`; the splitting characters
`x ↦ α (x / x̄) * υ x ^ (-m)` of spaces of rank `m` with character `α`, `υ` being the splitting
character of the Weil data, multiply in pairs to the inverse base change of `ν i`. Let `σ` order the
index set of `W` as that of `A'` followed by that of `A`. Let `Θ i x` be the lift from `U₁` to `A`
followed by the transposed lift to `U₂`, and `Θ' i y` the transposed lift to `A'` followed by the
lift to `U₂`, the data modulo `𝔪 i` being the indicator functions of the blocks of `x`, `y`.

There are `C > 0` and `κ`, possibly zero, and for each `i` a number `c` with
`‖c‖ ^ 2 = C * lValueProd (𝔪 i).places (ν i) t ≠ 0`, such that
`∑ Ψ' y • Θ' i y = (κ / c) • ∑ Ψ x • Θ i x` for all matched functions `Ψ`, `Ψ'` of matrices modulo
`𝔪 i`. Here `lValueProd S ν t = ∏_{w ∈ S} q_w ^ (t ^ 2) ∏_{1 ≤ z ≤ t} |L^S(z, ν)| ^ 2`, with `q_w`
the residue cardinality and `L^S(z, ν)` the Euler product of the base change of `ν` outside
`S ∪ S̄`. Matched over the whole residue ring (`⊤`) means: as `k` runs over the invertible matrices
indexed by `n₁ ⊕ n₂`, `Ψ` vanishes off the blocks `x` of rows `n'` of `k⁻¹`, `Ψ'` vanishes off the
blocks `y` of columns `n` of `k`, and `Ψ x = χ i (det k) * Ψ' y` for the two blocks of one `k`. 

### `equivariant_and_exists_sum_eq_of_areMatched`

 One square: two ways to lift forms from `U₁` to `U₂`, through `A` or through `A'`, transform by
the same character and agree on matched functions up to a constant.

Let `E` be a CM field with Weil data, which fix a splitting Hecke character `υ` of `E`. Let `A'`,
`A`, `U₁`, `U₂` be hermitian spaces over `E` with index sets `n`, `n'`, `n₁`, `n₂` and signs `s`,
`s'`, `s₁`, `s₂` at the infinite places (`A'` goes with the unprimed letters). Let `σ` order the
index set of `W = U₁ ⊕ U₂` as `n` followed by `n'`. The types `e'`, `e`, `e₁`, `e₂` are functions on
the real unitary groups (`GInf`) of the four spaces; a type prescribes the behavior of a form at the
infinite places, and `U₁.Form e₁` is the space of forms of type `e₁` on `U₁`. For `i` in a set `I`,
the pairs `(U₁, A)`, `(U₂, A)`, `(A', U₁)`, `(A', U₂)` carry the characters `(a₁ i, b₁ i)`,
`(a₂ i, b₂ i)`, `(b₁' i, a₁' i)`, `(b₂' i, a₂' i)` of `[U(1)]`, the norm-one ideles of `E` modulo
those from `E`, and the polynomials `P₁`, `P₂`, `P₁'`, `P₂'`, whose Fock vectors are the real theta
data.

The hypothesis `IsSquare` says:
* the rank of `A` is that of `A'` plus `2 t`;
* the number `N` of negative signs of `W` is that of `A` and `A'` together, and
  `2 N + 2 ≤ card (n₁ ⊕ n₂) ≤ 2 μ τ + 2 N` at every infinite place `τ`;
* `ν i` is tame for `𝔪 i ≠ 1`: it has weight `μ` at the infinite places, and its tame part is
  nontrivial exactly at the places dividing `𝔪 i` and defines the character `χ i` of the residue
  ring `R = 𝓞 E / 𝔪 i`;
* the four pairs are edges `e₁ → e`, `ē₂ → ē`, `ē' → ē₁`, `e' → e₂`, a bar being complex conjugation
  (`New.Exchange.IsPairEdge`): the characters have weights independent of `i`, and the theta
  integral lifts forms of the first type to forms of the second;
* with `α[m]` the Hecke character `x ↦ α (x / x̄) * υ x ^ (-m)`, each of the four products
  `a₁[card n₁] a₂[card n₂]`, `a₁'[card n₁] a₂'[card n₂]`, `b₁[card n'] b₁'[card n]`,
  `b₂[card n'] b₂'[card n]` at `i` is the inverse of the base change `x ↦ ν i (x / x̄)`.

For a matrix `x` over `R`, `Θ i x` is the theta lift (`pairLift`) from `U₁` to `A` followed by the
transposed lift (`pairTransposedLift`) to `U₂`; the data modulo `𝔪 i` are the indicator functions of
the two column blocks of `x`. For a matrix `y` over `R`, `Θ' i y` is the transposed lift from `U₁`
to `A'` followed by the lift to `U₂`, for the indicator functions of the two row blocks of `y`.
Then:

(a) `Θ i (g x) = χ i (det g) • Θ i x` and `Θ' i (y g) = χ i (det g) • Θ' i y` for invertible `g`.

(b) There are `C > 0` and a number `κ`, possibly zero, both independent of `i`, and for each `i` a
number `c` with `‖c‖ ^ 2 = C * lValueProd S (ν i) t ≠ 0`, such that
`∑ Ψ' y • Θ' i y = (κ / c) • ∑ Ψ x • Θ i x` for all matched `Ψ`, `Ψ'`. Here `S` is the set of places
dividing `𝔪 i`, and `lValueProd S ν t = ∏_{w ∈ S} q_w ^ (t ^ 2) ∏_{1 ≤ z ≤ t} |L^S(z, ν)| ^ 2`, with
`q_w` the residue cardinality and `L^S(z, ν)` the Euler product of the base change of `ν` outside
`S ∪ S̄`. 

### `one_square_identity_of_isEdgeFamily`

 The case of `New.Exchange.equivariant_and_exists_sum_eq_of_areMatched` in which the characters
of `[U(1)]` come from two families `a`, `b` indexed by finite types: `a` on the pairs `(U₁, A)` and
`(A', U₂)`, `b` on `(U₂, A)` and `(A', U₁)`, with `a i p * b i q = rankTwist (ν i)⁻¹ (n₁ ⊕ n₂)`
whenever `card p + card q = card n₁ + card n₂`; here `rankTwist α N = α * upsilonU1 ^ (card N / 2)`,
with `upsilonU1` the restriction to `[U(1)]` of the fixed splitting character. A type of forms is a
function on the real unitary group (`GInf`); `k₁`, `k₂`, `k`, `k'` are pairs of conjugate types on
`U₁`, `U₂`, `A`, `A'`, the edges `h₂`, `h₁'` of the family `b` are taken at `d`, the edges `h₁`,
`h₂'` of the family `a` at `!d`, and the forms in the conclusion have types `k₁ !d`, `k₂ !d`. The
four edges are edge families: the characters of each family have fixed weights, a common tame part,
and the theta integral with the Fock vector of the given polynomial lifts forms of the type at that
edge's index (`d` or `!d`) to forms of the type at the same index. The number `N` of negative signs
of `W = U₁ ⊕ U₂` is that of `A` and `A'` together, the rank of `A` is that of `A'` plus `2 t`,
`2 N + 2 ≤ card (n₁ ⊕ n₂) ≤ 2 μ τ + 2 N` at every infinite place `τ`, and `ν i` is tame of weight
`μ` for the modulus `𝔪 i`: it has weight `μ` at infinity, and its tame part is ramified exactly at
the primes of `𝔪 i` and defines the character `χ i` of the residue ring.

Send a form `f` from `U₁` to `U₂` through `A` (`Θ i x`: lift, then transposed lift) or through `A'`
(`Θ' i y`: transposed lift, then lift), the data modulo `𝔪 i` being the indicator functions of the
blocks of `x` or `y`. There are `C` and `κ`, and for each `i` some `c ≠ 0` with
`‖c‖ ^ 2 = C * lValueProd (𝔪 i).places (ν i) t`, such that for every functional `l` the functions
`L x = l (Θ i x f)` and `L' y = l (Θ' i y f)` satisfy `New.Exchange.SquareLaw` with constant
`κ / c`: both transform by `χ i ∘ det`, and `∑ Ψ' L' = (κ / c) ∑ Ψ L` for all matched `Ψ`, `Ψ'`. 
