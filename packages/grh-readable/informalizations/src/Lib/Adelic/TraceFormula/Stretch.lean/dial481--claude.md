---
{
  "module": "src/Lib/Adelic/TraceFormula/Stretch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/Stretch.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/Stretch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rational points that pair short lattice vectors non-trivially

Let `y, y'` be vectors of the lattice of `V.move x` whose lengths have product at most `δ`, and let
`γ` be a rational point such that `x⁻¹ γ x` has finite part in a compact set. If `⟨y', γ y⟩` is not
`0`, then `(c δ)^f` times the product of `‖x⁻¹ γ x‖` over the `f` infinite places is at least `1`,
for a constant `c` that depends only on `V` and the compact set, because a non-zero algebraic
integer has norm at least `1`.

* `New.Space.exists_one_le_pow_mul_prod_norm`: the lower bound.

Notions from other files:
* `Space E n s`: a matrix `V.J` of a hermitian form on `E^n`, for `E` a field with a CM type
  (`CMType E`) whose embedding `Φ w` into `ℂ` gives the infinite place `w`, with an adelic basis
  `V.x` in which the form is `diag s` at infinity and `1` at the finite places; `V.move g` has the
  basis `V.x g`.
* `V.vecAtPoint y` is the adelic vector of coordinates of `y` in the basis `V.x`; `V.archCoords y`
  is its archimedean part, `V.coordsAt w y` its part at the infinite place `w`, and `V.baseLattice`
  is the lattice of the `y` for which its finite part is integral.
* `G E s` is the adelic unitary group, the product of the part at infinity and the finite part
  `Gf E n`; `V.ratEmbed γ` is the element of `G E s` given by a rational point `γ` of `U V.J`, the
  unitary group of the form `V.J` over `E`, in the basis `V.x`.


### `vecAtPoint_move_mulVec`

 For `x` in the adelic unitary group `G E s` and a rational point `γ` of the unitary group of
the form `V.J`, the adelic coordinates `vecAtPoint` of `γ b` in `V.move x` (the space `V` with its
basis moved by `x`) are those of `b` multiplied by the matrix `adeleMatrix` of `x⁻¹ γ x`, where `γ`
is embedded in `G E s` by `ratEmbed`. 

### `norm_coordsAt_mulVec_le`

 Let `x` lie in the adelic unitary group `G E s` (first factor: the part at infinity) and let
`γ` be a rational point of `U V.J`, embedded by `ratEmbed`. At an infinite place `w` the length of
`γ b` in the coordinates `coordsAt w` of `V.move x` (the space `V` with its basis moved by `x`) is
at most the length of `b` times the operator norm of the component at `w` of `x⁻¹ γ x`. 

### `exists_one_le_pow_mul_prod_norm`

 If `⟨y', γ y⟩ ≠ 0` for short lattice vectors `y` and `y'`, then `x⁻¹ γ x` is large at infinity.
Here `x` lies in the adelic unitary group `G E s`, whose two factors are the part at infinity and
the finite part, and `γ` is a rational point of `U V.J`, embedded in `G E s` by `ratEmbed`. For a
compact set `Ω` of finite parts there is `c ≥ 0` with the following property. Let `y` and `y'` lie
in the lattice of `V.move x` (the form of `V` with the basis moved by `x`), let their lengths
`‖archCoords‖` there have product at most `δ`, let the finite part of `x⁻¹ γ x` lie in `Ω`, and
let `⟨y', γ y⟩ ≠ 0`. Then `(c δ)^f` times the product of the operator norms of `x⁻¹ γ x` at the
infinite places is at least `1`, where `f` is the number of these places. 
