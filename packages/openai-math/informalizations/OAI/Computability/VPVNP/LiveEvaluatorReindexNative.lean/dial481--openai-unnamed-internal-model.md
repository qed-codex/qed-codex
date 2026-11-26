---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindexNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scatter of dense exponent bits into the initial evaluator tape

The incoming cut stores one bit per word, in dense label order and
least-significant digit first. The map table gives the formal evaluator label
of each dense label. On the evaluator tape the exponent payload is in reverse
order and one delimiter separates consecutive payload symbols. A native call
reads one bit and one map entry, and writes exactly one tape symbol.


### `scatterOps`

 Public words are the incoming bit base, label-map base, first exponent
payload symbol address, bits per label, and total number of payload bits. 

### `incomingAddress`

 The source address of one serialized exponent bit on the incoming cut. 

### `mapAddress`

 The address of the formal label ordinal corresponding to the dense exponent row containing
this bit. 

### `formalBit`

 The bit index in formal label order, combining the mapped label ordinal with the bit's
within-row position. 

### `targetAddress`

 The bit's destination in the reverse-ordered evaluator tape payload, accounting for the
interleaved delimiter cells. 

### `inputSymbol`

 Encode the incoming exponent bit as a nonblank evaluator tape symbol by adding one. 

### `scatterEvents`

 The two reads precede the write, so the read values are both from the
memory at entry. All arithmetic and cursor updates produce ticks. 

### `targetAddress_val`

 With a valid formal bit number, its product and digit addition fit a
word. The two subtractions are in increasing distance from the right end. 

### `scatterPhase`

 The phase enters through a cursor check. A completed final write
accepts in the same burst. On an empty array the initial call accepts
without accessing either array or the destination tape. 

### `phaseEvents`

 Three entry ticks and a final cursor test surround the two reads and
one write of the scatter block. 

### `execute_phase_active`

 Exact execution of the entire native phase on every active cursor and
choice stream. A nonterminal call returns the next cursor. 

### `execute_phase_empty`

 A zero-capacity phase at its initial cursor consumes no choices and
does no memory operations. 

### `execute_phase_past`

 Positive out-of-range cursors cannot accept the phase. 

### `scatterPhase_segment`

 A complete native scatter sweep. Every nonempty row contributes its
payload calls, with the final call accepting. The empty sweep uses its
single accepting entry check and preserves the initial memory. 

### `scatterPhase_choices`

 An accepting run from any cursor consumes exactly its remaining calls,
each with the empty choice stream. This includes runs of arbitrary
proposed lengths and establishes uniqueness of the initialization path. 
