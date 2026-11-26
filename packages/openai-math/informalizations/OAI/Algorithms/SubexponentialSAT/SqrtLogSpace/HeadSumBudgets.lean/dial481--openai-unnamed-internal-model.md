---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit compact boundary, source and arithmetic caps for the actual head
sum. Their fixed polynomial certificates depend on source dimensions and
physical word lengths, independently of the number of head assignments. 

### `compactCap`

 The boundary accommodates existing words, a regenerated ring cache and
any specialized dictionary returned by a factor. 

### `tableScalarCap`

 Includes the physical staging cap as well as every ordinary source scalar. 

### `arithmetic_caps`

 The actual indexed hash rows and marked clause use the same chosen Z. 

### `caps_polynomial`

 All chosen capacities and the per-assignment time coefficient have fixed
polynomial growth. The constants precede the physical input cap. 

### `addressed_source_word_caps`

 The actual addressed constructor uses canonical polynomial-width word(s).
The denominator value may be exponential; only its physical binary length
appears in this statement. No arbitrary padding premise is required. 

### `produced_source_word_caps`

 These are the very source parameters built from the produced ring and
addressed query input. The bound follows the constructor's physical word(s). 
