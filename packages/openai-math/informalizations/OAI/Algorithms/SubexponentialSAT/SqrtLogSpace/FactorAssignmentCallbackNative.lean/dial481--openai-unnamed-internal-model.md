---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorAssignmentCallbackNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorAssignmentCallbackNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorAssignmentCallbackNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete physical inputs for the streamed factor callback. The source
context is the actual q.ctx, and the dispatcher determines every selected row
and clause. These predicates contain stored words and finite size bounds only.
Their construction from the actual loader/cache run remains an integration step. 

### `fetched`

 Exact selected-payload state produced by the concrete dispatcher. 

### `Input`

 Physical callback boundary, specialized to the source's actual arithmetic
context. In particular no incidence family or evaluator execution is a field. 

### `Input.payload_length`

 A selected record is bounded by the actual serialized master containing
it. This includes the neutral empty payload. 

### `Input.table_frame`

 Source master words survive dispatch and the concrete unary factor-ID
conversion; only the selected payload154 and selected-factor word556 change. 

### `Input.table_ready`

 The actual source-table readiness is derived from fixed physical masters
and the already stored original ID; it is not provided by a caller service. 

### `Input.fetched_hash`

 The hash source bytes are the actual row selected by f, in the unchanged
original raw-row order. No arbitrary raw payload is assumed. 

### `Input.fetched_marked`

 Actual marked-clause bytes retain literal polarity and original variable
IDs; this is the source's clause-violation expression, not its complement. 

### `Input.table_private`

 The table-private boundary is unaffected by the selected payload port. 

### `Input.staged_factorJet`

 The source-table projection uses the current ambient assignment and fixed
high data, exactly as the original source factor does. 

### `Input.staged_correction`

 Correction specialization retains the precise current U word, separately
from the high mask and current-head mask. 

### `Input.payload_correct`

 The exact entries consumed by native arithmetic have the original source
meaning. The byte-injectivity theorem transports denotation without replacing
those entries by another valid representation. 

### `hashBranchBudget`

 The explicit paid ordinary-branch cost, on the exact dispatched state. 

### `hash_callback_eval`

 Actual ordinary dispatch, table production, expansion, indicator,
accumulator multiplication and record return, specialized to q.ctx. 

### `markedBranchBudget`

 Explicit paid cost of the actual marked-clause branch. 

### `marked_callback_eval`

 Actual marked dispatch and clause violation arithmetic, retaining the
very specialized incidence entries returned by the table run. 

### `neutral_callback_eval`

 Neutral original IDs execute their paid record path and preserve the
complete accumulated dictionary. 

### `selected_step_value`

 Dense multiplication for the same selected native factor. The source jet
uses all original factor IDs, but the concrete incidence family is the one
just produced for f; no table for other IDs is constructed or assumed. 

### `hash_step_value`

 The ordinary branch computes the precise original hash selected by f,
followed by multiplication into the same current seed. 

### `marked_step_value`

 The marked branch retains the source clause's violation polynomial and
multiplies it into the same current seed. 

### `callbackBudget`

 The explicit cost keeps every dispatcher scan and every native branch.
It is a proof-side numerical envelope, never a traversal over possible states. 

### `callback_eval_correct`

 The concrete callback produces the exact specialized original factor
value. Its whole raw output, physical frame, paid execution, and arithmetic
meaning refer to one and the same actual execution. 

### `tableBudget`

 Uniform source-table work: the actual staged high-mask word is bounded
by the entry's physical word cap, independently of dispatcher registers. 

### `Input.dispatchBudget_le`

 The actual dispatcher pays for all losing records in both encoded masters. 

### `uniformCallbackBudget`

 The complete per-record bound is fixed before the record scan. Z bounds
only explicit source dimensions, serialized inputs and retained arithmetic
capacity; no evaluator or run is assumed. 

### `callback_cost_polynomial`

 A fixed ninth power bounds the callback's composed numerical envelope.
The degree does not depend on the input or the number of scanned factors. 

### `uniformCallbackBudget_polynomial`

 The only large service terms are the already explicit source and
specialization budgets, inside a fixed power. 
