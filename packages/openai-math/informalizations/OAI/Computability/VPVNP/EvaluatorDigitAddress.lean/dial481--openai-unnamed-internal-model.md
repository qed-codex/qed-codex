---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing an address in the packed radix table

Each of the label rows holds `Z` digits, each of width `ℓ`. Fixed stack code
forms the row-major bit address from unary indices and copies the digit width
for the destructive lookup. The indices and dimensions survive every call.


### `Port`

 Unary registers for the label and column ordinals, row and digit widths, computed address
and scratch used to locate a radix digit. 

### `addressProgram`

 The physical calculation first forms the cell ordinal, then scales it by
the bit width. All temporary registers are cleared before returning. 

### `addressRoutine`

 The fixed stack routine that computes the starting bit address of a row-major digit cell
and prepares its width for lookup. 

### `registers`

 Register contents for label i and column j in a row with Z cells of width ℓ, including the
offset and cell-width tallies. 

### `ready`

 Initial unary registers for one cell. 

### `result`

 Address and width for the packed lookup, alongside the preserved inputs. 

### `addressTicks`

 Number of stack instructions used to compute the bit address and copy the cell width for
digit (i,j). 

### `addressRoutine_runs_framed`

 The address calculation can be called while the packed table, digit
accumulator, and evaluator state occupy arbitrary other stacks. 

### `cell_fits`

 A legal cell occupies an interval contained in the packed table. 

### `addressTicks_le_cells`

 Every cell address can be prepared in time linear in the size of the
table and its number of cells. This form also applies to width zero. 

### `addressTicks_le`

 At positive digit width the uniform cell-address clock is at most
twenty-four times the bit length of the table. 

### `copyCount`

 Initialize a loop counter by adding a preserved unary count. 
