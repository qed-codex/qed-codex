---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite control for the bitonic phase and stride loops

Start with one unary mark for each bit of the global wire address. Each
outer pop advances the phase. A preserved copy of the new phase drives
the inner loop, which presents the exponents in descending order. The
layer routine sees the actual unary phase and stride while it works on
the site's bit stacks.


### `Control`

 Unary loop counters and scratch stack for the phase and descending-stride loops of bitonic
sorting. 

### `Port`

 Sorting schedule registers formed from the loop-control stacks and the caller's layer
registers. 

### `bank`

 Initialize the remaining, phase, and stride stacks with unary marks, clear the temporary
stack, and retain the caller's data. 

### `program`

 The stage counter lives on four bit stacks. Only the finite layer
control is incorporated into the surrounding transition table. 

### `LayerRuns`

 The callback updates its data and preserves the phase and stride ports. 

### `runs`

 From the initial unary global width, run every prescribed layer once
in chronological order. No address-width-dependent transition table is used. 

### `Visits`

 A bounded execution of each callback on the successive actual buffers.
This version permits callbacks whose run depends on having the appropriate
send and receive blocks at the front of the stream. 

### `future`

 The unvisited phase suffix after finishing phase `a`. 

### `runs_of_visits`

 Each callback need only run on the state it actually receives. 

### `Visits.of_stream`

 Compose stage computations that consume a chronological suffix of the
incident stream. Local stages take an empty prefix. The final stage returns
whatever tail the caller placed after the sorting fields. 
