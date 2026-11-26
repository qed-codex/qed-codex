---
{
  "module": "OAI/Computability/VPVNP/SharpPowerObstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpPowerObstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpPowerObstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Balanced layout comparison with polynomial overhead in the power

An encoding of length `A * (h+1)^D * q^h` gives the central wire exponent `C`
when the source circuit budget is `n^C`. The polynomial in `h` can be retained
as a common factor in the finite sum, since each bridge distance is at most one.
The strict layout gap absorbs this factor at all sufficiently large powers.


### `not_small_universal_of_sharp_projections`

 The source budget exponent enters the layout cost unchanged when the
projection length is linear in the terminal dimension up to polynomial factors in
the power `h`. 
