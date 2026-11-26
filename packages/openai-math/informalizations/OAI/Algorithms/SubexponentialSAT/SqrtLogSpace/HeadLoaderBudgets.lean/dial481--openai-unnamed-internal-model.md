---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadLoaderBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadLoaderBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadLoaderBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed polynomial bounds for the actual head loader from its retained
source words. Column time is derived from the native integer-entry program;
the outer loop's address is charged by its actual unary word length. 

### `sizeCoefficient`

 This constant is independent of the input and all runtime parameters. 

### `preparationSize_le`

 The source bank includes the ambient/factor counters, the complete row
word, low mask, native metadata and the integer-arithmetic widths. 

### `workSize_le`

 No column evaluator or successful running-time witness is assumed.
The actual native column budget follows from the physically stored inputs. 

### `localWork_le`

 The local native budget has a fixed degree, even when the outer scan
visits exponentially many assignments. It bounds each load independently. 

### `leafWork_le`

 Paid address staging, import, export and cleanup have the same degree64
envelope. The resource use of the outer repeated run remains a separate bound. 
