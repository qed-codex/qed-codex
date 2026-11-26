---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/SphereFibres.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/SphereFibres.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/SphereFibres.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The spheres of ℂ^κ as fibres of the standard form

* `New.Floors.exists_isDisintegration_le_sphereDensity`: in rank at least two, the volume of ℂ^κ
  disintegrates along y ↦ y* y into a measurable family of measures on the spheres, whose mass on a
  box is bounded.

Notions from other files:
* `New.Floors.Place.IsDisintegration`: a family of measures, indexed by the skew scalars, whose
  integrals of compactly supported continuous functions are finite and continuous in the index and
  which integrates over the index to a given measure, the index recording the value of a form.
* `New.Floors.lintegral_eq_polar`: polar coordinates on ℂ^κ by the unitary group. The squared norm
  r has density `sphereDensity k r / 2`, where `sphereDensity k r` = 2 π^k r^(k-1) / (k-1)!.

## Relation to the literature
Elementary: polar coordinates.


### `lintegral_eq_lintegral_two_mul`

 Substitution of `r = 2 t` in a Lebesgue integral over the real line. 

### `re_star_dotProduct_self_le`

 If the entries of a vector of ℂ^κ have modulus at most R, then its squared norm is at most
|κ| R². 

### `exists_isDisintegration_le_sphereDensity`

 Let κ have k ≥ 2 elements. Over the complex place the volume of ℂ^κ disintegrates along the
standard form y ↦ y* y into an s-finite kernel l from the skew (purely imaginary) numbers β to ℂ^κ:
the integral of f (y* y, y) over the volume is the iterated integral of f (-2 i β, y) against l β
and then β, and for continuous compactly supported g ≥ 0 the integral of g against l β is finite
and continuous in β. Moreover the mass that l β gives to the vectors with entries of modulus at
most R is at most `sphereDensity k (k R²)`, where `sphereDensity k r` = 2 π^k r^(k-1) / (k-1)!. 
