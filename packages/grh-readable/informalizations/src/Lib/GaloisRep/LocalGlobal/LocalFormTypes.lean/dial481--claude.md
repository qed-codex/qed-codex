---
{
  "module": "src/Lib/GaloisRep/LocalGlobal/LocalFormTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/LocalFormTypes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/LocalFormTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local GL_N(E_w)-action on forms, parahoric types and labels at a split place

This file relates forms on a definite hermitian space `V` to the local theory of `GL_N(E_w)` at a
split place `w`. The action of `GL n (𝒪_w)` on a function on the finite adelic group is then
described through the finite group `GL n (k_w)`, in two ways: by parahoric types and by labels.

## Main definitions and results

* `New.Patching.localFormRep`: the local representation on forms. It is smooth, and the vectors
  fixed by the pro-`p` Iwahori subgroup `New.proIwahori` in the span of the translates of one form
  (`New.cyclicSpan`) are finite-dimensional; both are instances.
* `New.hasHeckePolyAt_iff_localFormRep`: the Hecke polynomial at `w` read in the local
  representation.
* `New.HasParahoricType`: `f` has a parahoric type: the parabolic subgroup with blocks `b` acts
  through characters of the determinant on all blocks but one, and on the remaining block through a
  character of the determinant times a function `F`.
* `New.HasProductLabel`: `f` has a label: the class function of `GL n (k_w)` built from a polynomial
  and characters does not kill `f` (`New.HasLabel`).
* `New.HasParahoricType.hasProductLabel`: a type gives a label.

Notions from other files:
* `New.ofSplitPlace`: For a split place w, the homomorphism GL_n(E_w) → G_f sending g to the unitary
  element with component g at w and 1 off w, w̄; `New.offPartComap` is the open subgroup of G_f
  pulled back along the map replacing the components of an element of G_f at w and w̄ by 1.
* `New.ResField`: The residue field of the completion E_w of E at the finite place w.
* `New.labelChar`: The multiplicative map sending `c` to the parabolic-induction product of the
  class functions attached to the monic irreducible factors of `c`, with multiplicity.

## Relation to the literature

Known; see `Lib.GaloisRep.LocalGlobal.LabelCompatibility` for sources.



## The local representation on forms and its Hecke polynomials

`New.IsEigenform f P` says `f ≠ 0` and `New.HasHeckePolyAt f w hw (P w)` at almost all places of
prime norm; `New.levelSpace π K` is the space of `K`-fixed vectors.


### `Patching.embedAtSplit`

 For a split place w, the homomorphism GL_N(E_w) → G_f, N the cardinality of n, given by a
chosen numbering of n followed by `New.ofSplitPlace`. 

### `Patching.localFormRep`

 The representation of GL_N(E_w), N the cardinality of n, on forms of weight κ (a `New.Weight E`)
on V at a split place w: right translation `V.formTranslation κ` by G_f, pulled back along
`embedAtSplit`, which uses a chosen numbering of n. 

### `instance : IsSmoothRep (localFormRep V κ hw).ρ`

 The local representation on forms is smooth: each form is fixed by an open subgroup of the
local group. 

### `instance : Module.Finite ℂ ((cyclicSpan (localFormRep V κ hw).ρ x).submoduleOf (levelSpace (localFormRep V κ hw).ρ proIwahori))`

 In the span of the translates of one form, the vectors fixed by the pro-`p` Iwahori subgroup
form a finite-dimensional space. 

### `Space.invariantForm`

 A positive definite sesquilinear form on the forms of weight `κ` on `V` for which right
translation by the finite adelic unitary group is unitary (`New.IsUnitary`), chosen by
`New.Space.exists_isUnitary_formTranslation`. 

### `IsEigenform.of_mem_cyclicSpan`

 If a form x on V is an eigenform for the system P of Hecke polynomials, then so is every
non-zero y in the span of the translates of x under the local group GL_n(E_w) at a split
place w. 

### `hasHeckePolyAt_iff_localFormRep`

 At a split place w, a form x has Hecke polynomial P if and only if, in the local
representation of GL_n(E_w) on forms, GL_n(O_w) fixes x, the j-th Hecke operator scales x by
t_j, and P = Σ (−1)^j q_w^{j(j−1)/2} t_j X^{n−j}. 

 ## Parahoric types and labels at a split place 

### `HasParahoricType`

 `f` has a parahoric type at the split place `w`. The function `b` cuts the indices into blocks
`0, …, s`, and `e` numbers block `0`. An integral matrix `k` whose reduction is block triangular,
with block `0` equal to `x`, sends `f` to `∏ l, χ l (det k_(l+1))` times `ψ (det x)` times `F x`. 

### `HasProductLabel`

 `f` has a label at `w` built from `c` and the characters `χ l`. Here `c` is a label of degree
`d` (`IsLabel`), `c * ∏ l, (X - charName T (χ l))` is separable (`charName T (χ l)`, a unit of
`ResField w`, is the name of `χ l` read through `T`), and `d + ∑ l, t l = card n`. The label is
`labelChar T c * ∏ l, (χ l ∘ det on GL (t l))`. 

### `surjective_reindexGL_comp_blockHom_zero`

 Let block `0` of the blocks `b` be the image of `e` (`h_block`). Then the map from the
parabolic subgroup of `b` to `GL ρ (ResField w)` that takes block `0`, renumbered along `e`, is
onto: a matrix `x` extends by the identity matrix outside block `0`. 

### `_root_.Polynomial.separable_mul_prod_X_sub_C_of_squarefree`

 Over a perfect field, `a * ∏ l, (X - C (x l))` is separable when `a` is squarefree, the `x l`
are distinct and none of them is a root of `a`. 

### `HasParahoricType.hasProductLabel`

 A parahoric type gives a label. Let `σ` be a representation of `GL ρ (k_w)` on `V`, `L` an
injective linear map from `V` to functions on the finite adelic group, and `y` a vector not killed
by the idempotent `labelIdem ρ c` (a multiple of `∑ x, star ((labelChar T c).evalGL x) • x`, with
`T` as below; it is zero unless `c` is a label of degree `card ρ`). Let `f` have a parahoric type
with distinct `χ l`: `b` cuts `n` into blocks `0, …, s` and `e` numbers block `0`. An integral `k`
whose reduction is block triangular with block `0` equal to `x` sends `f` to
`∏ l, χ l (det k_(l+1))` times `ψ (det x)` times `L (σ x y)`. Let `T` be
`faithfulChar (ResField w)`, a chosen faithful character of the algebraic closure of `ResField w`
and `a` be `c` with its roots scaled by `charName T ψ`. If no `charName T (χ l)` is a root of `a`,
then `f` has the label `labelChar T a * ∏ l, (χ l ∘ det)` of degree `card ρ`, with blocks `l + 1`
(`New.HasProductLabel`). 
