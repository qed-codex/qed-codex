---
{
  "module": "OAI/Computability/VPVNP/RAMSortCompareCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCompareCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCompareCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word program for one sorting comparison

The fixed five-word format is ordered first by address, then by the
initialization flag, start cost and probe ordinal. Ties are broken by kind
and value. Empty records follow every occupied record. The comparator below
uses only fixed-offset reads, word constants, comparisons and conditional
selection. Each expression node costs one elementary operation.


### `Expr`

 Word expressions. A conditional selection is evaluated after its three
operands, so the operation count is independent of the input. 

### `Input`

 Two five-word comparison operands indexed by side and by field within each record. 

### `Expr.eval`

 Evaluate a comparison expression on the two input records, encoding truth by one and
selecting the false arm on a zero test. 

### `Expr.steps`

 Word-operation count for a comparison expression, charging field accesses, constants,
comparisons, and both arms of a select. 

### `Expr.eval_lt`

 Each intermediate result fits one word when both operands fit.
The immediate constants use at most two bits. 

### `program`

 The straight-line word comparison for two encoded slots. Tags outside
the occupied range 1--3 compare as empty, as in the parser. 

### `slotWords`

 Word values of the paper's physical record, viewed as naturals. 

### `inputs`

 Assemble the comparator input from two five-word arrays, choosing the right array on true
and the left array on false. 

### `compareSlots`

 Result and elementary word count of the fixed comparator. Natural field
values represent one word for every slot supplied by the word-format parser. 

### `parsedSlot`

 The word-level representation supplied by the five-word parser, including
its convention for unknown tags and noncanonical padding. Canonicality is
checked separately by `Format.decode`. 

### `Expr.runWord`

 Execute the syntax using genuine `w`-bit words. Each operand is evaluated
before its instruction, including all three inputs of conditional selection. 

### `compareWords`

 Evaluation directly on the two received five-word tuples. 

### `compareWords_eq`

 The direct word computation gives exactly the abstract slot order and
cost, even on arbitrary tag values that the raw parser interprets as empty. 

### `compareWords_encoded`

 Every valid record, including an initialization or empty record, can be
compared in the physical representation with the same result and step count. 

### `lexBit`

 Lexicographic step on ordinary unsigned word values. 

### `compareWords_lex`

 The bit-level sorting comparator can compute each lexicographic step
as soon as it has classified the two unsigned word values. 
