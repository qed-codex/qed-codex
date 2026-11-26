---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFactorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete factor-row evaluation primitives

Programs in this module have fixed Boolean registers and fixed finite control.
Inputs are working copies on stacks. All costs below are actual instruction
traces; neither arithmetic comparisons nor semantic predicates are instructions.


### `unary_validity_iff`

 A padded little-endian label is below `2^b` exactly when all bits beyond
its `b` low bits are zero. No comparison is being assigned unit cost. 

### `program`

 Consume a bit word and output whether every bit is zero. 

### `primitive_outputs`

 The fixed program runs on the primitive machine with its proved overhead. 

### `evalPairs_clause`

 A row stream contains the actual sign and looked-up variable bit for each
literal. Producing the looked-up bits is a separate caller operation. 

### `program`

 A fixed-control evaluator for interleaved sign/value row data. 

### `primitive_clause`

 The actual fixed program computes clause truth once the caller supplies
the sign/value row stream, including the empty-clause case. 

### `eval`

 Actual unary validity evaluation. The width is data on a separate unary
counter stack; the label is a padded little-endian bit word. 

### `unary_matches_factor`

 The numeric predicate computed by the unary program is exactly the
constructed prime-label factor's acceptance condition. 

### `factorTable_on_encoding`

 On a valid encoded row, the finite source search returns the source table
value. This is semantic justification, not a unit-cost execution premise. 

### `primitive_clause_factor`

 The signed-bit program computes an actual constructed clause factor on
valid encoded labels. The input stream consists of the explicitly supplied
decoded values for that clause's literals. 
