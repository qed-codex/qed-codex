---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The persistent physical boundary for the actual high-assignment loop.
The ring, source and parked layout words are produced once for this query and
retained across each rank. No execution or evaluator is part of this invariant. 

### `preparedPorts`

 The node index, coefficient stream and decoded current-high assignment
are regenerated at each rank; the remaining prepared words are unchanged. 

### `parked_mem`

 The actual parked layout lies entirely in the repeated high-loop frame. 

### `arithmetic_mem`

 All arithmetic words consumed by the concrete node constructor are static
between high assignments. 

### `prepared_input_caps`

 The source-local cache cap stays fixed across all high assignments;
transient caller storage is not fed into the next node's source cap. 

### `initialized_prepared`

 The actual seed does not alter any prepared ring, source or layout word. 

### `copied_prepared`

 Refreshing the reusable lower counter retains the same prepared words. 

### `advance_prepared`

 The genuine odometer changes only its counter and scratch words. 

### `mass_prepared`

 Actual native count addition leaves every prepared input word intact. 

### `mass_eval_prepared`

 The same static words survive the actual native addition trace. 

### `branch_prepared_of_stream`

 This is the physical frame join around a concrete fixed-stream run.
The stream's actual word equalities are retained through the real adder. 

### `prepared_frame_stable`

 A pure physical word frame is stable under the real high odometer.
Its logical assertion contains no code, successful layout or query oracle. 

### `kept_disjoint`

 Kept caller words are disjoint from the concrete high controller's
reusable counter and mass-adder words. This includes the parked blank767. 

### `kept_frame_stable`

 The complete caller frame can be carried by the same pure loop invariant. 

### `mass_eval_kept`

 Actual native addition preserves the full caller frame, not only the
arithmetic words required by the next conditioned query. 

### `branch_kept_of_stream`

 The real copy, fixed query, guard restoration and native adder retain the
same caller words as the actual stream; no global space cap proves this frame. 

### `prepared_seed_entry`

 The concrete prepared-and-seeded run starts at the empty count and the
single zero tuple, even when there are no high coordinates. 

### `complete_frame_stable`

 The complete high-loop invariant combines only literal word equalities.
Both frames survive the actual odometer and the paid initial guard. 

### `compact_width`

 The high counter and exact accumulator fit the compact boundary from
an independent ambient source cap. No prefix allowance enters this bound. 

### `prepared_parked`

 Every rank reads the layout physically produced by this same preparation. 

### `prepared_arithmetic`

 The arithmetic witness is the actual preparation output, with unchanged
physical cache words at each repeated branch boundary. 

### `prepared_nodes`

 Both node serializations remain the ones emitted by the same ring run. 

### `prepared_mask`

 A repeated branch retains this query's own computed high set. 

### `prepared_sources`

 Literal source and current-marker inputs at every rank follow from the
same frontend execution and original readiness, rather than a supplied source. 

### `run`

 Actual complete enumeration of the fresh high set. Every rank invokes the
fixed streamed query, and the same run accumulates the full source count.
The input word and scalar caps are physical preparation bounds; no evaluator,
layout service, branch execution, or repeated-loop bound is assumed. 
