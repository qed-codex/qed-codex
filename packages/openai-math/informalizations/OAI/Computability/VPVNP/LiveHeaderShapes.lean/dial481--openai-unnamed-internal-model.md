---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderShapes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderShapes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderShapes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Field intervals for the live incident cuts

In the unit mode all nonmode bits form a single zero-padding interval.
In the simulation mode the cut carries the exterior and exponents up
to and including the midpoint, then the evaluator configuration. Missing
cuts and empty payloads have no sites to visit.


### `Side`

 The incoming left or outgoing right side of the group whose incident cut is being parsed. 

### `Field`

 The payload or padding interval requested from a live incident cut. 

### `Shape`

 The cut formats governing field lengths, covering absent endpoints, unit mode, paired
computation, and evaluator tail. 

### `shape`

 The first tail group's left cut is the midpoint, so it still has the
pair layout even though the group's own mode dispatch chose the tail. 

### `cutIndex`

 The index of the left or right incident cut of a one-based group. 

### `shape_at_group`

 The index-based flag dispatch produces the layout of the incident cut
itself. In particular the group just after the midpoint has different
layouts on its two sides. 

### `exterior`

 Natural-number lengths for the three payloads, in their physical order. 

### `exponents`

 The occupied exponent length for a cut shape, equal to the supplied exponent size on a pair
cut. 

### `config`

 The occupied configuration length for a cut shape, equal to the supplied configuration size
on a tail cut. 

### `mode`

 The length occupied by the leading mode bit, zero at a missing cut and one on a nonempty
cut. 

### `start`

 The offset of the requested field after the mode bit and preceding enabled payloads. 

### `count`

 The occupied length of the specified field, assigning the remainder of the cut to padding. 

### `span`

 No source address is used for an empty field; its offset word is zero. 

### `payload_le`

 The largest nonpadding prefix ends at or before the cut boundary. 

### `partition`

 After the mode bit these four consecutive fields cover every site. 

### `span_fit`

 Every emitted interval lies inside the supplied cut. 

### `width_ge_block`

 Every nonempty cut has at least one full block under equation (9.1). 

### `pair_exterior`

 A pair-layout outgoing live cut carries exactly the primed exterior
at twice its index, including the midpoint where that exterior is empty. 

### `midpoint_exterior`

 At the middle cut the exponents start immediately after the mode. 
