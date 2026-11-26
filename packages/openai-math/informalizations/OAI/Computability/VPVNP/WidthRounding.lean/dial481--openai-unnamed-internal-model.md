---
{
  "module": "OAI/Computability/VPVNP/WidthRounding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WidthRounding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WidthRounding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer wire widths in the shrinking step

Section 7.2 of *VP and VNP differ over every field* divides a bundled wire
into equal-mass slots. An integral width `b` splits into slots of widths
`b / q` and `b / q + 1`. The excess in the sum of squares is exactly
`r * (q - r) / q`, where `r` is the remainder, and hence is at most `q / 4`.


### `splitWidth`

 The first `b % q` slots receive the extra bit. 

### `sum_splitWidth`

 Concatenating the split payloads recovers exactly the old bit count. 

### `sum_splitWidth_sq`

 Exact sum of squared widths, expressed as the fractional optimum plus the
rounding error. 

### `sum_splitWidth_sq_le`

 The error from rounding all the widths is at most one quarter per slot. 

### `splitWidth_energy_le`

 With mass `p` per slot, the energy penalty for integral splitting is at
most `q / (4*p)`. This applies to both subdivisions in Section 7.2. 
