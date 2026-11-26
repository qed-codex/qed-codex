---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramUnary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramUnary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramUnary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Production sparse-code parameter program. Fixed arithmetic, minimum,
metadata identities and unary materialization are checked in one unit. 

 Arithmetic identities used by the physical sparse-code parameter program. 

### `dimensionFor_eq_size`

 The minimal graph dimension is computed by one division and a binary size,
including the one-vertex case. No unbounded semantic search is needed by the
physical parameter program. 

### `size_eq_log2_odd`

 A branch-free implementation of binary size using the existing positive
logarithm primitive. 

 A concrete minimum operation used between two straight-line arithmetic
stages. The comparison consumes only two explicitly copied temporary words. 

 Fixed finite arithmetic instructions for all sparse-code search metadata.
Ports 0 and 1 contain m and B. Outputs: q=5, D=9, t=11, tD=12,
local distance=15, r=18, rD=19, N=21. Unary conversion is a separate,
explicitly paid stage. 

### `final_search_lengths`

 The actual binary search words have length linear in the lengths of the
input metadata, independently of their numeric values. 

### `command_eval`

 Execute the fixed arithmetic table and the concrete minimum comparator.
All copy, division, logarithm and exponentiation costs are included. 

 Explicit paid binary-to-unary copies for code-search metadata. 

### `unaryPairs`

 Each pair is (binary source, unary destination). Binary source words are
retained. Destination slots24--30 and temporary slot62 start empty. 

### `parameterValues_le`

 Unary materialization is paid by numeric value. All seven values are
polynomial in the original number of violation coordinates, even when B is
large. In particular the vertex count is not charged merely by bit length. 
