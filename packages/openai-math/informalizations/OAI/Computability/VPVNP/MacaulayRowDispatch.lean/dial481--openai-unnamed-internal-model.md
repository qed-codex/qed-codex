---
{
  "module": "OAI/Computability/VPVNP/MacaulayRowDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRowDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRowDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native dispatch of an augmented Macaulay row

The first block contains the integer equations, followed by the affine slice
rows, each paired with every multiplier monomial. The last block contains the
powered monomials. One fixed register routine computes the kind of the row,
the index of its equation or pin, the ordinal of its source monomial, and the
unaltered column ordinal. All these numbers are runtime operands.


### `Kind`

 The row block determines which coefficient routine runs for an original equation, an affine
pin or an appended powered monomial. 

### `Kind.tag`

 Numeric dispatch tag for a row block, numbered 0 for equations, 1 for pins and 2 for
powers. 

### `Address`

 Decoded address of a Macaulay entry, giving the row block, its local equation or pin index,
and the source and column monomial ordinals. 

### `Address.kind`

 Row block whose coefficient routine reads this entry. 

### `Address.row`

 Index within the original equations or affine pins. The decoder uses zero in this field
  for appended powers. 

### `Address.source`

 Ordinal of the multiplier monomial for an equation or pin, or of the source monomial for
  an appended power. 

### `Address.column`

 Ordinal of the requested column monomial. 

### `Address.fields`

 Encode the decoded address as six output words in the order tag, local row, source ordinal,
column ordinal, zero, zero. 

### `address`

 These three cases use the same contiguous row ordering as `appendRows`
and the two equation blocks of `slicedQueryData`. 

### `inputs`

 Form the eight input words from the row, column, equation count, pin count and multiplier
count, followed by three zeros. 

### `cap`

 Number of scratch registers required by the compiled row decoder. 

### `Reg`

 Register indices for the decoder's eight inputs, six outputs and scratch space. 

### `Small`

 Physical ISA ports for the decoder's register bank, with zero public memory ports. 

### `machine`

 Fixed register routine that decodes an augmented row and returns its block and local
indices. 

### `ticks`

 Upper bound on decoder ticks from the emitted instruction count and the cost per
instruction on width-`w` words. 

### `requiredWidth`

 Sufficient word width for intermediate computations when each decoder input fits in `bits`
bits. 

### `inReg`

 Locate one of the eight input words in the decoder's register bank. 

### `outReg`

 Locate one of the six decoded address words in the registers immediately following the
inputs. 

### `machine_runs`

 The output ports are numbered by `Address.fields`. Input ports preserve
both supplied ordinals and all advised row counts. 

### `original_address`

 Recover an equation row and the dense ordinal of its multiplier. 

### `affine_address`

 Affine rows retain their pin index when the prefix of integer equations
is removed. 

### `power_address`

 The appended row reads the source monomial ordinal in the suffix. 
