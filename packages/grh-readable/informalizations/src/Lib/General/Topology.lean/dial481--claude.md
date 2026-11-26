---
{
  "module": "src/Lib/General/Topology.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Topology.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Topology.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Open subgroups, a tube lemma, and procyclic images of ℓ-adic characters

This file collects auxiliary facts from topology and algebra. It characterises congruence modulo a
principal ideal `(a)` by divisibility of the difference by `a`.

## Main definitions and results

* `IsCompact.eventually_forall_mem`: a form of the tube lemma for a jointly continuous map of two
  variables, with the continuity hypothesis discharged by `fun_prop` by default.
* `New.Selmer.exists_procyclic_generator`: a continuous character of a compact group with values in
  1 + 4ℤ_ℓ has procyclic image.
* `MonoidHom.IsGeneratorModKer`: an element generates a topological group modulo the kernel of a
  homomorphism; `New.Selmer.exists_isGeneratorModKer` gives one for such a character of a profinite
  group.


 ## Open subgroups, a tube lemma, and congruence modulo a principal ideal 

### `Subgroup.IsOpen`

 The subgroup U of G is an open subset of G. 

### `IsCompact.eventually_forall_mem`

 Tube lemma for a jointly continuous f: if W is a neighbourhood of f(x₀, y) for each y in a
compact set K, then f(x, y) ∈ W for all y in K and all x near x₀. 

### `Ideal.mk_span_eq_iff_dvd_sub`

 Two elements x and y have the same class modulo the principal ideal (a) if and only if a divides
x − y. 

 ## Procyclic images of ℓ-adic characters of compact groups 

### `ZMod.index_zpowers_unitOfCoprime_five`

 The powers of 5 form a subgroup of index 2 in (ℤ/2^(k+2))ˣ. 

### `New.Selmer.exists_isCyclic_range_toZModPow`

 A continuous character κ of Γ with values in 1 + 4ℤ_ℓ admits a continuous character μ with
ker μ ≤ ker κ whose image modulo every ℓ^(k+2) is cyclic: κ itself for odd ℓ, κ² for ℓ = 2. 

### `New.Selmer.exists_procyclic_generator`

 Let ℓ be a prime and κ a continuous homomorphism from a compact group Γ to ℤ_ℓ^× with values in
1 + 4ℤ_ℓ (for odd ℓ this is no condition, as 4 is a unit of ℤ_ℓ; for ℓ = 2 it keeps κ away from
−1). Then κ has procyclic image: for some γ, every open subgroup S that contains γ and ker κ is all
of Γ. 

### `MonoidHom.IsGeneratorModKer`

 The element γ generates Γ modulo the kernel of κ: the only closed subgroup that contains γ and
ker κ is Γ. 

### `MonoidHom.IsGeneratorModKer.inv`

 If γ generates Γ modulo the kernel of κ, then so does γ⁻¹. 

### `MonoidHom.IsGeneratorModKer.exists_mul_eq`

 Let γ generate the compact group Γ modulo the closed kernel of κ. Then every g is a product
h q with h in ker κ and q in the closure of the powers of γ. 

### `MonoidHom.IsGeneratorModKer.pow_sub_one_dvd`

 If γ generates Γ modulo the kernel of a continuous character κ with values in ℤ_ℓ^×, then
κ(γ)^a − 1 divides κ(g)^a − 1 for every g. 

### `New.Selmer.exists_isGeneratorModKer`

 A profinite group has a generator modulo the kernel of a continuous character with values in
1 + 4ℤ_ℓ. 
