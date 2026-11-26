---
{
  "module": "OAI/Computability/VPVNP/TwoMarkedTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transporting two marked tensor indices

The two marked factors in Appendix A.3 may be placed at coincident parties.
To relocate one of them, keep the other as part of the background basis.
The two regroupings preserve every coefficient.


### `twoMarked`

 An array with a marked row at `a` and a marked column at `b`. 

### `holdSecond`

 View the second marked leg as part of the background. 

### `holdFirst`

 View the first marked leg as part of the background. 

### `twoMarked_wire_mutual`

 With trivial background and the identity coefficient table, the two
marked legs give the equality wire at their chosen parties. 

### `twoMarked_independent_bound`

 Combining first-index and second-index relocation bounds gives the four
independent endpoint weights of (A.4). 

### `SpectralPoint.value_twoMarked_atFraction_le`

 Equation (A.4). Relocation of each mark bounds the value at the two
fractional points by the independent product of all four endpoint values. 
