---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineTraceInverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineTraceInverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineTraceInverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Completeness of the physical online descriptor trace

At an active ordinal the fixed calendar must emit the current row, and every
successful data call is governed by its worker's invariant. Each extracted
row consumes the three control calls and its closing call. Induction on the
remaining physical calls therefore recovers all rows from an arbitrary
accepting path, including schedules with no active rows. The equivalence
keeps the path's original list of branch tapes and hence its multiplicity.


### `RowInvariant`

 At each reachable calendar boundary, supply the physical row's frame
and single-call invariant. On completion of that source row the next memory
again satisfies the boundary invariant. 

### `RowInvariant.next`

 Recover the phase, worker, and execution bounds for the next live row from the memory
  invariant. 

### `recover_trace`

 Recover every chronological source row and its exact native reports.
Induction on the supplied stream length does not require a bound on the
number of selector choices available to a worker. 

### `RowTapes`

 A tape list and its resource predicate can be checked on the actual
chronological rows. Different proofs of row invariants carry no path weight. 

### `acceptedEquiv`

 Bijection between accepting online program paths and valid row tapes satisfying the same
report filter. 
