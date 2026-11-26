---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Burst RAM interval intersection

A fixed instruction table intersects a candidate pair of fields from Appendix E.
The persistent word points to a frame with four input words and three output
cells. The table reads the two starts and widths. A nonempty intersection writes
two offsets and a length. An empty intersection returns zero after the four reads.


### `pairTemplate`

 Labels 17–28 load the frame. Labels 0–16 select the larger start and
smaller end and skip all three writes when the intersection is empty. 

### `resultReport`

 The native events prescribed by the descriptor. Source and target offsets
are written only when the interval contains a bit. 

### `execute_slice`

 From label zero, the table executes the pair test with fields already loaded. 

### `resultReport_cost`

 Three probes and thirteen nonterminal instructions suffice for a nonempty
copy. A disjoint pair takes eight nonterminal instructions and zero probes. 

### `frameAddress`

 Consecutive cells of a seven-word frame, with the burst machine's modular addresses. 

### `frameAddress_val`

 Every cell of a frame fitting the address space has its ordinary consecutive address. 

### `frameHolds`

 The four input words of a candidate test in a caller's memory. 

### `frameReport`

 Exact report for the whole candidate call, including its frame reads. 

### `execute_candidate`

 Fresh-call execution for every field pair of the source-major scan. The
two bounds on total widths suffice for all its endpoint additions. 

### `frameReport_cost`

 The frame contributes four reads and twelve instructions. The final
return costs one instruction in both cases. 

### `frameReport_after`

 Replay gives exactly the three specified writes for a nonempty interval
and preserves memory on the empty branch. 

### `scan_cost`

 Exact cost of all candidate-test calls. Memories can differ from one
call to the next. Each report is native under the frame invariant of
`execute_candidate`. The cost depends only on field and record counts. 

### `fieldOps`

 One step of `fieldsFrom` with the width in external memory. Registers
0 and 1 carry the index and prefix sum. Register 2 supplies the width address
and registers 3–5 supply the index, start and width output addresses. 

### `fieldOps_trace`

 The prefix scan reads one width, writes one indexed descriptor and
advances both running totals. 

### `fieldOps_native`

 Numeric field and next prefix computed by the straight-line native code,
under the usual index and address-width bounds. 

### `scan_bounds`

 The two prefix scans plus all interval tests use a width-independent
number of word instructions and probes. This accounts for the prefix steps
and the candidate calls with their input frames in place. 
