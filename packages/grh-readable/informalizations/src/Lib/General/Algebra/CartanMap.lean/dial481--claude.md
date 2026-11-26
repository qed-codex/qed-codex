---
{
  "module": "src/Lib/General/Algebra/CartanMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/CartanMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/CartanMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Higman's criterion, dévissage and multiplicative functions on finite modules (Cartan map)

Tools that reduce a statement about finite `l`-power-torsion discrete `G`-modules to simple cases;
they serve the inequality of local duality (`Lib.ClassField.LocalDuality.DualityInequality`) and the
cocycle counts of `Lib.ClassField.GreenbergWiles.CocycleCounts`.

* `New.DiscreteModule.IsHigmanProjective`: Higman's criterion, some additive `τ` has `∑ g τ g⁻¹ = 1`
  over `G ⧸ Q`.
* `New.DiscreteModule.FiniteKilledFixedInj`: the module is finite, killed by `n` and fixed by `Q`,
  and `ρ z - m` is injective on it.
* `New.DiscreteModule.diagonalPermModule`: the functions `Y → A` with the diagonal action of `G`.
* `New.DiscreteModule.devissage_induction`: dévissage to modules killed by `l` and fixed by a normal
  subgroup `P`.
* `New.DiscreteModule.exists_open_sylow`: an open `P ≥ U` of index prime to `l` whose elements have
  an `l`-power power in `U`.
* `New.DiscreteModule.IsMultiplicative.eq_one_of_eq_one_on_isHigmanProjective`: on the finite
  modules killed by `l` and fixed by `U` with `ρ z - 1` injective, `z` central modulo `U`, a
  function with values in `ℚ≥0` that is multiplicative in short exact sequences is `1` as soon as it
  is `1` on the modules with Higman's property.

Notions from other files:
* `New.DiscreteModule R G`: an `R`-module with the discrete topology and a continuous `R`-linear
  action `ρ` of the topological group `G`.

## Relation to the literature

Known result: The Cartan map has finite cokernel. It is stated for multiplicative functions with
nonnegative rational values on finite modules killed by a prime on which one element, central modulo
the level, fixes no nonzero vector, with projectivity read as Higman's property. It is proved using
functions on two parallel affine hyperplanes instead of Brauer characters or Artin induction.
Source: J.-P. Serre, Linear Representations of Finite Groups (1977), Thm 35; for the route by
induction from cyclic subgroups in the local Euler characteristic formula, Milne, Arithmetic Duality
Theorems, I 2.10-2.12.


 ### Finite modules, Higman's criterion and function modules 

### `IsHigmanProjective`

 Higman's criterion for the discrete `G`-module `A` relative to a subgroup `Q` of finite index:
some additive `τ : A → A` has `∑ g τ g⁻¹ = 1`, summed over the chosen representatives `g.out` of the
cosets in `G ⧸ Q`. The map `τ` is not asked to commute with `Q`. If `Q` acts trivially on `A`, the
choice of representatives does not matter, see `TrivialOn.isHigmanProjective_iff`. 

### `TrivialOn`

 The subgroup `Q` of `G` acts trivially on the discrete `G`-module `A`. 

### `TrivialOn.conj_apply_eq_of_mk_eq`

 If `Q` acts trivially on `A`, the conjugate `g τ g⁻¹` of an additive map `τ` depends only on
the coset of `g` in `G ⧸ Q`. 

### `TrivialOn.isHigmanProjective_iff`

 If `Q` has finite index and acts trivially on `A`, Higman's criterion may be checked with any
system `s` of representatives of the cosets in `G ⧸ Q`. 

### `permModule`

 For a discrete `G`-module `A` and a finite set `Y` with an action of a discrete group `Δ`, the
`G × Δ`-module of functions `f : Y → A`, with `((g, δ) f) x = g (f (δ⁻¹ x))`. 

### `FiniteKilledFixedInj`

 The discrete `G`-module `A` is finite and killed by `n`, the subgroup `Q` acts trivially on it,
and `ρ z - m` is injective on it. 

### `FiniteKilledFixedInj.finite`

 The module is finite. 

### `FiniteKilledFixedInj.nsmul_eq_zero`

 The module is killed by `n`. 

### `FiniteKilledFixedInj.trivialOn`

 The subgroup `Q` acts trivially. 

### `FiniteKilledFixedInj.injective`

 The endomorphism `ρ z - m` is injective. 

### `FiniteKilledFixedInj.left_of_isShortExact`

 Being finite, killed by `n`, fixed by `Q` and with `ρ z - m` injective passes from the middle
term `B` of a short exact sequence `0 → A → B → M → 0` to `A`. 

### `FiniteKilledFixedInj.right_of_isShortExact`

 Being finite, killed by `n`, fixed by `Q` and with `ρ z - m` injective passes from the middle
term `B` of a short exact sequence `0 → A → B → M → 0` to `M`. 

### `isHigmanProjective_of_coprime_index`

 Let `Q` have finite index in `G`. If `A` is killed by an integer `n` prime to the index of `Q`,
then `A` satisfies Higman's criterion relative to `Q`. 

### `FiniteKilledFixedInj.isHigmanProjective_of_coprime`

 Let `Q` have finite index in `G`, and let `A` be finite, killed by `n` and fixed by `Q`, with
`ρ z - m` injective. If `n` is prime to the index of `Q`, then `A` satisfies Higman's criterion
relative to `Q`. 

 ### Dévissage and Sylow subgroups 

### `devissage_induction`

 Dévissage. Let `l` be prime, `n = l ^ j`, and let `p` be a property of the modules that are
finite, killed by `n`, fixed by `Q` and on which `ρ z - m` is injective. Let `P` be a normal
subgroup each of whose elements `g` has a power `g ^ l ^ i` in `Q`. If `p` holds for the modules
that are also killed by `l` and fixed by `P`, and is stable under extensions, then it always
holds. 

### `exists_open_sylow`

 For a prime `l` and `U` open normal in a compact group there is an open subgroup `P ≥ U` of
index prime to `l` each of whose elements `g` has a power `g ^ l ^ k` in `U`. 

 ### Function modules and multiplicative functions 

### `diagonalPermModule`

 Let `U` be open normal in `G`, let `S` be normal in `G ⧸ U` and let `Y` be a finite
`(G ⧸ U) ⧸ S`-set. The `G`-module of functions `f : Y → A` with the diagonal action
`(g f) y = g (f (g⁻¹ y))`, where `g` acts on `Y` through its image in `(G ⧸ U) ⧸ S`. 

### `exists_normal_pow_mem_not_dvd_card`

 Let `l` be prime, `U` open normal in the compact group `G`, and suppose every commutator
`⁅z, g⁆` lies in `U`. Then `G ⧸ U` has a normal subgroup of order prime to `l` that contains the
image of some power `z ^ l ^ j`. 

### `FiniteKilledFixedInj.diagonalPermModule`

 Let `l` be prime and let `A` be finite, killed by `l` and fixed by `U`, with `ρ z - 1`
injective. If `S` contains the image of a power `z ^ l ^ j`, the functions `Y → A` on a finite
`(G ⧸ U) ⧸ S`-set `Y`, with the diagonal action of `G`, have the same properties. 

### `isHigmanProjective_diagonalPermModule`

 Let the prime `l` kill `A` and not divide the order of `S`. The functions `Y → A` on a finite
`(G ⧸ U) ⧸ S`-set `Y`, with the diagonal action of `G`, satisfy Higman's criterion relative to `U`
if some `a : Y → ZMod l` has `∑ g, a (g⁻¹ • y) = 1` for every `y`, the sum running over
`(G ⧸ U) ⧸ S`. 

### `exists_diagonalPermModule_isHigmanProjective`

 Let `l` be prime, `U` open normal in the compact group `G`, and suppose every commutator
`⁅z, g⁆` lies in `U`. Then there is a normal subgroup `S` of `G ⧸ U` with the following property.
Let `A` be finite, killed by `l` and fixed by `U`, with `ρ z - 1` injective, and let `Y` be a finite
`(G ⧸ U) ⧸ S`-set. Then the module of functions `Y → A` with the diagonal action of `G` has the
same properties. It satisfies Higman's criterion relative to `U` if some `a : Y → ZMod l` has
`∑ g, a (g⁻¹ • y) = 1` for every `y`, the sum running over `(G ⧸ U) ⧸ S`. 

### `orbitCompl`

 The complement of the orbit of `y` in the `Δ`-set `Y`, as a `Δ`-set. 

### `eq_one_of_prod_quotient.`

 Let `Δ` be a finite group and `f` a function of finite `Δ`-sets with values in `ℚ≥0` that is `1`
on empty sets and has `f Y = f (Y ∖ Δ y) * f (Δ ⧸ Stab y)` for `y` in `Y`. If `X` has a fixed point
`x` and `f (X × Δ ⧸ K) = 1` for all subgroups `K`, then `f (Δ ⧸ K) = 1` for all `K`. 

### `exists_isShortExact_permModule`

 Let `A` be a discrete `G`-module, let `Δ` be a finite group acting on a finite set `Y`, and let
the discrete group `Γ` act through `q : Γ →* Δ`. For a `Γ`-set `X`, `A.permModule X` is the
`G × Γ`-module of functions `f : X → A` with `((g, γ) f) x = g (f (γ⁻¹ x))`. There is a short exact
sequence of these modules from the functions on the complement `C` of the orbit of `y`, to those on
`Y`, to those on the orbit `Δ ⧸ Stab y`. 

### `perm_pow_eq_one_of_map_sub`

 A permutation of an abelian group killed by `n` that preserves differences is a translation, so
its `n`-th power is trivial. 

### `sumValuesHom`

 The sum `a ↦ ∑ g, a g` of the values of a function on a finite type. 

### `hyperplaneAction`

 A finite group `Δ` acts on the functions `Δ → M` by `(g • a) d = a (g⁻¹ * d)`, and this keeps
the sum of the values. This is its action on the hyperplane of functions with the same sum as `e`,
moved to the functions of sum zero by letting `x` stand for `e + x`. 

### `hyperplaneAction_toPerm_apply`

 The value at `d` of the image of `x` under `g`, for the action on the hyperplane through `e`. 

### `hyperplaneAction_toPerm_sub`

 The action on the hyperplane through `e` is affine, and its linear part is the action on the
hyperplane through `0`. 

### `sum_hyperplaneAction_toPerm_apply_one`

 On the hyperplane through `e`, where `y` stands for `e + y`, the sum over `Δ` of the translates
of evaluation at `1` is constant, equal to the sum of the values of `e`. 

### `IsMultiplicative`

 A function `φ` of the modules that are finite, killed by `n` and fixed by `Q`, with `ρ z - m`
injective, is multiplicative: `φ B = φ A * φ D` for every short exact `0 → A → B → D → 0` with `B`
of this kind. 

### `apply_eq_of_equiv`

 Let `φ` be a function of the modules that are finite, killed by `l` and fixed by `U`, with
`ρ z - 1` injective. If `φ` is multiplicative in short exact sequences and `1` on the modules with
Higman's property relative to `U`, then it takes the same value on isomorphic modules. 

### `apply_restrictAlong_eq_of_inv_mul_mem`

 Let `φ` be a function of the modules that are finite, killed by the prime `l` and fixed by `U`,
with `ρ z - 1` injective, that is multiplicative in short exact sequences and `1` on the modules
with Higman's property relative to `U`. If `s t : G → H` agree modulo a normal subgroup `P` killed
by `l`, then the restrictions of an `H`-module along `s` and `t` have the same `φ`. 

### `apply_diagonalPermModule_eq_of_affine`

 Let `φ` be a function of the modules that are finite, killed by the prime `l` and fixed by `U`,
with `ρ z - 1` injective, that is multiplicative in short exact sequences and `1` on the modules
with Higman's property relative to `U`. Let `V` be a finite abelian group killed by `l` with two
actions `α`, `β` of `(G ⧸ U) ⧸ S`, where `α` is additive and `β` is affine with linear part `α`.
Then for a `G`-module `B` the functions `V → B` with the diagonal action of `G`
(`diagonalPermModule`) have the same `φ` for `α` and for `β`. 

### `IsMultiplicative.eq_one_of_eq_one_on_isHigmanProjective`

 Let `l` be prime, `G` a compact topological group and `U` open normal, and let every commutator
`⁅z, g⁆` lie in `U`. Consider the discrete `G`-modules over `R` that are finite, killed by `l` and
fixed by `U`, with `ρ z - 1` injective, and let `φ`, with values in `ℚ≥0`, satisfy `φ B = φ A * φ D`
for every short exact `A → B → D` with `B` of this kind. If `φ B = 1` for every such `B` satisfying
Higman's criterion relative to `U`, that is some additive `τ : B → B` has `∑ g τ g⁻¹ = 1` summed
over representatives `g` of the cosets in `G ⧸ U`, then `φ A = 1` for every such `A`. This is a form
of the known result that the Cartan map has finite cokernel (Serre, Linear Representations of Finite
Groups, §16.1, Theorem 35). 
