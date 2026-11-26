---
{
  "module": "src/Lib/SiegelWeil/OneVector/ResidueClasses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/ResidueClasses.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/ResidueClasses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Classes modulo a lattice at a finite place

Let `A` be a finite place, `R` its ring of integers, `κ` an index type, `L` the lattice `R^κ` of
integral vectors in `A^κ` and `g` a unit of `A`.

* `New.Floors.IntegralPlace.latticeMultiple`, `New.Floors.IntegralPlace.residueClass`: the lattice
  `g L` and its classes. They are compact and, for finite `κ`, open of volume `modulus g ^ card κ`.

Notions from other files:

* `New.Floors.IntegralPlace`: the structure `P` that makes `A` a finite place; `P.integers` is the
  ring of integers `R`, and `P.modulus x` is the inverse of the generalised index of `x R` in `R`.


### `latticeMultiple`

 The lattice `g L`, where `L = R^κ` is the lattice of vectors with entries in the ring of
integers `R` of the finite place `A`: the vectors `y` with every `g⁻¹ * y i` in `R`. 

### `mem_latticeMultiple`

 A vector lies in the lattice `g L`, `L` the lattice of integral vectors, exactly when all its
entries, divided by `g`, lie in the ring of integers `P.integers` of the place. 

### `coe_latticeMultiple`

 The lattice `g L`, `L = R^κ`, is the product of copies of the set `g R`, where `R` is the ring
of integers of the finite place `A`. 

### `isCompact_latticeMultiple`

 The lattice `g L`, where `L = R^κ` and `R = P.integers` is the ring of integers of the finite
place `A`, is compact. 

### `residueClass`

 The class `x₀ + g L` of `x₀` modulo the lattice `g L`, where `L` is the lattice of integral
vectors. 

### `isCompact_residueClass`

 The class `x₀ + g L` of a vector `x₀` modulo `g L`, `L` the lattice of integral vectors, is
compact. 

### `isOpen_latticeMultiple`

 For a finite index type `κ`, the lattice `g L` is open, where `L = R^κ` and `R = P.integers` is
the ring of integers of the finite place `A`. 

### `volume_latticeMultiple`

 For a unit `g` of the finite place `A` and the lattice `L = R^κ` of integral vectors, the
lattice `g L` has volume `modulus g ^ card κ`; here `modulus g` is the volume of `g R`. 

### `isOpen_residueClass`

 The class `x₀ + g L` of a vector `x₀` modulo `g L`, `L` the lattice of integral vectors, is
open when the index type is finite. 

### `volume_residueClass`

 For a unit `g` of the finite place `A` and the lattice `L` of integral vectors, each class
`x₀ + g L` has volume `modulus g ^ card κ`; here `modulus g` is the volume of `g R`. 
