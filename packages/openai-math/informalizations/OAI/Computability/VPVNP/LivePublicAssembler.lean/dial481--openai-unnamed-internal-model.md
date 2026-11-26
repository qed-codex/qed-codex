---
{
  "module": "OAI/Computability/VPVNP/LivePublicAssembler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicAssembler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicAssembler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Assembler operands for the primed pair

The index width is the one-based group's width. The cut field is the maximum
capacity shared by every pair. Actual cut lengths live in the three initial
RAM cells and therefore never occur in this public table.


### `Spec`

 Constants of the fixed live program. 

### `Spec.program`

 The universal-machine program whose literal prefix is placed in the primed pair inputs. 

### `Spec.groupExp`

 Exponent controlling the group index width and the height of the first half of the chain. 

### `Spec.adviceExp`

 Exponent giving the distributed advice length as a power of the input length. 

### `Spec.cutExp`

 Exponent giving the basic cut block width as a power of the input length. 

### `geometry`

 Compute the site's address and RAM word widths from the address multiplier and input
length, and attach the supplied bucket capacity. 

### `lengths`

 The paired chain's actual index, advice, and cut lengths for the specified pair at input
length n. 

### `R`

 Public expression for the number of sites in one group, two raised to the site-address
width. 

### `cells`

 Total cells in the input rectangle spanning both groups, twice the number of sites per
group times the input length. 

### `index`

 Public bit width of the one-based group index, one plus the input length raised to the
group exponent. 

### `advice`

 Number of advice bits in a primed row, given by the input length raised to the advice
exponent. 

### `capacity`

 Common capacity reserved for a cut, given by the input length raised to the sum of the
group and cut exponents. 

### `table`

 The sixteen public operands for primed pair assembly, including geometry, virtual scratch
base, literal prefix, incident widths, and cut capacity. 

### `table_eval`

 The sixteen expressions are the native assembler's public words before reduction modulo the word width. 

### `table_fits`

 Word fit for every intermediate of all sixteen assembler expressions. 
