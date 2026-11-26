---
{
  "module": "src/Lib/Shimura/Deformation/TangentCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Deformation/TangentCount.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Deformation/TangentCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting w-torsion points bounds a space of natural semilinear functions by n − 1

`x` is a `k`-point of a family of abelian schemes with `𝓞 E`-action (`New.ThetaObject`).
`x.groupScheme` is its abelian variety, `x.baseHom : 𝓞 E → k` is the structure map and `w` its
kernel. A morphism `specOver k C ⟶ x.groupScheme` is a `C`-point, and `placeTorsion x C` is the
`𝓞 E`-module of the `C`-points killed by `w`; `placeTorsionMap ψ` carries such points along
`ψ : C → C'`, composing with `specOver.map ψ`. The main result is
`New.Variety.finrank_le_of_placeTorsion`; there `n = Fintype.card D.Index`.

## Relation to the literature

Known; see `Lib.Shimura.Deformation.TangentBound` for sources.


### `mem_powers_card_of_isLinearMap_pow`

 If x ↦ x^i, for a natural number i, is F-linear on an algebraically closed extension k of a
finite field F, then i is a power of |F|. 

### `exists_local_universal_point`

 Suppose that the kernel of `x.baseHom` contains some `p ≠ 0`. Then `placeTorsion x k` is finite,
and there is a local ring `B` (that of the finite group scheme `placeTorsion x` at the origin) with
a universal point `u`: a homomorphism out of `B` is determined by the image of `u`, and every point
with values in a local ring `C` that reduces to `0` along some `C → k` is such an image. 

### `adjoin_eq_top_and_exists_algHom_eq_smul`

 If a nilpotent `τ` divides every element of the kernel of `z : B → k`, then `τ` generates the
`k`-algebra `B`, and each scaling `τ ↦ a • τ` extends to an endomorphism of `B`. 

### `exists_dual_mul_eq`

 In a local `k`-algebra `B` with a `k`-point `z`, every `t ≠ 0` has a linear form `γ` with
`γ (t * b) = z b` for all `b`. 

### `eq_zero_of_dvd_cofactor`

 Let `τ ^ N = 0`. If for every factorisation `b = τ ^ i * g` with `τ ^ i ≠ 0` the cofactor `g` is
divisible by `τ`, then `b = 0`. 

### `IsLocalParameter`

 Facts on a `k`-algebra `B` with a point `u` of `placeTorsion x`, a map `s : B → k[ε]` and
an element `τ`, relative to a line `L` of tangent vectors of `x.groupScheme` at `0`: `u` is
universal (as in `exists_local_universal_point`), `s` sends `u` to `L 1`, and `τ` is a nilpotent
local parameter of `B` that `s` sends to a nonzero multiple of `ε`. 

### `IsLocalParameter.injective`

 A homomorphism out of `B` is determined by the image of `u`. 

### `IsLocalParameter.exists_map_eq`

 A point over a local `C` that reduces to `0` along `π : C → k` is an image of `u`. 

### `IsLocalParameter.val_eq`

 `s` sends `u` to the tangent vector `L 1`. 

### `IsLocalParameter.val_map_eq`

 Scaling `ε` by `a` then sends `u` to `L a`. 

### `IsLocalParameter.fst_eq_zero`

 `s τ` has no constant term. 

### `IsLocalParameter.snd_ne_zero`

 `s τ` has a nonzero `ε`-term. 

### `IsLocalParameter.pow_eq_zero`

 `τ` is nilpotent of order at most `N`. 

### `IsLocalParameter.dvd_of_fst_eq_zero`

 `τ` divides every element of `B` that `s` sends to a multiple of `ε`. 

### `IsLocalParameter.exists_lift`

 Every tangent vector `L a` is the image under `s` of a point over `B`. 

### `exists_isLocalParameter`

 Let `ker x.baseHom` contain `p ≠ 0`, and let `L` be a line of tangent vectors of `x.groupScheme`
at `0` (`L 1 ≠ 0`, each `L m` reduces to `0`) on which `𝓞 E` acts through `x.baseHom`, scaled by
the maps `ε ↦ m ε`. Let `ν` map a type `T` to the `k`-points of `placeTorsion x` such that every
point `z` over a local `k`-algebra with a `k`-point `π` has a parameter `t` with `π t = 0` and
`t ^ N = 0`, `N` the size of the fibre of `ν` over the reduction of `z`, and with `z` zero
modulo `t` when its reduction is `0` (`h_param`). Then some local `k`-algebra `B`, point `u`, map
`s : B → k[ε]` and element `τ` satisfy `IsLocalParameter` for `L` and the fibre of `ν` over `0`. 

### `pow_eq_div_of_isLocalParameter`

 Let `u`, `s`, `τ` satisfy `IsLocalParameter` for the tangent line `L`, and let `f` be natural
in `C` (`hf`). On a point `y` over `B` that `s` sends to the tangent vector `L a`, the coefficient
of `τ ^ i` is multiplied by `a ^ i`: if `f B u l = τ ^ i * g`, `γ` reads the coefficient of
`τ ^ i` (`hγ`) and `(s g).fst ≠ 0`, then `a ^ i = γ (f B y l) / (s g).fst`. 

### `apply_eq_zero_of_apply_universal_eq_zero`

 Let `u` be a point over the local `k`-algebra `B` through which every point that reduces to `0`
factors (`h_fac`), and let `f` be natural in `C` (`hf`). If `f B u l = 0` and `l` gives `0` at every
`k`-point, then `l` gives `0` at every point over a finite local `k`-algebra `C`: such a point is a
constant point plus one that factors through `u`. 

### `eq_zero_of_isLocalParameter`

 The main step of `finrank_le_of_placeTorsion`. Let `u`, `s`, `τ` satisfy `IsLocalParameter`
for the tangent line `L`, let `γ i` read the coefficient of `τ ^ i` (`hγ`), and let `f` be as in
`finrank_le_of_placeTorsion`. If `l` gives `0` at every `k`-point and the coefficient of
`τ ^ q ^ j` in `f B u l` is `0` for every `j > 0` with `τ ^ q ^ j ≠ 0`, with `q` the norm of
`w = ker x.baseHom`, then `l = 0`: a lowest term of `f B u l` would have degree `q ^ j` with
`j > 0`. 

### `finrank_le_of_placeTorsion`

 Let `x` over `k` be the reduction, at a good place `w = ker x.baseHom` (which gives some `p ≠ 0`
in `w` and a tangent line at `0` on which `𝓞 E` acts through `x.baseHom`), of an object `y` over a
valuation subring of `ℂ` with a full structure. Let `f` attach to each `l ∈ W` a function
`y ↦ f C y l` from the `w`-torsion points over a local `k`-algebra `C` to `C`, semilinear in `y`
along `x.baseHom` and linear in `l`, such that (a) `f` is natural in `C`; (b) `f` vanishes on the
points over `k[ε]` that reduce to `0`; (c) only `l = 0` gives zero on all finite local `C`. Then
`dim W ≤ n - 1`, where `n = Fintype.card D.Index` is the number of indices of the PEL datum `D`. 
