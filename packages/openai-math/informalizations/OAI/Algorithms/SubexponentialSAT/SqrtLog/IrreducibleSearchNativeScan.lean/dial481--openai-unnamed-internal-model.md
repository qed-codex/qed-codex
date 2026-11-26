---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchNativeScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchNativeScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchNativeScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native irreducible-polynomial search: concrete factor callbacks,
saved universal scans, exact ordered candidate selection, and measured cost. 

 A fixed factor-pair callback and universal scan. All checker arithmetic,
record extraction, array splitting, and cleanup use explicit bit programs. 

### `factorTest`

 This observer labels executions on valid records. The program never calls
it: the preceding measured arithmetic proof establishes the label. 

### `factorRecords_generated`

 The factor-list input to the universal scan is itself produced by the
same fixed ordered generator, at the supplied runtime depth `2(d+1)`. 

 Fixed first-success scan using the concrete saved factor checker. 

### `candidateTest`

 A mathematical observer for the proof; every executed test is the concrete
factor-scan callback above. 

### `searchCost_nodeBound`

 Ancillary estimate under a stronger field-size premise. The implemented
`Nat.size Q + 1` degree uses `searchCost_sizeDegreeBound` below. 

### `searchCost_sizeDegreeBound`

 The implemented degree is `Nat.size Q + 1`; its proved field-size bound
is quadratic in `Q + 1`, giving degree ten for the search. 

### `primitiveCost`

 The translation overhead is one fixed constant, because the program has
no dimension-dependent code. All dimension data live on input stacks. 
