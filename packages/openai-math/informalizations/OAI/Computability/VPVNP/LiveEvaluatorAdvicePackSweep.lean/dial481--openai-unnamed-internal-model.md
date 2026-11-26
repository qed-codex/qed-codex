---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdvicePackSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native sweeps for packing the evaluator's bit banks

Each output row begins with one reset call. Further calls install the row's
occupied source bits and leave its padding zero. The resulting memory is
specified at every address. Every nonempty sweep has a single accepting
branch stream and incurs at most four calls-plus-probes per cursor.


### `packControl`

 The cursor for an unfinished call, or the halted control after all rows. 

### `deterministic_scan`

 The reported memory, call count, clock and total probe cost of a native
deterministic scan, with an exact characterization on arbitrary branch streams. 

### `packMemory`

 Each row is overwritten when its reset call occurs. Subsequent calls in
the same row expose one more little-endian bit, up to the fixed field width. 

### `packCalls`

 Number of native calls, including the initial reset of every row. 

### `PackLayout`

 The public geometry and the word bounds used for packing. Addresses are
ordinary naturals until they are shown to fit in a native word. 

### `PackSource`

 Source advice occupies one Boolean word at each actual bit address. 

### `packMemory_full`

 At the end all row words are fully written, even if padding calls have
been needed after the end of the raw advice. 

### `pack_index`

 On a nonreset column the live source offset is the ordinary row-major
bit index. All arithmetic in the native registers stays within the modulus. 

### `packMemory_step`

 The natural row-prefix invariant advances exactly once for the native
reset, active bit, or padding call. 

### `packStep_guards`

 The valid natural cursor satisfies both native guards, and its footer
publishes the next ordinary cursor unless the complete scan has ended. 

### `packSweep`

 All accepted runs of the actual packed-advice program, including streams
of unintended lengths or surplus bits, with exact final memory. 

### `packSweep_zero`

 A zero-row interval takes zero calls. Its starting cursor and memory are
available to the next phase. 

### `packPathCount`

 The nonempty advice sweep contributes exactly one native path under the
paper's per-call and global transcript caps. 
