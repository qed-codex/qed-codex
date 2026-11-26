---
{
  "module": "src/Lib/Shimura/HeckeTower/HeckeData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/HeckeTower/HeckeData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/HeckeTower/HeckeData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke elements in group rings, marked triples, local terms and neat levels

Hecke operators for a group `G` with a subgroup `K` are realised inside the group ring `k[G]`, so
they act on every representation of `G` without convolution. With this, the file sets up the data
for counting fixed points of Hecke correspondences for a CM field `E` over K₀ = ℚ(√-d₀). A rigidity
result for frames then shows that the objects counted have no automorphisms at deep level: levels
inside a large place are neat.

## Main definitions and results

* `New.Variety.fixedToEigen`: the elements that send `K`-fixed vectors to eigenvectors of a
  subgroup, in every representation.
* `New.Variety.MarkedTriple`, `New.Variety.countTerm`: triples (coset, rational matrix, mark) and
  the term that an orbit of triples contributes; `New.Variety.IsRegularHecke`: only separable
  matrices contribute.
* `New.Variety.IsSafe`, `New.Variety.invHeckeIsogeny`, `New.Variety.heckeSum`: the safe split places
  and the Hecke elements that appear in the congruence relation.
* `New.Variety.localTerm`: the local term of a fixed point, a polynomial whose coefficients are
  built from the roots of the characteristic polynomial.
* `New.Variety.IsSignedFrameFor.similitude_and_root_norm`: an automorphism scales the form, and its
  eigenvalues have equal moduli.
* `New.Variety.IsSignedFrameFor.eq_one_of_congr_large_norm`: if such an automorphism is congruent to
  `1` modulo an ideal of large norm, it is `1`.
* `New.Variety.eventually_isNeat`: hence levels inside a large place are neat.

Notions from other files:
* `New.levelSpace`: For a representation π of G, a subgroup K and a character χ of K, the submodule
  of vectors v with π(k)v = χ(k)v for all k in K; for χ = 1, the K-fixed vectors.
* `New.ofSplitPlace`: For a split place w, the homomorphism sending g in GL_n(E_w) to the unitary
  finite adelic matrix with component g at w and 1 off w, w̄.
* `New.Variety.GU`: The unitary similitudes: the frames of the scalar forms `c • 1`, `c > 0`
  rational. `New.Variety.GUPlus`: those whose inverse has integral entries.
* `New.Gf`: The finite adelic unitary group G_f: matrices g in GL_n(𝔸_f) with gᴴg = 1;
  `New.stdLevel` is its subgroup of integral points, `New.stdSpace E n` the definite space with form
  `1`.
* `New.basicCosetRep U`: for a subspace U of k_wⁿ of dimension r (k_w the residue field at w), a
  chosen g in GL_n(E_w) with g and ϖg⁻¹ integral, det g of valuation r, and U the kernel of the
  reduction of g.
* `New.levelOf w H`: the elements of `New.stdLevel` whose reductions modulo the places `w i` lie in
  `H`; `New.classAut Γ K g`: the stabiliser Γ ∩ gKg⁻¹ of the coset gK.

## Relation to the literature

Known; see `Lib.Shimura.HeckeTower.Model`, `Lib.Shimura.IntegralModel.TowerExistence` and
`Lib.Shimura.Uniformisation.AppellHumbert` for sources.



## The Hecke algebra inside the group ring, acting on fixed vectors

* `New.Variety.cosetFn`: the map `k[G] → k[G / K]`, `[g] ↦ [gK]`.


### `spanOn`

 The submodule of the group ring k[G] spanned by the basis elements [g] for g in D. 

### `cosetFn`

 The linear map `k[G] → k[G / K]` sending `∑ a_g [g]` to `∑ a_g [gK]`. It is written as the
action of the group ring element on the basis vector of the trivial coset. 

### `fixedToEigen`

 The submodule of elements `a` of k[G] with the following property: for every representation π of
G, `a` sends the K-fixed vectors to vectors on which the subgroup J of H acts through π∘ι by the
character χ. By default J = ι⁻¹(K) and χ is trivial. 

### `Model.cosetSum`

 For ψ from G/K to a k-module W, the linear map sending a = ∑ a_g [g] in k[G] to ∑ a_g ψ(gK). 

### `single_one_mem_levelSpace`

 The basis vector of the trivial coset in k[G / K] is fixed by K. 

### `spanOn.exists_mem_of_cosetFn_ne_zero`

 If `a` is supported on `D`, its image in `k[G / K]` is supported on the cosets of elements of
`D`. 

### `spanOn.mul`

 If `a` is supported on `D`, `b` on `D'`, and `D * D' ⊆ D''`, then `a * b` is supported on
`D''`. 


## Marked triples, safe places and Hecke elements in the fixed point count

`Φ v` is the embedding chosen by the CM type at the infinite place `v`, and `v₀` is the one place at
which the hermitian forms may be indefinite. `New.Variety.IsSignedFrame x J` says that the adelic
matrix `x` is a frame for a rational form β that is positive definite off `v₀`, with β J positive
definite at `v₀`. `New.Variety.toFinGL` embeds rational matrices in adelic ones.


### `New.GaloisRep.IsSplitPrimeToDisc`

 The prime u of ℚ(√−d) contains an element x = (1 + √−d)/2 − b, b ∈ ℤ, that is coprime to its
conjugate x̄; here `QuadField.betaK d` is (1 + √−d)/2. 

### `New.GaloisRep.IsSplitPrimeToDisc.isSplit_and_prime_q`

 Let the place w of ℚ(√−d) satisfy `New.GaloisRep.IsSplitPrimeToDisc`. Then w̄ ≠ w, the order
`w.q` of the residue field of w is prime, and the places of ℚ(√−d) that contain `w.q` are exactly
w and w̄. 

### `New.GaloisRep.IsSplitPrimeToDisc.isSplit`

 A place satisfying `New.GaloisRep.IsSplitPrimeToDisc` differs from its conjugate. 

### `New.GaloisRep.IsSplitPrimeToDisc.prime_q`

 The order `w.q` of the residue field of a place satisfying
`New.GaloisRep.IsSplitPrimeToDisc` is prime. 

### `New.GaloisRep.IsSplitPrimeToDisc.q_mem_asIdeal_iff`

 If `w` satisfies `New.GaloisRep.IsSplitPrimeToDisc`, the places that contain `w.q` are `w` and
its conjugate. 

### `New.HasQuadSubfield`

 The number d is 3 mod 4, and the field E is an algebra over the imaginary quadratic field
ℚ(i√d). 

### `SplitFinPlace`

 The finite places w of E with w̄ ≠ w, that is, those split over the maximal real subfield. 

### `nonempty_embedding_complex`

 A finite type embeds in ℂ. 

### `numberedRoots`

 A chosen injection `n ↪ ℂ` that lists the roots of `t(P)` when these, counted with
multiplicity, are `|n|` distinct numbers (`roots_map_eq_map_numberedRoots`). Otherwise it is an
arbitrary injection. 

### `roots_map_eq_map_numberedRoots`

 If some injection `n ↪ ℂ` lists the roots of `t(P)`, then `numberedRoots t P` does. 

### `eigenReflection`

 The matrix that describes the signature at `v₀`, written as a polynomial in `Φ v₀ (y)`. The
proposition `ε` chooses the case. In the marked case (`ε` holds) it is `markedReflection y i`. In
the definite case (`ε` fails) it is the identity. See `eigenReflection_eq_ite`. 

### `markedReflection`

 The marked case of `eigenReflection`: the matrix `Q(Φ v₀ (y))`, where `Q` is the Lagrange
polynomial with value `1` at the `i`-th listed root of the characteristic polynomial of `y` and
`-1` at the others (`markedReflection_eq_aeval`). If the roots are distinct, it is `1` on the
`i`-th eigenline and `-1` on the other eigenlines. 

### `eigenReflection_eq_ite`

 The matrix `eigenReflection ε y i` is `markedReflection y i` if ε holds and `1` otherwise. 

### `MarkedTriple`

 Triples (xK, y, z): a coset of `K` in GL_n of the finite adeles, an element `y` of GL_n(E), and
a mark `z : Z`. In `New.Variety.countTerm` the type of marks is `Z = n`, the index of an eigenvalue
of `y`; the default is `Z = ℂ`. GL_n(E) acts by left multiplication on the coset, by
conjugation on `y`, and trivially on the mark. 

### `invAutInFrame`

 For y in GL_n(E) and x in GL_n of the finite adeles of E, the element x⁻¹y⁻¹x of that adelic
group, with y embedded diagonally. 

 ### Split places and the Hecke elements of the congruence relation 

### `conjAtSplit`

 For a split place v, the homomorphism sending g in GL_n(E_v) to the adelic matrix that is
g⁻ᵀ at v, the conjugate of g at v̄, and 1 elsewhere. 

### `dualComponent`

 For a split place v, the homomorphism sending an adelic matrix to the inverse transpose of
its component at v, in GL_n(E_v); a left inverse of `New.Variety.conjAtSplit` at v. 

### `IsCuspidalType`

 Cuspidality of χ: for every idempotent matrix ε ≠ 0, 1, χ is non-trivial on the elements of
J lying in the unipotent group 1 + εM_n(1 − ε). 

### `uniformizerNorm`

 The norm from E to K₀ of the finite idele that is the chosen uniformiser at v and 1
elsewhere. 

### `centralScalar`

 The homomorphism sending a finite idele x of K₀ to the scalar matrix x̄·1 in GL_n of the
finite adeles of E. 

### `IsSafe`

 Safe places w of E: the place u of ℚ(√−d₀) below w satisfies `New.GaloisRep.IsSplitPrimeToDisc`,
and 𝔑 lies neither in w nor in any place above ū. 

### `SafePlace`

 The split places of E that are safe for K₀ and the level 𝔑, in the sense of
`New.Variety.IsSafe`. 

### `IsSafe.isSplitPrimeToDisc_below`

 A safe place lies over a place of K₀ that satisfies `New.GaloisRep.IsSplitPrimeToDisc`. 

### `IsSafe.level_notMem_asIdeal`

 If `w` is safe for 𝔑, then 𝔑 is prime to `w`. 

### `IsSafe.level_notMem_asIdeal_of_below_eq_star`

 If `w` is safe for 𝔑, then 𝔑 is prime to every place `v` above the conjugate of the place of
K₀ below `w`. 

### `invHeckeIsogeny`

 For a subspace U of k_vⁿ (k_v the residue field) of dimension r, the scalar matrix of the
conjugate of the (-r)-th power of `New.Variety.uniformizerNorm` at v, times
`New.Variety.conjAtSplit` of the transpose of `New.basicCosetRep` U. 

### `levelGU`

 The principal level: the similitudes in `GL_n(Ô E)` that are congruent to `1` modulo `𝔑`. 

### `heckeSum`

 The element τ_{v,j} of the group ring over k: the sum of the elements
`New.Variety.invHeckeIsogeny` over all j-dimensional subspaces U of k_vⁿ. 

### `heckeAlgebra`

 The Hecke algebra of level K = `New.Variety.levelGU` for 𝔑. It is the subalgebra of elements
∑ a_g [g] of k[GL_n(𝔸_f)] that are supported on `GUPlus E n` and whose function ∑ a_g 1_{gK} is
left K-invariant. 

### `levelGU_le_GU`

 The principal level consists of similitudes. 

### `heckeAlgebra.val_mem_spanOn`

 An element of the Hecke algebra is supported on `GUPlus E n`. 

### `heckeAlgebra.val_mem_fixedToEigen`

 An element of the Hecke algebra sends the vectors fixed by `levelGU n 𝔑` to vectors fixed by
it, in every representation. 

### `heckeCosetFn`

 For an element f = ∑ a_g [g] of the Hecke algebra of level 𝔑, the function ∑ a_g 1_{gK} on
cosets of the principal level subgroup K. 

### `countTerm`

 The term of a `GL n E`-orbit of triples, read at a chosen representative `(q, y, μ)` of the
orbit and a chosen representative `x` of the coset `q`. It is `f(x⁻¹ y⁻¹ x K) * ω(charpoly y, μ)`
if `x` is a signed frame for `eigenReflection ε y μ`, and `0` otherwise. So `ε = True` gives
the marked count and `ε = False` the definite count. The value does not depend on the two choices;
see `New.Variety.countTerm_mk` in `Lib.Shimura.Transfer.MarkedPairs`. 

### `IsRegularHecke`

 Regularity of f: whenever f(x⁻¹y⁻¹x) ≠ 0 with y in GL_n(E) and x adelic, the characteristic
polynomial of y is separable. 

### `IsLieRoot`

 For μ : ℂ, the eigenline of the root r at the embedding t : E →+* ℂ lies in the Lie algebra: if
t = Φ v₀, then r = μ; if t is the other embedding above v₀, then r ≠ μ̄; if t lies above a place
v ≠ v₀, then t = Φ v. 

 ### The local term 

### `lieRoots`

 For an embedding `σ : E →+* ℂ`, the roots `r` of σ(P), as polynomials: `r X` if the eigenline of
`r` lies in the Lie algebra, the constant `r` otherwise. It is `r X` exactly in these cases:
* σ = Φ v₀: only `r = μ`;
* σ the other embedding above `v₀`: all `r` other than the conjugate of `μ`;
* σ above a place `v ≠ v₀`: all `r` if σ = Φ v, none otherwise. 

### `localTerm`

 For P : E[X] and α : Fin ν → 𝓞 E, with μ the `j`-th listed root of the image of P under Φ v₀:
the polynomial L(μX), with L the Lagrange basis polynomial that is 1 at μ and 0 at the other listed
roots, times ∏ (1 − σ(α i) η), over all i, all embeddings σ and all η in `New.Variety.lieRoots` at
σ. 


## Rigidity of frames, neat levels and free action

Rigidity of frames, used to show that the objects counted have no automorphisms at deep level. A
matrix `x` over the finite adeles of the CM field `E` is a frame for the form `β`
(`New.Variety.IsFrameFor`) if `xᴴ β x` is the scalar matrix of a unit of `Ô ℚ`.
`New.Variety.IsSignedFrameFor x ℓ β` adds that `β` is positive definite at the infinite places other
than the base place `v₀`, and `β * ℓ` is so at `v₀`. `New.Variety.ratConj y ℓ` is `ℓ` conjugated by
the image of `y` under `Φ v₀`.


### `instance [h : HasPrimitiveRoot5040 E] : Nontrivial (InfinitePlace E)`

 A CM field that contains a primitive `5040`-th root of unity has degree at least `3` over `ℚ`,
hence at least two infinite places. 

### `exists_isScalarFrame_of_gram_eq`

 If `xᴴ x` is the scalar matrix of a finite idele `a` of `ℚ`, then the idele norm
`finIdeleAbs a` is a rational number `c`, and `x` is a frame for the positive scalar form `c • 1`.


### `mem_GU_of_gram_eq`

 A matrix `x` with `xᴴ x` the scalar matrix of a finite idele of `ℚ` is a similitude. 

### `isScalarFrame_of_gram_eq`

 If `xᴴ x` is the scalar matrix of a finite idele `a` of `ℚ` and the rational `c` is the idele
norm `finIdeleAbs a`, then `x` is a frame for the positive scalar form `c • 1`. 

 ### Frames and their multipliers 

### `mem_GUPlus_of_mem_levelGU`

 An element of the principal level is a similitude whose inverse has integral entries. 

### `IsFrameFor.isHermitian_map`

 If `x` is a frame for the form `β`, the image of `β` under every complex embedding is
hermitian. 

### `isSignedFrameFor_one`

 A point `g` of the finite adelic unitary group `Gf E n` (so `gᴴ g = 1`) is a signed frame for
the identity form, with `ℓ = 1` at the base place. 

### `IsFrameFor.exists_intCast_eq`

 If `x` is a similitude whose inverse has integral entries (`x ∈ GUPlus E n`) and `x` is a frame
for the scalar form `c • 1`, then the rational number `c` is an integer. 

### `IsScalarFrame.eq_one_of_mem_levelGU`

 If `x` lies in the principal level `levelGU n 𝔑` and `x⁻¹` is a frame for the positive scalar
form `c • 1`, then `c = 1`. 

### `levelGU.isScalarFrame_inv_one`

 The inverse of an element of the principal level is a frame for the identity form. 

 ### Uniqueness of the form, and automorphisms 

### `IsFrameFor.unique`

 A frame determines its form: let `x` in GL_n of the finite adeles of the CM field `E` be a frame
for both `β` and `β'` (`IsFrameFor`: xᴴβx = ε • 1 and xᴴβ'x = δ • 1 for units ε and δ of Ẑ). If
both forms are positive definite at the infinite place `w` (mapped to `ℂ` by the chosen embedding
`Φ w`), then `β' = β`. 

### `IsSignedFrameFor.conjTranspose_mul_mul_eq_smul`

 Let `E` have a base place `v₀` (`CMBase`, so at least two infinite places), let `(x, ℓ, β)` and
`(x', ℓ', β')` be signed frames (`IsSignedFrameFor`), and let `y ∈ GL_n(E)`. If `(x'⁻¹ y x)⁻¹` is a
frame for the scalar form `c • 1` with `c > 0` rational, then `yᴴ β' y = c β`. 

### `IsSignedFrameFor.similitude_and_root_norm`

 Let `(x, ℓ, β)` be a signed frame (`IsSignedFrameFor`) and let `y ∈ GL_n(E)` fix `ℓ` under
`ratConj`, with `(x⁻¹ y x)⁻¹` a frame for the scalar form `c • 1`; so `y` is an automorphism of the
object given by `x`. Then `y` is a similitude of `β` with multiplier `c` (`yᴴ β y = c β`), and each
root `r` of the characteristic polynomial of `y` mapped by `Φ w`, at each infinite place `w`, has
`r * star r = c`. 

### `exists_eq_trace_sub_one_mem_of_mem_congruenceGL`

 If `x⁻¹ y x` is congruent to `1` modulo the ideal `J` of `Ô E`, and `J` meets `𝓞 E` inside the
ideal `I`, then the trace of `y - 1` is an algebraic integer `t` that lies in `I`. 

### `norm_trace_sub_one_le_of_mul_star_eq_one`

 If every complex eigenvalue `r` of `y` at the infinite place `v` has `r * star r = 1`, then the
image of the trace of `y - 1` under `Φ v` has modulus at most `2 * card n`. 

### `abs_norm_le_pow_finrank_of_forall_norm_le`

 An algebraic integer `t` of `E` whose images under all the embeddings `Φ v` have modulus at
most `B` has norm at most `B ^ [E : ℚ]` in absolute value. 

### `trace_eq_card_of_mem_congruenceGL`

 Let `x⁻¹ y x` be congruent to `1` modulo the ideal `J` of `Ô E`, where `J` meets `𝓞 E` inside an
ideal `I` of norm above `(2 * card n) ^ [E : ℚ]`. If the images of the trace of `y - 1` under all
the embeddings `Φ v` have modulus at most `2 * card n`, then the trace of `y` is `card n`. 

### `eq_one_of_conjTranspose_mul_mul_eq_of_trace_eq`

 Let `β` be positive definite at the infinite place `w`. If `y` preserves `β` (`yᴴ β y = β`) and
the trace of `y` is `card n`, then `y = 1`: the positive definite form `A ↦ tr (β⁻¹ Aᴴ β A)` at
`w` takes the value `n - n - n + n = 0` at `A = y - 1`. 

### `IsSignedFrameFor.eq_one_of_congr_large_norm`

 Let `(x, ℓ, β)` be a signed frame, let `y ∈ GL_n(E)` fix `ℓ` under `ratConj`, and let
`(x⁻¹ y x)⁻¹` be a frame for the identity form (so `y` is an automorphism of the object given by
`x`). If `x⁻¹ y x` is congruent to `1` modulo an ideal `J` of `Ô E`, and `J` meets `𝓞 E`
inside an ideal `I` of norm above `(2 * card n) ^ [E : ℚ]`, then `y = 1`. 

 ### Neat levels and freeness 

### `IsNeat`

 The level 𝔑 is neat: 𝔑 ≠ 0 and, whenever `x` is a signed frame with `ℓ` for some form
(`New.Variety.IsSignedFrame`), every y in GL_n(E) with x⁻¹yx in `levelGU n 𝔑` that fixes ℓ under
`New.Variety.ratConj` equals 1. 

### `IsNeat.eq_one_of_mem_levelGU`

 On a neat level automorphisms are trivial: if `x` is a signed frame with `ℓ`, and `y ∈ GL_n(E)`
has `x⁻¹ y x` in `levelGU n 𝔑` and fixes `ℓ` under `ratConj`, then `y = 1`. 

### `eventually_isNeat`

 Let `E` have a base place (`CMBase`, so at least two infinite places) and let `n` be nonempty.
For all but finitely many finite places `w` of `E`, every nonzero `𝔑 : 𝓞 E` that lies in `w` is a
neat level (`IsNeat n 𝔑`). 

### `eq_one_of_reduceAt_eq_one`

 Freeness for the definite space `stdSpace E n`: let `E` be a CM field with at least two infinite
places, and let the `w i` be distinct finite places whose norms have product above
`(2 * card n) ^ [E : ℚ]`. Let `γ` be a rational unitary element and `g` lie in G_f. If the conjugate
`g⁻¹ γ g` (with γ embedded in G_f) lies in the integral level `stdLevel E n`, which is
G_f ∩ GL_n(Ô E) (hypothesis `hk`), and reduces to `1` modulo every `w i`, then `γ = 1`. 

### `classAut_eq_bot`

 Let `E` be a CM field with at least two infinite places. Let the `w i` be distinct finite places
whose norms have product above `(2 * card n) ^ [E : ℚ]`. Let `K` be a subgroup of the finite adelic
unitary group `Gf E n` whose elements are integral and reduce to `1` modulo every `w i`. Then for
`g` in `Gf E n`, the stabiliser of the coset `g K` is trivial. The stabiliser is taken in the
unitary group over `E` of the definite form `stdSpace E n` (identity matrix, sum of norms of
coordinates), embedded in `Gf E n`. A case of Minkowski's lemma on integral matrices of finite
order. 
