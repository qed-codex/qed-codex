---
{
  "module": "src/Lib/General/Algebra/AbsIntegrallyClosed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/AbsIntegrallyClosed.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/AbsIntegrallyClosed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Absolutely integrally closed rings and their stability properties; Frobenius powers

* `New.Variety.frobPow`: the ring endomorphism `x ↦ x ^ p ^ f`, for a prime `p` with `p = 0` in
  the ring.
* `New.Variety.IsAbsIntegrallyClosed`: every monic polynomial of positive degree has a root (the
  ring need not be a domain).
* The property passes to subrings that are integrally closed in the ring
  (`New.Variety.IsAbsIntegrallyClosed.of_isIntegrallyClosedIn`), to quotients
  (`New.Variety.IsAbsIntegrallyClosed.of_surjective`) and to localisations
  (`New.Variety.IsAbsIntegrallyClosed.of_isLocalization`). For a field it means algebraically
  closed: algebraically closed fields have it by an instance, and
  `New.Variety.IsAbsIntegrallyClosed.isAlgClosed` gives the converse.
* `New.Variety.IsAbsIntegrallyClosed.exists_root_map_eq`,
  `New.Variety.IsAbsIntegrallyClosed.mem_range_of_isIntegralElem`: for `f : A →+* B` from an
  absolutely integrally closed ring into a domain, roots in `B` of monic polynomials over `A` lift
  to roots in `A`, so integral elements lie in the image.


### `frobPow`

 The ring endomorphism `x ↦ x ^ p ^ f` of a commutative ring `B` in which the prime `p` is
zero. 

### `IsAbsIntegrallyClosed`

 `A` is absolutely integrally closed: every monic polynomial over `A` of positive degree has a
root in `A`. 

### `IsAbsIntegrallyClosed.exists_root`

 Every monic polynomial over `A` of positive degree has a root in `A`. 

### `instance [IsAlgClosed K] : IsAbsIntegrallyClosed K`

 An algebraically closed field is absolutely integrally closed. 

### `isAlgClosed`

 A field that is absolutely integrally closed is algebraically closed. 

### `exists_eval₂_eq_zero`

 If `A` is absolutely integrally closed and `f : B →+* A` is a ring map, then every monic
polynomial over `B` of positive degree has a root in `A` along `f`. 

### `of_isIntegrallyClosedIn`

 If `A` is absolutely integrally closed and `B` is integrally closed in the `B`-algebra `A`
(in particular `B → A` is injective), then `B` is absolutely integrally closed. 

### `exists_root_of_coeffs_subset_range`

 Let `A` be absolutely integrally closed and `f : A →+* B` a ring map. A monic polynomial over
`B` of positive degree whose coefficients lie in the image of `f` has a root in `B`. 

### `exists_pow_eq`

 In an absolutely integrally closed ring, every element has an `n`-th root for `n ≠ 0`. 

### `exists_pow_sub_mul_eq`

 In a nonzero absolutely integrally closed ring `A`, for `n > 1` and any `c`, `b` in `A`, the
equation `x ^ n - c * x = b` has a solution `x` in `A`. 

### `of_surjective`

 If `A` is absolutely integrally closed and `f : A →+* B` is a surjective ring map, then `B` is
absolutely integrally closed. 

### `of_isLocalization`

 A localization `B` of an absolutely integrally closed ring `A` at a submonoid is absolutely
integrally closed. 

 ### Maps to a domain 

### `exists_root_map_eq`

 Let `A` be absolutely integrally closed, `f : A →+* B` a ring map to a domain, and `P` a monic
polynomial over `A`. Every root `x` in `B` of the image of `P` is `f a` for some root `a` of `P`
in `A`. 

### `mem_range_of_isIntegralElem`

 If `A` is absolutely integrally closed and `f : A →+* B` is a ring map to a domain, then every
element of `B` that is integral along `f` lies in the image of `f`. 
