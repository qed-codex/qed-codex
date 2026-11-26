---
{
  "module": "OAI/Computability/VPVNP/LivePublicParser.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicParser.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicParser.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reconstructing the public words of the primed pair parser

In Section 14 the live evaluator reproduces the auxiliary machine's finite
table. Its last eighteen public words specify scratch addresses, parser
dimensions and schedule endpoints. Their expressions below use the first
sixteen public words together with the prescribed grammar-state count and
root. They use only length data and fixed arithmetic, independently of
pair-specific cut lengths, exterior bits and nominations.


### `Inputs`

 Length expressions for the assembler's public operands, the grammar state count, and the
root state. 

### `Inputs.assembler`

 The sixteen public operands of the primed input assembler. 

### `Inputs.states`

 Public expression for the number of grammar states. 

### `Inputs.root`

 Public expression for the grammar's root state ordinal. 

### `n`

 Input length recovered from the assembler's second operand. 

### `R`

 Number of sites per group recovered from the assembler's third operand. 

### `rectangle`

 Total number of input cells for both groups, taken from the assembler's first operand. 

### `base`

 Base of the second-pass assembled input rectangle, immediately after the first-pass choice
rectangle. 

### `degreeBase`

 Base of the parser's degree stack, immediately after the assembled input rectangle. 

### `stateBase`

 Base of the parser's state stack, one input length past the degree stack base. 

### `markBase`

 Base of the terminal-position mark array, one input length past the state stack base. 

### `histBase`

 Base of the label histogram, one input length past the mark array base. 

### `degree`

 Largest zero-based degree index for the full-degree grammar, the input length minus one. 

### `triangle`

 Number of positive binary degree splits over degrees through the input length. 

### `terminal`

 Number of terminal production labels, with one for each state, input position, and Boolean
bit. 

### `binary`

 Number of binary production labels, with one for each degree split and ordered triple of
states. 

### `labels`

 Total number of terminal and binary production labels checked by the parser. 

### `headerEnd`

 First word beyond the reserved primed header, after three length words, two group indices,
advice, and two cut capacities. 

### `assembly`

 Number of calls across the two rectangular input assembly passes. 

### `rowSpan`

 Number of parser calls for each site, three times the input length. 

### `rows`

 Total site rows in the two groups, twice the number of sites per group. 

### `compareStart`

 First call cursor of the histogram comparison phase after input assembly and all per-site
parser calls. 

### `total`

 Total number of scheduled calls through the last label comparison. 

### `parser`

 The fourteen parser parameters in the auxiliary machine's order. 

### `schedule`

 The four bounds partition the absolute cursor into assembly, site and
final histogram-comparison calls. 

### `table`

 Assemble the 34 public words in order from the sixteen assembler operands, the parser
operands, and the schedule operands. 

### `Values`

 Numerical inputs to the suffix construction, before word packing. 

### `table_eval`

 Re-evaluating the expressions gives the native auxiliary table exactly. 

### `table_fits`

 The existing parser bounds imply that every intermediate computation of
the suffix is word-sized. In particular, the numerator of the triangular
label count fits before it is divided by two. 
