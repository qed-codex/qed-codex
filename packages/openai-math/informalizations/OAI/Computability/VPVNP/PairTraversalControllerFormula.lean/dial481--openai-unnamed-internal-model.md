---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerFormula.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Runtime operands for the post-calendar traversal controller

One persistent word encodes the phase, physical level and site number. The
first pass writes every role. The second pass writes every descriptor. Each
burst reads its operands directly from the terminal and level headers.
All expression trees are fixed and use the repository's native compiler.


### `recipePub`

 The virtual five-word recipe ABI names the public square base and its
radix exponent. The last of the six input registers holds the true state word. 

### `terminal`

 Recover the high terminal header by adding the square workspace size to its base and
subtracting the 32-word header reservation. 

### `term`

 Read the specified scalar word from the terminal header computed by the traversal recipe. 

### `level`

 Read a field from level j using the terminal header's first-level pointer and level pitch. 

### `levels`

 The terminal-header expression for the number of physical traversal levels. 

### `initialSites`

 Initial site count used by the controller, with the terminal site count selected when the
directory contains only the initial level. 

### `pitch`

 Width of one phase-level block in the persistent state encoding, one larger than the
initial site count. 

### `phaseLevel`

 Decode the combined traversal phase and level ordinal by dividing the persistent state by
the phase-level pitch. 

### `site`

 Decode the within-level site ordinal as the remainder of the persistent state modulo the
pitch. 

### `index`

 Physical level ordinal obtained by reducing the combined phase-level number modulo the
level count. 

### `positiveIndex`

 Word-valued nonzero test on the current level ordinal, implemented by division by itself. 

### `previous`

 Preceding level ordinal, saturating at zero so the initial level remains a valid header
address. 

### `count`

 Select the current level's site count from the initial count or the preceding pass's output
count. 

### `formulas`

 Register order for control comparisons, state returns, and the three workers. 

### `R`

 Registers for the setup compiler followed by seven worker scratch words
and three readonly public/state inputs. 

### `vm`

 Embed the expression-evaluation registers in the leading portion of the traversal
controller register bank. 

### `value`

 Register containing the evaluated result of the given traversal operand formula. 

### `extra`

 A register beyond the formula evaluator, indexed among the ten extra traversal worker and
input registers. 

### `inputs`

 Assign the five public recipe operands and persistent state input to the extra controller
registers, reusing the workspace base where prescribed. 

### `scratchRegs`

 Embed the seven worker scratch registers in the controller bank after the register
evaluator. 

### `allocation`

 Construct the worker's register allocation from the designated formula outputs for its
public bank and current site. 

### `roleFields`

 Formula-output indices supplying the role writer's offset, row base, pitch, role code, and
unused zero fields. 

### `leafFields`

 Formula-output indices supplying the leaf-row writer's base and pitch, with zero values in
unused fields. 

### `fiberFields`

 Formula-output indices supplying the fiber count and row arrays, row capacity, preceding
row base, current row base, and pitch. 

### `roleAlloc`

 The role-tag worker's register allocation using its selected traversal formula outputs. 

### `leafAlloc`

 The leaf-row worker's register allocation using the initial layer base and row pitch. 

### `fiberAlloc`

 The fiber-row worker's register allocation using the selected placement directory and old
and new row bases. 
