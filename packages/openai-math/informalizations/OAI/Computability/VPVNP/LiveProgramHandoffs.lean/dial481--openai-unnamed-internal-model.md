---
{
  "module": "OAI/Computability/VPVNP/LiveProgramHandoffs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramHandoffs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramHandoffs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact transfers of the outer live router

At a jump, the continuation runs with cursor zero in the newly tagged
memory. An accepting router contributes exactly one path if its own report
fits the cap. These statements apply at a common group clock and keep every
report from the deterministic dispatch and flag test.


### `jumpReport`

 Router report for a selected jump. It reads the flag, tests the indicated branch, writes
the destination tag, and returns cursor zero. 

### `haltReport`

 Accepting router report consisting of the flag read and the tests through the selected
branch. 

### `outerReport`

 Wrap the router’s own report with the live stage linker’s dispatch and exit events at the
outer stage-tag address. 

### `outer_jump_probes`

 A jump costs one tag read in the linker and a read and write in the router. 

### `outer_halt_probes`

 A terminal route reads the two tags and writes no word. 

### `jump_call`

 The actual choice-free jump at the group's common clock. 

### `jumpEquiv`

 Exact all-path transfer after a successful first-tail, last-tail, or pair
selection. The tag write is the only change in external memory. 

### `unit_accept_iff`

 A checked unit-mode flag finishes the group at the router, with exactly
one possible choice stream consisting of a single empty call. 
