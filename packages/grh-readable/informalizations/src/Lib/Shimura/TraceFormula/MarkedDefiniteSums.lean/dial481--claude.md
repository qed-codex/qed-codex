---
{
  "module": "src/Lib/Shimura/TraceFormula/MarkedDefiniteSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/MarkedDefiniteSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/MarkedDefiniteSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# For a function with a cuspidal type at one place, marked and definite orbit sums agree

* `New.Variety.finsum_orbits_eq_zero_of_free_of_blocks`: a sum over orbits vanishes if it vanishes
  on each block of a partition that the group permutes, with finite support there, and the
  stabiliser of each point where it is non-zero is trivial.
* `New.Variety.finsum_markedTerm_eq_finsum_definiteTerm`: the marked and the definite sums agree for
  every weight; `New.Variety.finsum_countTerm_marked_eq_definite` says this in terms of `countTerm`.

Idea: both sums run over the classes of triples `(xK, y, μ)` under `GL n E`. Classes with
irreducible characteristic polynomial are matched by a change of signs. For a reducible one, an
idempotent at the split place gives a unipotent group, whose orbits cut the triples into blocks;
translation along it multiplies the terms by a value of the character that is not 1, so they sum to
zero on each block.

Notions from other files:
* `New.Variety.MarkedTriple`: triples `(xK, y, μ)` of an adelic coset, an element `y` of `GL n E`
  and an index `μ` of an eigenvalue of `y`.
* `New.Variety.countTerm`: the term `f(x⁻¹ y⁻¹ x K) * u(charpoly y, μ)` of the class of
  `(xK, y, μ)` if `IsSignedFrame x (eigenReflection ε y μ)` holds (the sign condition), else `0`;
  `ε = True` gives the marked count and `ε = False` the definite count.
* `New.Variety.conjAtSplit`: places an element of `GL n` over the completion at a split place `w₀`
  in the adelic similitude group; `New.Variety.dualComponent` is a left inverse.
* `New.Variety.IsRegularHecke`: `f(x⁻¹ y⁻¹ x K) ≠ 0` forces the characteristic polynomial of `y` to
  be separable.
* `New.Variety.IsCuspidalType`: for every idempotent matrix `e ≠ 0, 1`, the character `χ` is
  non-trivial on the elements of `J` in the unipotent group `1 + e M_n (1 - e)`.

## Relation to the literature

Known result: Simple trace formula on a definite group, with vanishing non-elliptic terms. This
file proves the comparison of orbit sums that is used, for unitary similitudes at a neat level, with
Haar integrals replaced by finite sums over cosets. The non-elliptic terms cancel for a regular test
function with a cuspidal type at one split place; the elliptic terms match for n odd.
Source: Dummigan, A simple trace formula for algebraic modular forms, Exp. Math. 22 (2013); Arthur
and Clozel, Simple algebras, base change and the advanced theory of the trace formula (1989), ch. 1
§2, after Deligne and Kazhdan.


 ### Sums over blocks and cosets 

### `card_block_inter_orbit`

 Let `Γ` permute the blocks `π p` of a partition of `X`. If the stabiliser of `p` is trivial,
the points of its block that lie in its orbit are as many as the elements of the stabiliser of
the block. 

### `mem_image_block_iff`

 Let `Γ` permute the blocks `π p` of a partition of `X`. An orbit `a` meets the block of `s` if
and only if the block of the chosen point of `a` is a translate of the block of `s`. 

### `finsum_orbits_eq_zero_of_free_of_blocks`

 Let `Γ` permute the blocks `π p` of a partition of `X`, and let `F` be a function on the orbits.
Suppose that at every point where `F` is not zero the stabiliser is trivial, and that the block of
such a point has finite intersection with the support of `F` and sum zero. Then the sum of `F` over
the orbits is zero. 

### `finsum_orbits_eq_zero_of_blocks`

 The form of `finsum_orbits_eq_zero_of_free_of_blocks` with one hypothesis `h_cancel`: at a point
where `F` is not zero the stabiliser is trivial, and `F` has finite support and sum zero on the
block. 

### `finsum_mem_range_eq_zero_of_translate`

 Let the fibres of `r` be the cosets of `L`. If translation by `a` multiplies `F ∘ r` by a
constant other than `1`, the sum of `F` over the image of `r` is zero. 

### `finite_range_inter_support`

 Let the fibres of `r` be the cosets of an open subgroup `L`. If every point of the image of `r`
where `F` is not zero comes from a compact set `C`, there are finitely many such points. 

 ### An idempotent that is a polynomial in the element, and its radical 

### `exists_idempotent_mod`

 Every polynomial `P` over a field has an idempotent `p` modulo `P` such that, if `P` is
separable, not irreducible and not a unit, neither `p` nor `1 - p` is coprime to `P`. 

### `splittingPoly`

 A fixed choice of the idempotent modulo `P` of `exists_idempotent_mod`. 

### `splittingIdempotent`

 The idempotent `p(g)`, where `p` is the chosen idempotent modulo the characteristic polynomial
of `g`. 

### `isIdempotentElem_splittingIdempotent`

 The matrix `splittingIdempotent g = p(g)` is idempotent, by the Cayley-Hamilton theorem. 

### `splittingIdempotent_ne_zero_and_ne_one`

 If the characteristic polynomial of `g` is separable and not irreducible, the idempotent
`splittingIdempotent g` is neither `0` nor `1`. 

### `splittingIdempotent_conj`

 Conjugating `g` conjugates its idempotent. 

### `splittingRadical`

 The parametrisation `Y ↦ 1 + e Y (1 - e)` of the unipotent radical attached to the idempotent
`e = splittingIdempotent g`. Its range is called the radical of `g`. 

### `mem_range_splittingRadical_conj`

 Conjugating `g` conjugates its radical: if `a` lies in the radical of `g`, then `b⁻¹ a b` lies
in the radical of `b⁻¹ g b`. 

### `splittingRadical_aeval_conj`

 An element `a` of the radical of `g` is recovered from the conjugate `a⁻¹ g a`: its parameter
can be taken to be `p(a⁻¹ g a)`, for the polynomial `p` that gives the idempotent of `g`. 

### `exists_splittingRadical_conj`

 A translate `j g` of `g` by an element `j` of its radical is conjugate to `g` under the
radical. 

### `range_splittingRadical_conj_self`

 Conjugating `g` by an element `b` of its radical does not change the radical, as this group is
commutative. 

### `IsCuspidalType.exists_mem_range_splittingRadical`

 If the characteristic polynomial of `g` is separable and reducible, a cuspidal type `(J, χ)`
has an element `j` in the radical of `g` with `χ j ≠ 1`. 

 ### The blocks of triples 

### `markedTriple`

 The triple `(xK, y, μ)`. 

### `markedTriple_out`

 A triple `p = (q, y, μ)` is the triple of the chosen representative of its coset `q`. 

### `markedTriple_eq_iff`

 The triples `(xK, y, μ)` and `(x'K, y', μ)` are equal if and only if `xK = x'K` and `y = y'`. 

### `smul_markedTriple`

 An element `z` of `GL n E` sends `(xK, y, μ)` to `(z x K, z y z⁻¹, μ)`. 

### `invAutInFrame_mul`

 Moving the frame `x` to `x k` conjugates `invAutInFrame y x = x⁻¹ y⁻¹ x` by `k`. 

### `invAutInFrame_conj`

 The element `invAutInFrame y x = x⁻¹ y⁻¹ x` does not change under `(y, x) ↦ (z y z⁻¹, z x)`. 

### `localAut`

 The automorphism `y` in the frame `x` at the split place `w₀`: the inverse transpose of the
component of `x⁻¹ y⁻¹ x` at `w₀`. 

### `localAut_mul`

 Moving the frame `x` to `x k` conjugates `localAut w₀ y x` by the inverse transpose of the
component of `k` at `w₀`. 

### `localAut_mul_conjAtSplit`

 Moving the frame `x` by an element `a` placed at `w₀` conjugates `localAut w₀ y x` by `a`. 

### `coe_dualComponent`

 The matrix of `dualComponent w₀ a` is the transpose of the component of `a⁻¹` at `w₀`. 

### `charpoly_localAut`

 The characteristic polynomial of `localAut w₀ y x` is that of `y`, read in the completion of
`E` at `w₀`. 

### `tripleBlock`

 The block of `(xK, y, μ)`: the triples `(x a K, y, μ)`, where `a` runs over the radical of
`localAut w₀ y x`, placed at `w₀`. 

### `mem_tripleBlock`

 The points of the block of `(xK, y, μ)` are the triples `(x a K, y, μ)` with `a` in the radical
of `localAut w₀ y x`. 

### `tripleBlock_mul_of_mem`

 If `K` consists of unitary similitudes, the block of `(xK, y, μ)` does not depend on the
representative `x` of the coset `xK`. 

### `tripleBlock_mul_conjAtSplit`

 All points of a block have the same block: for `b` in the radical of `localAut w₀ y x`, the
triples `(x b K, y, μ)` and `(xK, y, μ)` have the same block. 

### `smul_tripleBlock`

 An element `z` of `GL n E` carries the block of `(xK, y, μ)` to the block of
`(z x K, z y z⁻¹, μ)`. 

### `blockOf`

 The block of a triple `p = (q, y, μ)`, read at the chosen representative of the coset `q`. 

### `blockOf_markedTriple`

 If `K` consists of unitary similitudes, the block of `(xK, y, μ)` can be read at `x`. 

### `blockOf_smul`

 If `K` consists of unitary similitudes, then for `p` in the block of `q` the block of `z • p` is
the translate by `z` of the block of `q`. 

 ### The classes with reducible polynomial 

### `stabilizer_markedTriple`

 If the level `𝔑` is neat (it is non-zero, and an automorphism of a signed frame that lies in the
level is trivial), a triple `(xK, y, μ)` with `K = levelGU n 𝔑` whose frame `x` satisfies the sign
condition `h_sign` has trivial stabiliser in `GL n E`. 

### `heckeCosetFn_conjAtSplit_mul`

 Let the Hecke function `f` have type `(J, χ)` at `w₀`: it sends vectors of level `𝔑` to
`χ`-eigenvectors of `J`. Then left translation by `j ∈ J`, placed at `w₀`, multiplies the function
`heckeCosetFn f` on cosets of the level by `χ j⁻¹`. 

### `dualComponent_mem_matrix`

 If the Hecke function `f` is not zero on the coset of `t`, the inverse transpose of the
component of `t` at `w₀` is an integral matrix. 

### `countTerm_mul_conjAtSplit`

 Moving a frame `x` that satisfies the sign condition by an element `a` at `w₀` keeps the sign
condition and the weight, so the term of `(x a K, y, μ)` is the value of `f` times the weight. 

### `invAutInFrame_mul_conjAtSplit`

 Let `x⁻¹ y⁻¹ x` be a unitary similitude. Moving the frame `x` by an element `a` at `w₀`
conjugates its factor `localAut w₀ y x` at `w₀` by `a` and leaves the rest alone. 

### `blockPoint`

 The point of the block of `(xK, y, μ)` with parameter `Y`, for the principal level
`K = levelGU n 𝔑`. 

### `blockPoint_eq_iff`

 Two parameters `Y`, `Y'` give the same point of the block if and only if the element of the
radical with parameter `Y⁻¹ * Y'`, placed at `w₀`, lies in the level `levelGU n 𝔑`. 

### `finite_tripleBlock_inter_support`

 If `𝔑 ≠ 0` and the frame `x` satisfies the sign condition `h_sign`, then `countTerm ε f u`
(the value of `f` times the weight `u`, at classes with the sign condition) is non-zero at only
finitely many points `(x a K, y, μ)` of the block of `(xK, y, μ)`. Here `K = levelGU n 𝔑` and `a`
runs over the radical `1 + e M_n (1 - e)` of `localAut w₀ y x`, placed at `w₀` by `conjAtSplit w₀`;
`localAut w₀ y x` is the inverse transpose of the component of `x⁻¹ y⁻¹ x` at `w₀`, and `e` is its
chosen idempotent. 

### `finsum_tripleBlock_eq_zero`

 Let `f` have type `(J, χ)` at the split place `w₀` (it turns vectors fixed by the level into
`χ`-eigenvectors of `J`), let the frame `x` satisfy the sign condition and let `x⁻¹ y⁻¹ x` be a
unitary similitude. The block of `(xK, y, μ)` consists of the `(x a K, y, μ)` with `a` in the
radical of `localAut w₀ y x`, placed at `w₀`. If `χ` is not trivial at some `j ∈ J` in this radical,
the sum over the block of `countTerm ε f u` (the value of `f` times the weight `u`) is zero. 

### `finsum_countTerm_eq_zero_of_reducible`

 Let `𝔑` be neat (non-zero, with only trivial automorphisms of signed frames) and let `f` be a
regular Hecke function of level `𝔑` (its terms vanish unless the characteristic polynomial is
separable) with the cuspidal type `(J, χ)` at the split place `w₀` (`f` turns vectors fixed by the
level into `χ`-eigenvectors of `J`, and `χ` is non-trivial on `J` in each proper unipotent
radical). If the weight `u` vanishes on irreducible polynomials, so that only classes with reducible
characteristic polynomial contribute, then `countTerm ε f u` (the value of `f` times `u`, at classes
with the sign condition of `ε`) has sum zero over all classes, for the marked count (`ε` true) and
for the definite count (`ε` false). 

 ### The classes with irreducible polynomial 

### `reflectionSigns`

 The signs of `eigenReflection ε y μ` at the roots of `y`, place by place: `-1` at the place
`v₀` and the roots other than `μ` if `ε` holds, and `1` in all other cases. 

### `reflectionSigns_false`

 In the definite case all signs are `1`. 

### `prod_reflectionSigns`

 In odd rank the marked signs have product one: `-1` occurs `card n - 1` times. 

### `ite_eigenReflection_eq`

 The matrix that enters the sign condition at the infinite place `v` is `p(y)` under the
embedding `Φ v`, where `p` takes the values `reflectionSigns ε μ v` at the numbered roots of the
characteristic polynomial of `y`. 

### `isSignedFrame_iff_hasSignType`

 Let `y` have irreducible characteristic polynomial, and let `x⁻¹ y⁻¹ x` be a frame for the
scalar form `ν • 1`. Then `x` is a signed frame for `eigenReflection ε y μ` (a frame for some
hermitian form with the positivity that this matrix prescribes at `v₀`) if and only if `y` is an
elliptic similitude of multiplier `ν`, with the signs `reflectionSigns ε μ` at its roots, of a form
whose Gram matrix in the frame `x` is `c • 1` for a unit `c` of the integral adeles `Ô ℚ`. 

### `markedTerm`

 The term of the marked count: `countTerm` with the sign condition on the class of
`(xK, y, μ)` taken for the reflection attached to the marked root `μ` of `y`. 

### `definiteTerm`

 The term of the definite count: `countTerm` with the sign condition on the class of
`(xK, y, μ)` taken with all signs `+1`. 

### `finsum_markedTerm_eq_of_irreducible`

 Let the rank be odd and let `f` be a Hecke function of level `𝔑`. If the weight `u` vanishes on
the polynomials that are not irreducible, so that only classes with irreducible characteristic
polynomial contribute, the sum over all classes of `markedTerm f u` (`f` times `u`, with the signs
of the marked root) is that of `definiteTerm f u` (the same with all signs `+1`): a change of signs
of the frame matches the classes. 

 ### The comparison 

### `finsum_markedTerm_eq_finsum_definiteTerm`

 The marked and the definite orbit sums agree. Assume that `𝔑` is neat and the rank is odd; that
`f` is a regular Hecke function of level `levelGU n 𝔑`; that in every representation `f` sends
vectors of that level to `χ`-eigenvectors of `J`, acting through `conjAtSplit` at the split place
`w₀`, where `(J, χ)` is a cuspidal type (`χ` is non-trivial on `J` within each proper unipotent
radical); and that with weight `1` finitely many classes have a non-zero marked term and finitely
many a non-zero definite term. Then for every weight `w` the sums over all classes of the marked and
of the definite terms are equal. 

### `finsum_countTerm_marked_eq_definite`

 The sums of `countTerm ε f w` over all classes agree for `ε = True` (the marked count) and
`ε = False` (the definite count): the level `𝔑` is neat, the rank is odd, `f` is a regular Hecke
function (its terms vanish unless the characteristic polynomial is separable) of cuspidal type
`(J, χ)` at the split place `w₀`, and with weight `1` finitely many classes have a non-zero term.

Known result: the comparison of orbit sums in the simple trace formula on a definite group. 
