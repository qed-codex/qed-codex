---
{
  "module": "src/Lib/ClassField/Global/Chebotarev.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/Chebotarev.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/Chebotarev.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chebotarev: Frobenii at primes of degree one in every nonempty open set

The qualitative form of Chebotarev's theorem used in the proof: `New.chebotarev`. It is reduced to a
cyclic extension, where it follows from the second inequality `New.second_inequality`.

Notions from other files:
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.IsPlaceOver`: `IsPlaceOver A v` says that the valuation subring `A` of `Ω` lies over the
  prime `v` of `K`: an integer of `K` is in the maximal ideal of `A` exactly when it lies in `v`.

## Relation to the literature

Known result: Chebotarev's density theorem, existence form. Only existence is proved, namely that
Frobenius elements at primes of degree one outside a finite set are dense in the absolute Galois
group, and no density value is given. Source: J. S. Milne, Class Field Theory, VIII 7.4 (Deuring's
reduction); Stevenhagen–Lenstra, Chebotarëv and his density theorem, Math. Intelligencer 18 (1996).


### `New.chebotarev`

 Chebotarev's theorem, existence form (no density is given). Let `W` be a nonempty open subset of
the absolute Galois group `Gal(Ω/K)` of the number field `K`, and `S` a finite set of finite places
of `K`. Then (a) some place `v ∉ S` has prime norm `v.q` (the size of its residue field), with a
place `A` of `Ω` over it (a valuation subring, `New.IsPlaceOver`); (b) some arithmetic Frobenius
at `A` for `v.q` lies in `W`; (c) every arithmetic Frobenius at `A` for `v.q` lies in `W`. 
