---
{
  "module": "src/Lib/Adelic/Witt/IwasawaDecomposition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/IwasawaDecomposition.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/IwasawaDecomposition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Maximal compact subgroup, splittings of isotropic frames and the Iwasawa decomposition

The file concerns the adelic unitary group `New.G E s` of a CM field `E` and its maximal compact
subgroup `New.maxCompact E s`, and the stabiliser of the span of k for a splitting of a hermitian
space along dual isotropic frames k, l. After the first section `E` carries a CM type and, for the
most part, Weil data (`New.WeilData`: roots of unity of order 5040, a purely imaginary element `j`
and further choices).

## Main definitions and results

* `New.Space.exists_splitting`: every isotropic frame `k` of a hermitian space `V` is part of a
  splitting `V = range l ⊕ V₀ ⊕ range k` (`New.Space.Splitting`, a Witt decomposition). The proof
  compares `V` with the sum of a hyperbolic space and a standard space by Landherr's theorem
  (`New.Space.landherr`) and moves the frame by Witt's theorem (`New.Space.witt`).
* `New.Space.Splitting.radicalCentre`: the centre of the radical, parametrised additively by adelic
  matrices M through M − M*; it sends rational matrices to rational points.
* `New.Space.Splitting.centreCoeff`: the Fourier coefficients of a function along this centre.
* `New.Space.Splitting.iwasawa`: the Iwasawa decomposition for the maximal compact subgroup
  `New.maxCompact`, obtained at each infinite place and over the finite adeles from Witt's theorem
  (`New.Space.Splitting.iwasawa_of_witt`). The compact factor can be taken trivial where the given
  element is (`New.Space.Splitting.exists_mem_maxCompact_actsOnFrame_and_eq_one`).
* `New.Space.Splitting.exists_eq_radicalElement_mul_levi_mul_isAdapted`: every element is a product
  of an element of the radical, a Levi element and an element adapted to the splitting.

Notions from other files:
* `New.G E s`: the adelic unitary group of the form ε (`New.stdForm`) that is diag(s) at the
  infinite places and the identity at the finite places; `g.adeleMatrix` is the adelic matrix of
  `g`.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with
  xᴴJx = ε; `W.Γ` is the group of rational points in `New.G E s`.
* `New.U A`: the unitary group of a matrix A.
* `New.parabolic`: the invertible matrices that are block upper triangular for a level function.

## Relation to the literature

Known results: Witt's extension theorem for hermitian forms and for unimodular hermitian lattices,
and the Iwasawa decomposition. Witt's theorem is imported: over fields with a nontrivial involution
for invertible hermitian forms (`New.witt`), and over the integral finite adeles only for primitive
frames of the identity form over a CM field containing the roots of unity of order 5040
(`New.witt_Ô`). Its form in the maximal compact subgroup at an infinite place is deduced here: an
isotropic subspace is the graph of an isometry between the coordinates of the two signs. Source: U.
A. First, Witt's extension theorem for quadratic spaces over semiperfect rings, J. Pure Appl.
Algebra 219 (2015), Cor. 4.9 (for fields, Dieudonné, La géométrie des groupes classiques, 1955; for
lattices, Jacobowitz, Amer. J. Math. 84 (1962)). For the Iwasawa decomposition at the finite places:
J. Tits, Reductive groups over local fields, Proc. Sympos. Pure Math. 33 (1979), part 1, 3.3.2 and
3.8.1.



## The maximal compact subgroup of the adelic unitary group

`New.G E s` is the adelic unitary group of the CM field `E`: one complex unitary group of the sign
matrix `New.signMatrix s` for each infinite place, times the unitary group of the identity matrix
over the finite adeles.


### `New.maxCompact`

 The subgroup K_∞K₀ of G: elements that are unitary matrices at each infinite place and lie
in GL_n(Ô) at the finite places. 

### `New.mem_maxCompact_iff_isOrthoIntegral_adeleMatrix`

 An element of the adelic unitary group lies in the maximal compact subgroup exactly when its
matrix has orthonormal columns at every infinite place and integral finite entries
(`New.Exchange.IsOrthoIntegral`). 

 ## Existence of splittings of isotropic frames 

### `New.rank_le_card_preimage_of_isotropic`

 If a complex matrix `X` is isotropic for the form diag(s), then its rank is at most the number
of coordinates `i` with `s i = ε`, for either sign `ε`. 

### `New.exists_equiv_hyperbolicSigns`

 If each sign occurs at least `card p` times in `s`, then the coordinates can be numbered by
`(p ⊕ p) ⊕ Fin m` so that the first copy of `p` has sign 1 and the second sign -1: the signs become
`hyperbolicSigns p` (1 on the first copy, -1 on the second) joined with some `s₀` on `Fin m`. 

### `New.Space.card_le_card_preimage_of_isotropic`

 If the columns of a left invertible matrix `k` span an isotropic subspace of `V`, then each
sign occurs among the signs `s` of `V` at least as often as `k` has columns. 

### `New.Space.exists_splitting`

 Let `k` be a left invertible `n × p` matrix over `E` whose columns span an isotropic subspace of
`V`, that is, `kᴴ J k = 0` for the Gram matrix `J`. Then `k` is the frame `D.k` of a splitting `D`
of `V` (dual isotropic frames `D.k`, `D.l` and a copy of `V₀` orthogonal to both) over some space
`V₀` with coordinates indexed by `Fin m`. 

### `New.Space.card_eq_of_perp_subset`

 Let `k`, `l` be dual isotropic frames of `V`, whose Gram matrix is `J`, and let `i` be an
isometric embedding of a space `V₀` into `V` that is orthogonal to both. If every vector orthogonal
to the columns of `k` has the form `k a + i b`, then the rank of `V` is the rank of `V₀` plus twice
the number of columns of `k`. 

### `New.Space.exists_splitting_of_perp_eq`

 Let `k` be a left invertible `n × p` matrix over `E` whose columns span an isotropic subspace
`A` of `V` (`kᴴ J k = 0` for the Gram matrix `J`), and let `i` be an isometric embedding of a space
`V₀` into `V` (`iᴴ J i = J₀`) such that the orthogonal complement of `A` is `A + i V₀`: a vector `y`
satisfies `kᴴ J y = 0` exactly when `y = k a + i b` for some `a`, `b`. Then there is a splitting `D`
of `V` over `V₀` whose isotropic frame `D.k` is `k` and whose embedding `D.i` is `i`. 


## Adapted elements, the centre of the radical and the Iwasawa decomposition

H is a splitting of W over W₀ (`New.Space.Splitting`): dual isotropic frames k, l and a copy of W₀
orthogonal to both. In standard adelic coordinates k is `New.Space.Splitting.kAdelic`; the
stabiliser of its span has a unipotent radical with elements `New.Space.Splitting.radicalElement`
and a Levi subgroup parametrised by `New.Space.Splitting.levi`.


 ### Adapted elements 

### `IsAdapted.inv_mul_mem_maxCompact`

 Let `H` be a Witt decomposition of `W` over `W₀`, and let `l`, `k`, `ι` be its two isotropic
frames and its embedding of `W₀` in standard adelic coordinates (`H.lAdelic`, `H.kAdelic`,
`H.iAdelic`). Let `t` be in GL_p(𝔸). Suppose two elements `g`, `g'` of the adelic unitary group
`G E s` are both adapted to `H` and `t`: the matrices `g⁻¹ (l (t⁻¹)ᴴ, k t, ι)` and
`g'⁻¹ (l (t⁻¹)ᴴ, k t, ι)` have orthonormal columns at every infinite place and integral entries at
the finite places. Then `g⁻¹ * g'` lies in the maximal compact subgroup K_∞K₀. 

### `IsAdapted.mul_of_mem_maxCompact`

 An element adapted to the splitting `H` and the basis `γ` (its frame `H.frameAt h γ`, the matrix
h⁻¹ (l (γ⁻¹)ᴴ, k γ, ι) built from the frames `H.lAdelic`, `H.kAdelic` and the embedding `H.iAdelic`,
has orthonormal columns at the infinite places and is integral) stays adapted after right
multiplication by an element of the maximal compact subgroup. 

 ### The centre of the radical 

### `radicalCentre`

 For an adelic p×p matrix M, the element 1 + k(M − M*)k*ε (k*ε is `H.lCoord`) of the centre of
the unipotent radical of the stabiliser of the span of the isotropic frame k. 

### `mul_radicalCentre`

 If `g` acts on the isotropic frame k of the splitting by the matrix `c`, that is `g k = k c`,
then conjugation by `g` carries the element 1 + k(M − Mᴴ)kᴴε of the centre of the radical to the
element given by `c * M * cᴴ`. 

### `centreCoeff`

 The Fourier coefficient at T of a function D at g: the mean of ψ(tr TM)·D(z(M)g) over adelic
matrices M modulo rational ones, z = `New.Space.Splitting.radicalCentre`. 

 ### The Iwasawa decomposition 

### `iwasawa_of_witt`

 The Iwasawa decomposition in one component `f : 𝔸 E →+* S` of the adeles, where `A` stands for
the form: `H.lCoord` maps to (k*)A for the image k of the isotropic frame `H.kAdelic` (hypothesis
`h_form`). Let `P` be a class of frames such that every left invertible frame is brought into `P`
by an invertible matrix that is block triangular for `wt`, and any two isotropic frames in `P`
differ by an element of `C`. Then for each isometry `u` of `A` there is `κ ∈ C` such that `u * κ`
acts on k by such a block triangular matrix. 

### `exists_unitary_mul_eq_of_isotropic`

 Witt's theorem in K = U(diag s) ∩ U(n): two frames that are orthonormal and isotropic for
diag s differ by an element of K. 

### `exists_mem_maxCompact_actsOnFrame`

 For a Witt decomposition `H` of `W` with isotropic frame `k`, every `g` in the adelic unitary
group `G E s` of `W` has a right translate `g * κ`. Here `κ` lies in the maximal compact subgroup
K_∞K₀, and `g * κ` acts on `k` by some `b` in GL_p(𝔸) (`H.ActsOnFrame`: g κ k = k b). This `b` is
block triangular for the weights `wt : p → ℕ`. 

### `exists_mem_maxCompact_actsOnFrame_and_eq_one`

 The Iwasawa decomposition place by place. Every `g` has a right translate `g * κ`, with `κ` in
the maximal compact subgroup, that acts on the isotropic frame k by a matrix `b` (`H.ActsOnFrame`:
g κ k = k b) that is block triangular for the weights `wt`, where `κ` is trivial at every infinite
and every finite place at which `g` is trivial (`atPlace w` is the component at `w`). 

### `iwasawa`

 The Iwasawa decomposition. Every `g` has a right translate `g * κ`, with `κ` in the maximal
compact subgroup, that acts on the isotropic frame by a matrix `b`, block triangular for the
weights `wt` (`H.ActsOnFrame`), and is therefore the product of a unipotent element
`H.radicalElement c z`, with adelic matrices `c`, `z`, and the Levi element `H.levi (b, u)`, where
`u` is in the unitary group of the smaller space. For the first part alone see
`New.Space.Splitting.exists_mem_maxCompact_actsOnFrame`.

This is an adelic form of the Iwasawa decomposition G = PK (Bruhat–Tits at the finite places) for
this unitary group and the stabilisers of isotropic flags. 

### `exists_eq_radicalElement_mul_levi_mul_isAdapted`

 The Iwasawa decomposition with an adapted factor: every `g` is an element of the radical times a
Levi element times an element `h` adapted to the splitting `H` and the basis `1`. 
