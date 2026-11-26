---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordScores.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordScores.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordScores.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the common layout from two word counters

In the second descriptor scan of Appendix E, each term contributes its squared supply
widths to two totals. Clearing the fixed denominators yields nonnegative integers, and
the common positive arc mass cancels. One native word block accumulates an edge's
contribution with two probes. One comparison of the two counters picks the same layout
as the real energy comparison of §7.2, including the tie case.


### `layoutScore`

 Integral score accumulated for the selected payloads in one layout. 

### `selectLayout`

 The finite program chooses `true` only on strict improvement. 

### `accumulateScore`

 Register 0 holds the score address, 1 the integer weight and 2 the payload width.
Registers 3 and 4 are temporaries. The same code updates either layout score. 

### `scoreWord_exact`

 A word counter gives the exact natural score while the final sum fits in one word. 

### `accumulateScore_native`

 The exact finite opcode table realizes the score update from supplied registers. 
