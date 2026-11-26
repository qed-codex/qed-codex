---
{
  "module": "src/Lib/PadicComparison/Descent/AlmostDescent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Descent/AlmostDescent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Descent/AlmostDescent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Almost coefficients, v-descent for perfect algebras and acyclicity of tilt points

The tilt O♭ (`New.Period.OFlat`) has maximal ideal 𝔪 (`New.Variety.MaxIdealFlat`) and contains p♭
(`New.Variety.pFlat`); N is an O♭-module killed by p♭. The coefficient functor
`New.Variety.almostCoeff N` sends an O♭-algebra b to b ⊗ N ⊗ 𝔪, a case of
`New.Variety.tensorCoeff`.
For these coefficients, a map of perfect O♭-algebras that is onto on points in tilts of tests is a
cover. By Čech descent, the points of a perfect algebra in tilts are acyclic. Auxiliary results
treat 𝔪² = 𝔪 and Witt vectors of O♭-algebras.

## Main definitions and results

* `New.Variety.isCover_of_points`: if p^♭ kills N, a map b → b' of perfect O^♭-algebras that is onto
  on points with values in tilts of tests is a cover (`New.Variety.IsCover`) for the coefficients
  D ↦ D ⊗ N ⊗ 𝔪.
* `New.Variety.isAcyclicAt_perfectTilt`: for N killed by p♭, the points of a perfect O♭-algebra in
  tilts of tests are acyclic (`New.Variety.IsAcyclicAt`) for the coefficients b ↦ b ⊗ N ⊗ 𝔪. This
  holds on the category of perfect O♭-algebras.
* `New.Variety.isAcyclicOnPerfect_almostCoeff`: the same on all O♭-algebras, for b perfect.

Notions from other files:
* `New.Period.OFlat`: The ring O^♭, the inverse limit of O_C/p along x ↦ x^p, where O_C is the ring
  of integers of C_p.
* `New.Variety.moduleCoeff`, `New.Variety.tensorWith`: A functor Φ to S-modules regarded as
  coefficients for cohomology, and M ⊗_S Φ for an S-module M.
* `New.Variety.pFlat`: The element p^♭ = ξ mod p of O^♭ = A_inf/p, the zeroth Witt coefficient of
  the generator ξ of the kernel of θ.
* `New.Variety.PadicTest`: A non-empty family of cells (`New.Variety.IsCell`) with a ring map from
  O_C = `New.OC` to their product; `TiltRing` is the tilt of the product.

## Relation to the literature

Known result: Almost acyclicity of the structure sheaf for the v-topology. The statement holds for
any perfect algebra over the tilt of O_C, as cohomology on products of complete absolutely
integrally closed valuation rings modulo p♭, with the maximal ideal put into the coefficients so
that the result is exact. The proof passes to a valuation ring. Source: P. Scholze, Étale cohomology
of diamonds, arXiv 1709.07343 (2017), Theorem 8.7, Proposition 8.8; for perfect rings B. Bhatt, P.
Scholze, Projectivity of the Witt vector affine Grassmannian, Invent. Math. 209 (2017), Theorem 4.1;
points argument O. Gabber, S. Kelly, Points in algebraic geometry, J. Pure Appl. Algebra 219 (2015),
Theorem 2.3.



## Almost coefficient functors and idempotence of 𝔪

`New.Variety.MaxIdealFlat.exists_smul_eq` is a sharp form of 𝔪² = 𝔪: every element of 𝔪 is s • k
with k in 𝔪 and s nilpotent modulo a given t ≠ 0.


### `tensorCoeff`

 For an O^♭-module M, the functor B ↦ B ⊗_{O^♭} M from commutative O^♭-algebras to
O^♭-modules. 

### `almostCoeff`

 For an O^♭-module N, the functor b ↦ b ⊗ N ⊗ 𝔪 from commutative O^♭-algebras to O^♭-modules,
𝔪 the maximal ideal of O^♭ and tensor products over O^♭. 

### `MaxIdealFlat.exists_smul_eq`

 For m in the maximal ideal 𝔪 of O^♭ and t ≠ 0 in O^♭, one can write m = s·k with k in 𝔪 and
s in O^♭ such that t divides a power of s. 


## The zeroth Witt coefficient and p-torsion-freeness

An O^♭-algebra b is an algebra over A_inf = W(O^♭) through the zeroth Witt coefficient.


### `wittConstCoeff`

 For an O^♭-algebra b, the A_inf-linear map W(b) → b sending a Witt vector to its zeroth
coefficient. 

### `isSMulRegular_tensor_witt`

 If the A_inf-module 𝒜 has no p-torsion and the O^♭-algebra b is perfect without p♭-torsion
(`New.Variety.IsPerfectTorsionFree`), then 𝒜 ⊗ W(b), over A_inf, has no p-torsion. 


## v-descent for almost coefficients

* Suppose a relative class z with coefficients E ⊗ D ⊗ N ⊗ 𝔪 is nonzero, of least degree. It is
  pushed along maps E → E' (`New.Variety.tensorPush`) and stays nonzero up to a valuation ring V
  (`New.Variety.exists_maximal_tensorPush_ne_zero`,
  `New.Variety.exists_perfect_valuationRing_factor`);
* `New.Variety.exists_faithfullyFlat_padicTest`, `New.Variety.tensorPush_quotient_ne_zero`: to a
  quotient of V over which the tilt of a test is faithfully flat;
* `New.Variety.faithfullyFlat_descent`: there it vanishes, as this point of b lifts to b'.

`New.Variety.PerfectAlg` S is the category of perfect S-algebras, `New.Variety.H` K F n is Ext^n(K,
F) for functors to abelian groups, and `New.Variety.relFreeAb` U = ℤ[Y]/ℤ[U], for a subfunctor U of
Y, gives relative cohomology. For an object X, h_X = Hom(X, −).


 ### Two facts of commutative algebra over O^♭ 

### `MaxIdealTensor.isTorsionFree_of_isReduced`

 For a reduced commutative O^♭-algebra S, the O^♭-module 𝔪 ⊗_{O^♭} S is torsion-free, where
𝔪 is the maximal ideal of O^♭. 

### `exists_faithfullyFlat_padicTest`

 Let V be a perfect O^♭-algebra that is a valuation domain, in which p^♭ is neither zero nor a
unit. Then there are a p-adic test c and an O^♭-algebra map φ from V to the tilt `c.TiltRing` of c
such that the induced map V / ker φ → `c.TiltRing` is faithfully flat and p^♭ divides every element
of the kernel of φ. Here a p-adic test is a non-empty family of cells together with a ring map from
O_C to their product. 

### `tensorPush`

 For a functor Φ from C to S-modules, a functor K from C to abelian groups and a degree n: the
additive map that sends an S-linear map f: M → M' to the induced homomorphism
H^n(K, M ⊗_S Φ) → H^n(K, M' ⊗_S Φ). 

### `coeffMap_comp`

 The coefficient map of a composite of natural maps is the composite of the coefficient maps. 

### `tensorCoeffMap`

 For a functor Φ to S-modules, the natural map M ⊗ Φ → M' ⊗ Φ induced by an S-linear map
f: M → M'. 

### `tensorPush_apply`

 `tensorPush f` is the push-forward along the map of coefficients M ⊗ Φ → M' ⊗ Φ induced by f. 

### `eq_of_tensorPush_eq`

 Let M → M' → M'' → 0 be exact via f, g, with f ⊗ Φ(A) injective for every object A of C. If
H^m(K, M'' ⊗ Φ) = 0 for all m < n, then classes z and y in H^n(K, M ⊗ Φ) with the same image under
`tensorPush f` are equal. 

### `exists_repr_cech`

 Let S be an O^♭-algebra and φ: b → d a map of perfect S-algebras. On perfect S-algebras, the
(m+1)-fold fibre power of h_d over h_b (`New.Variety.cech`) is representable: there are a perfect
S-algebra D and a point z of the fibre power at D such that, for every A, the map h_D(A) → fibre
power at A induced by z is bijective. 

### `relFreeAbOfHom`

 For a map φ: b → d of perfect S-algebras, the functor D ↦ ℤ[Hom(b,D)]/ℤ[maps that factor
through φ] from perfect S-algebras to abelian groups. 

### `one_tmul_eq_zero_of_tensorPush`

 Let S be an O^♭-algebra, φ: b → d a map of perfect S-algebras, and Q the functor
D ↦ ℤ[Hom(b,D)]/ℤ[maps factoring through φ] (`New.Variety.relFreeAbOfHom φ`). Let Φ be a functor
from perfect S-algebras to S-modules, and V → A a map of S-algebras with A flat over V. If x in
H^n(Q, V ⊗_S Φ) maps to zero in H^n(Q, A ⊗_S Φ) under the map induced by V → A (`tensorPush`), then
1 ⊗ x = 0 in A ⊗_V H^n(Q, V ⊗_S Φ). 

### `perfectAlmostCoeff`

 The functor sending a perfect S-algebra D to D ⊗ N ⊗ 𝔪, tensor products over O^♭ with 𝔪 its
maximal ideal, regarded as an S-module. 

 ### Reduction to valuation rings 

### `exists_tensorPush_ne_zero_of_isChain`

 Let z be a class in H^n(Q, D ↦ a ⊗_S D ⊗ N ⊗ 𝔪), Q = `New.Variety.relFreeAbOfHom φ`, and c a
non-empty chain of relations on a, each t in c of the form f, g ↦ ψ_t(f) ∣ ψ_t(g) for a map
ψ_t: a → B_t of perfect S-algebras whose push-forward keeps z nonzero. Then some map χ: a → L of
perfect S-algebras keeps z nonzero, and every relation in c implies χ(f) ∣ χ(g). 

### `exists_maximal_tensorPush_ne_zero`

 Let φ: b → d be a map of perfect S-algebras, a a perfect S-algebra, N an O^♭-module,
Q = ℤ[h_b]/ℤ[im h_d] (`New.Variety.relFreeAbOfHom φ`) and z ≠ 0 a class in H^n(Q, D ↦ a ⊗_S
D ⊗ N ⊗ 𝔪). Consider the relations f, g ↦ ψ(f) ∣ ψ(g) on a, for the maps ψ: a → B of S-algebras, B
perfect, whose push-forward (`New.Variety.tensorPush`) keeps z nonzero. Among them there is a
maximal one m, for the order of implication between relations. 

### `exists_perfect_valuationRing_factor`

 Let S be an O^♭-algebra, and ψ: a → d, k: d → b be maps of perfect S-algebras with k ≠ 0,
such that for any two elements of a one of their images under ψ divides the other, and likewise
for k on d. Then kψ factors, by S-linear maps α: a → V and β: V → b, through a perfect S-algebra
V that is a valuation domain. 

### `tensorPush_quotient_ne_zero`

 Let φ: b → d be a map of perfect S-algebras, a a perfect S-algebra, and let p^♭ kill the
O^♭-module N. Let I be an ideal of a such that the image of p^♭ in a divides every element of I,
or is radical in a. Then a nonzero class z in H^n(ℤ[h_b]/ℤ[im h_d], D ↦ a ⊗ D ⊗ N ⊗ 𝔪) stays
nonzero when pushed along a → a/I. Here h_b = Hom(b, –) and im h_d is the set of maps that
factor through φ. 

### `faithfullyFlat_descent`

 Let S be a perfect O^♭-algebra, i: S → d and k: d → a maps of perfect S-algebras, ρ: V → a a
faithfully flat map of S-algebras, and N an O^♭-module. Then every class x in
H^n(ℤ[h_S]/ℤ[im h_d], D ↦ V ⊗_S D ⊗ N ⊗ 𝔪) is zero; here h_S = Hom(S, –) and im h_d is the set
of maps that factor through i. 

### `perfectAlgAlong`

 For a map φ: b → d of perfect S-algebras, the ring d regarded as a perfect b-algebra through
φ. 

### `exists_tensorPush_ne_zero_and_dvd_total`

 Let S be a perfect O^♭-algebra, φ: b → d a map of perfect S-algebras, a a perfect
S-algebra, and z ≠ 0 a class in H^n(ℤ[h_b]/ℤ[im h_d], D ↦ a ⊗_S D ⊗ N ⊗ 𝔪)
(`New.Variety.relFreeAbOfHom φ`). Suppose that these groups vanish in every degree m < n for every
perfect S-algebra E in place of a. Then z stays nonzero (`New.Variety.tensorPush`) along some map
ψ: a → B of S-algebras, B perfect, such that of any two images under ψ one divides the other. 

### `isCover_reprMap_of_forall_subsingleton`

 Let y: b → b' be a map of perfect O^♭-algebras, regarded also as a map of perfect b-algebras (b'
a b-algebra through y; `structureMap` is the map from b, seen as a b-algebra over itself, to b').
Suppose that for every n and every perfect b-algebra E the relative cohomology H^n(ℤ[h_b]/ℤ[im
h_{b'}], D ↦ E ⊗_b D ⊗ N ⊗ 𝔪) of this map of b-algebras vanishes. Then h_{b'} → h_b is a cover
(`New.Variety.IsCover`) for the coefficients D ↦ D ⊗ N ⊗ 𝔪 on perfect O^♭-algebras. 

### `isCover_of_points`

 Let p^♭ kill N and let y : b → b' be a map of perfect O^♭-algebras such that every
map from b to the tilt of a test (`New.Variety.PadicTest`) factors through y. Then h_{b'} → h_b is a
cover (`New.Variety.IsCover`) for the coefficients D ↦ D ⊗ N ⊗ 𝔪; here h_b = Hom(b, –) on perfect
O^♭-algebras, and ι includes them into all O^♭-algebras. This is v-descent for these
coefficients. 


## Acyclicity of points in tilts

`New.Variety.IsAcyclicAt φ F B` says that the functor Hom(B, φ –) with coefficients F∘φ has
cohomology F(B), in degree 0. `New.Variety.IsAcyclicOnPerfect F` says this for the tilt functor and
every perfect O♭-algebra B.


### `Comparison.IsBijective.transfer`

 Let `c` and `c'` compare the coefficients `F` on `C` and `F'` on `C'` with the same coefficients
`G` on `D`, and let `u` and `v` map a functor `Y` on `D` to the points of `B` and of `B'`. A point
`y` of `Y A` gives maps `F B → G A` and `F' B' → G A`; suppose that they agree through a bijection
`γ : F B → F' B'`. If `c` is bijective along `u`, then `c'` is bijective along `v`. 

### `IsAcyclicOnPerfect`

 For every perfect O^♭-algebra b, the functor S ↦ Hom(b, S^♭) on p-adic tests, with coefficients
S ↦ F(S^♭), has cohomology F(b), in degree 0. 

### `exists_isPointwiseSurjective_and_isAcyclicAt`

 Every perfect O^♭-algebra b has a map y: b → b' of perfect O^♭-algebras that is onto on points
in tilts of p-adic tests, such that the points of b' in tilts of tests are acyclic for the
coefficients D ↦ D ⊗ N ⊗ 𝔪. The proof takes b' to be the tilt of one test through which all points
of b factor, or the zero ring if b has no point. 

### `isAcyclicAt_perfectTilt`

 Almost descent. Let N be an O^♭-module killed by p^♭, and 𝔪 the maximal ideal of O^♭. For b
perfect over O^♭, S ↦ Hom(b, S^♭) on p-adic tests with coefficients S^♭ ⊗ N ⊗ 𝔪 has cohomology
b ⊗ N ⊗ 𝔪, in degree 0. 

### `isAcyclicOnPerfect_almostCoeff`

 Let `N` be an `OFlat`-module killed by `pFlat`. For every perfect `OFlat`-algebra `b`, the
cohomology of the points of `b` in the tilts of tests, with coefficients `almostCoeff N`, is the
value of the coefficients at `b`, placed in degree zero. 
