---
{
  "module": "src/Lib/Weil/Construction/WeilData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting characters, Weil data, and the adelic Heisenberg cocycle and vacuum

On a CM field `E` with CM type `Φ` (`New.CMType`; `Φ w` is the embedding τ : E → ℂ chosen at the
infinite place w), this file fixes the arithmetic data that determine the Weil representation. From
these data the file builds the adelic Heisenberg bicharacter and the vacuum function on `𝔸^n`, the
two ingredients of the adelic Weil representation.

## Main definitions and results

* `New.SplittingChar`: a splitting character `υ`, a unitary Hecke character with prescribed values
  on ideles whose finite part is a unit.
* `New.WeilData`: `υ` together with a purely imaginary `ȷ ∈ E`, which turns the hermitian form into
  a Heisenberg cocycle, and a finite idele `α`, which scales the vacuum lattice.
* `New.WeilData.scaleIdele`: the idele with finite part `α` that normalises the real coordinates.
* `New.adelicHeisenberg`: the bicharacter β(x, y) = ψ(½ȷ y*Sx), where S is `New.stdForm`, the
  diagonal form with signs `s` at the infinite places and 1 at the finite ones.
* `New.vacuumFn`: the vacuum, a Gaussian at the infinite places times a function of modulus one on
  the lattice αÔ^n of finite vectors (zero off the lattice). It does not depend on `s`.

Notions from other files:
* `New.𝔸`: The ring ℂ^f × 𝔸_f, one copy of ℂ for each infinite place of E times the finite adeles:
  the adele ring of E when E is totally complex.
* `New.ψf`: The standard additive character of the finite adeles: ψ_f(x) = exp(2πi Tr_{E/ℚ}(a)) for
  any a in E with x − a integral.
* `New.Heisenberg`: A continuous function β on W × W, W a topological abelian group, with values of
  modulus one, multiplicative in each variable, and β(x,x) = 1.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` and `Lib.ClassField.Global.CMSplittingCharacters` for
sources.



## Splitting characters and Weil data

`New.Ô E` is the ring of integral finite adeles.


### `SplittingChar`

 A splitting character: a unitary Hecke character `υ` of `E` with `υ x̄ = (υ x)⁻¹` that equals
`∏ x_τ / |x_τ|` (over the infinite places) when the finite part of the idele `x` is a unit of
`Ô`, that is, when the finite parts of `x` and of `x⁻¹` both lie in `Ô`. 

### `SplittingChar.υ`

 The unitary Hecke character υ of E. 

### `SplittingChar.υ_unit`

 If the finite part of the idele x is a unit of Ô, then υ(x) = ∏ x_τ / |x_τ| over the infinite
  places τ, where x_τ = `(x : 𝔸 E).fst τ` is the component of x at τ. 

### `SplittingChar.υ_star`

 Complex conjugation inverts υ: υ(x̄) = υ(x)⁻¹. 

### `WeilData`

 Weil data on E, which contains a primitive 5040th root of unity (`New.HasPrimitiveRoot5040`;
then E/E⁺ is unramified at the finite places): ȷ = −ȷ̄ in E with Im τȷ > 0 and (1 − ȷ⁻¹)/2 integral,
a finite idele α making Ô self-dual for the pairing (z, u) ↦ ψ_f(ȷαᾱzu) of finite adeles z, u, and a
splitting character υ equal to −1 at uniformisers of places w = w̄. 

### `WeilData.j`

 The element ȷ of E. 

### `WeilData.star_j`

 ȷ is purely imaginary: its conjugate is −ȷ. 

### `WeilData.im_pos`

 ȷ has positive imaginary part under each embedding of the CM type. 

### `WeilData.α`

 The finite idele α of E. 

### `WeilData.self_dual`

 At every finite place w, the order of ȷαᾱ is minus the order of the different of E. 

### `WeilData.isIntegral_traceOne`

 c₀ = (1 − ȷ⁻¹) / 2 is an algebraic integer. 

### `WeilData.υ_inert`

 At a finite place w fixed by conjugation, υ is −1 on the chosen uniformiser. 

### `scaleIdele`

 The idele whose component at each infinite place τ is (2π Im τȷ)^(-1/2) and whose finite
part is α. 

### `traceOne`

 The element c₀ = (1 − ȷ⁻¹)/2 of E, ȷ from the Weil data; it is an algebraic integer with
c₀ + c̄₀ = 1. 

### `j_ne_zero`

 The element ȷ of the Weil data is nonzero, since Im τȷ > 0 at every infinite place τ. 


## The adelic vacuum function and the Heisenberg cocycle

The purely imaginary ȷ (written `j`), the finite idele α and c₀ = (1 − ȷ⁻¹)/2 (written `traceOne`)
come from `New.WeilData`. ψ is `New.stdAddChar`, the standard additive character of the adeles. An
adele `x` is a pair: `x.1` is the family of its infinite components, `x.2` its finite part.


### `vacuumFn`

 The vacuum on adelic vectors: exp(−π ∑_{i,τ} Im(τȷ)|x_{i,τ}|²) times ψ_f(½c₀ȷ x_f*x_f) if
the finite part x_f lies in αÔ^n, and 0 otherwise. 

### `vacuumFn_eq_exp_mul_ite`

 The phase of the vacuum is ψ_f(−¼ x_f*x_f): c₀ȷ/2 = (ȷ − 1)/4, and ψ_f does not see the skew
part ȷ x_f*x_f/4. 

### `adelicHeisenberg`

 The Heisenberg datum on adelic n-space with bicharacter β(x,y)=ψ(½ȷ h(y,x)), h being the
hermitian form with matrix `New.stdForm E s`; `toAdele` is the embedding of E in the adeles
`𝔸 E`. 
