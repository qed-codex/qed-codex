---
{
  "module": "src/Lib/Adelic/TraceFormula/ChangingSigns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/ChangingSigns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/ChangingSigns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Types of frames with a similitude, and the permutation of orbits that changes signs

Let E be a CM field with CM type Φ and y ∈ GL_n(E). If the characteristic polynomial of y is
separable, its roots under an embedding into ℂ are numbered by `New.Variety.numberedRoots`.
`New.Variety.MarkedTriple` K Z is the set of triples (xK, y, μ), x ∈ GL_n(𝔸_f), y ∈ GL_n(E) and
μ ∈ Z; z ∈ GL_n(E) acts on it by (xK, y, μ) ↦ (zxK, zyz⁻¹, μ).

* `New.Variety.IsEllipticSimilitude`: y has irreducible characteristic polynomial and is a
  similitude of a form β with multiplier ν, all of whose eigenvalues r satisfy r r̄ = ν.
* `New.Variety.HasSignType`: y is an elliptic similitude of a form β whose Gram matrix in the finite
  frame x satisfies a given condition, with signs ε on the eigenvectors of y at each infinite place.
* `New.Variety.exists_hasSignType_mul_iff`: for signs η of product 1, moving the frame by a suitable
  finite adelic matrix U changes the signs by η, and these moves permute the orbits of marked
  triples.

Notions from other files:
* `Φ w`: the embedding of E into ℂ that the CM type chooses at the infinite place w.
* `𝔸f E`: the ring of finite adeles of E.

## Relation to the literature

Known; see `Lib.Adelic.TraceFormula.TraceComparison` for sources.


### `roots_eq_map_numberedRoots`

 For y in GL_n(E) with separable characteristic polynomial P and an embedding t of E into ℂ,
the numbering `New.Variety.numberedRoots` lists the complex roots of t(P), each once. 

### `isRoot_numberedRoots`

 If the characteristic polynomial of y is separable, then each numbered root of its image under t
is a root of the characteristic polynomial of the image of y under t. 

### `IsEllipticSimilitude`

 The element y is an elliptic similitude of β with multiplier ν: its characteristic polynomial is
irreducible, ν ≠ 0, yᴴβy = νβ, and under each embedding of the CM type every complex root r of the
characteristic polynomial satisfies r r̄ = ν. 

### `IsEllipticSimilitude.irreducible_charpoly`

 The characteristic polynomial of y is irreducible. 

### `IsEllipticSimilitude.ne_zero`

 The multiplier is not zero. 

### `IsEllipticSimilitude.conjTranspose_mul_mul`

 The element y multiplies the form β by ν. 

### `IsEllipticSimilitude.root_mul_star_Φ`

 Under each embedding of the CM type, every complex root r satisfies r r̄ = ν. 

### `HasSignType`

 The pair (y, x) has type ε for the multiplier ν and the condition F if there is a matrix β over
E such that (a) y is an elliptic similitude of β with multiplier ν
(`New.Variety.IsEllipticSimilitude`); (b) F holds for the Gram matrix xᴴβx over the finite adeles;
(c) at each infinite place w, βp_w(y) is positive definite, p_w the polynomial interpolating the
signs ε_w at the roots numbered by `New.Variety.numberedRoots`. 

### `exists_eigenbasis_diag_form`

 Let `y` be an elliptic similitude of `β` with multiplier `ν`: its characteristic polynomial is
irreducible, `ν ≠ 0`, `yᴴβy = νβ`, and under each embedding of the CM type every root `r` satisfies
`r r̄ = ν`. Let `w` be an infinite place and `σ` a permutation of the index set. Write `g` and `B`
for the images of `y` and `β` under the embedding of the CM type at `w`. Write `x_i` for the root
numbered `σ(i)` by `New.Variety.numberedRoots`. There are an invertible `k` and numbers `d_i` with
three properties. (a) `kᴴBk = diag(d)`. (b) For every polynomial `q`, `B·q(g)` is positive definite
iff all `d_i q(x_i) > 0`. (c) For signs `t` with all `d_i t_i > 0`, some invertible `k` has
`kᴴBk = diag(t)` and `k⁻¹gk = diag(x)`. 

### `mul_aeval_eq_conjTranspose_mul`

 Let y be an elliptic similitude of β with multiplier ν and let c be a polynomial with
y c(y) = ν. Then c(y) is the adjoint of y for β, that is, β c(y) = yᴴ β. 

### `posDef_mul_interpolate_iff`

 Let y be an elliptic similitude of β with multiplier ν, w an infinite place, and r_i the
numbered roots of its characteristic polynomial at w. If η_i δ(r_i) > 0 for a polynomial δ and
signs η_i, then β has signs ε at w iff β δ(y) has signs εη there. That is, at w the matrix β p(y)
is positive definite iff β δ(y) q(y) is, where p interpolates ε and q interpolates εη at the
roots. 

### `IsEllipticSimilitude.root_mul_star`

 Let y be an elliptic similitude of a form with multiplier ν
(`New.Variety.IsEllipticSimilitude`). Then every complex root r of the characteristic polynomial
satisfies r r̄ = ν, under every embedding of E into ℂ. 

### `isEllipticSimilitude_mul_aeval_iff`

 Let δ be a polynomial with δ(y) invertible. Then y is an elliptic similitude of β δ(y) with
multiplier ν if and only if it is one of β, because δ(y) commutes with y. 

### `eq_of_mk_lift_numberedRoots_eq`

 Let P, the characteristic polynomial of y, be irreducible. For each infinite place w let Φ w be
the embedding of the CM type at w and r_w the numbering of the complex roots of P under Φ w. Then
the embeddings of E[X]/(P) that extend Φ w and send the root to r_w i give different infinite
places for different pairs (w, i). 

### `aeval_conj_comp_mul_aeval_eq`

 If the characteristic polynomial of y divides the difference of ḡ(c) g and δ, then
ḡ(c(y)) g(y) = δ(y) over the finite adeles, by the Cayley–Hamilton theorem. Here ḡ has the
conjugate coefficients of g. 

### `exists_coprime_sign_dvd_norm_sub`

 Let y be an elliptic similitude with multiplier ν₀ and characteristic polynomial P, and let η be
signs of total product 1. There are polynomials δ, c over E and g over the finite adeles with four
properties: δ is prime to P; δ has the signs η at the numbered roots of P; modulo P the product
X c is the constant ν for each ν that is r r̄ for all complex roots r of P; and modulo P the product
of ḡ(c) and g is δ, where ḡ has the conjugate coefficients. 

### `gram_aeval_eq_map_mul_aeval`

 Let y be an elliptic similitude of β with multiplier ν and let P be its characteristic
polynomial. Let c, δ over E and g over the finite adeles be polynomials with X c = ν and
ḡ(c) g = δ modulo P. Then the Gram matrix of β in the frame g(y) is β δ(y). 

### `exists_aeval_hasSignType_mul_iff`

 For signs `η` of total product one and a polynomial `P` over `E` there is a polynomial `υ` over
the finite adeles of `E` such that, for every `y` with characteristic polynomial `P`, the matrix
`υ(y)` is a unit `U`, and for all `ν`, `ε`, `F` and `x` the pair `(y, x)` has type `εη`
(`New.Variety.HasSignType`: an elliptic similitude with multiplier `ν` of some form whose Gram
matrix in the frame lies in `F` and whose signs at infinity are given) iff `(y, U x)` has type
`ε`. 

### `exists_hasSignType_mul_iff`

 Change of signs. Let η assign a sign to each mark μ, infinite place w and index i, with product
1 for each μ. A marked triple (q, y, μ) is a coset q ∈ GL_n(𝔸_f)/`K`, y ∈ GL_n(E) and a mark μ;
GL_n(E) acts by left translation on q and by conjugation on y. There is a permutation e of the
orbits such that for every y ∈ GL_n(E) and mark μ some U ∈ GL_n(𝔸_f) satisfies: (a) for all ν, ε, F
and x, the pair (y, x) has type εη_μ iff (y, Ux) has type ε (`New.Variety.HasSignType`: for some β,
y is an elliptic similitude of β with multiplier ν, F holds for xᴴβx, and signs ε hold at infinity);
(b) U commutes with the image of every z ∈ GL_n(E) that commutes with y; (c) e sends the orbit of
(q, y, μ) to the orbit of (Uq, y, μ). 
