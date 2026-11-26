---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsPhaseRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPhaseRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPhaseRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling current-level formulas to native row planners

Expressions can read the level pointer, the five controller ports, and memory
at computed addresses. The compiler allocates disjoint output registers and
reuses a bounded scratch interval between formulas. Natural literals are
synthesized from their binary digits using word additions. Every read finishes
before the row writer installs its first field.


### `Expr`

 A word formula for planning a directory row from constants, the controller's five public
words, the current level pointer, memory loads and RAM binary operations. 

### `Expr.eval`

 Compute the formula's machine word in the current level and entry memory. A load reads
memory at the address obtained by evaluating its subexpression. 

### `Expr.add`

 Form the sum of two planner expressions using machine-word addition. 

### `Expr.mul`

 Form the product of two planner expressions using machine-word multiplication. 

### `Expr.sub`

 Subtract the second planner expression from the first at the machine's word width. 

### `Expr.div`

 Form the unsigned integer quotient of the two word values computed by planner expressions. 

### `Expr.mod`

 Form the unsigned remainder of the first planner expression's value modulo the second's. 

### `Expr.headerAddress`

 Address expression for field offset `i` from the current level header, whose base is
carried in persistent state. 

### `Expr.header`

 Load a level-header field at the given word offset from the current state pointer. 

### `Expr.rowBase`

 Address of the directory row to publish, computed as the directory base plus the stored
ordinal times the row width `g + 3`. 

### `Expr.slots`

 Number of consecutive scratch registers used to compile this expression. Binary operations
keep the left result while compiling the right operand one register later. 

### `Expr.compile`

 The scratch register at `start` holds the result. A right subexpression
begins one register later and may reuse the left subexpression's temporaries. 

### `Expr.loads`

 Number of external reads when evaluating an expression. Repeated occurrences
are counted separately, including repeated loads of the same header field. 

### `Phase`

 Parameters occupy a full catalog-width row, including any padding. 

### `Phase.tag`

 Numeric worker tag written at the start of the directory row so the launcher can select
  the pass. 

### `Phase.initial`

 Expression for the worker's first cursor, stored immediately after its tag. 

### `Phase.stop`

 Expression for the exclusive cursor bound at which the worker scan returns to the
  controller. 

### `Phase.params`

 Expressions for the worker's public operands in directory order, including any padding to
  the catalog width. 

### `Phase.ofParams`

 Pad a worker's finite operand vector at the high end of the row. 

### `Phase.registerCount`

 Number of planner registers needed for the row address, its `g + 3` fields and the largest
scratch interval used by any one formula. 

### `Phase.recipe`

 One fixed finite native recipe for a phase of the online calendar. 

### `Phase.recipe_reads`

 The row address contributes one ordinal read. All remaining reads arise
from the starting cursor, stopping cursor, and padded public operands. 

### `Phase.words`

 Evaluate the directory row in the current header and memory, yielding the tag, starting
cursor, exclusive stop and all parameter words in storage order. 

### `execute_phase`

 A completed native planner accepts with the computed worker row installed in
the current directory slot. All expression loads see the input memory. 

### `row_fields`

 Pointwise interface to the launcher's row reader. The last equality uses
the same origin and offset as the worker parameter frame. 

### `RefreshHeader`

 The seven pointer fields are in the native refresh visitor's public order:
old widths, bundle targets, port shifts, bundle totals, outgoing offsets,
incoming offsets, and incoming widths. 

### `RefreshHeader.vertices`

 Offset in the current level header of the vertex-count word used to compute the refresh
  scan length. 

### `RefreshHeader.degree`

 Offset of the degree word used both as the first refresh operand and to compute the
  numbers of bundles and slots. 

### `RefreshHeader.residualLanes`

 Offset of the residual-lane count used to expand each vertex and port into refresh
  bundles. 

### `RefreshHeader.heads`

 Offsets of the seven array pointers for old widths, bundle targets, port shifts, bundle
  totals, outgoing offsets, incoming offsets and incoming widths, in worker order. 

### `RefreshHeader.bundles`

 Planner expression multiplying the header's vertex count, degree and residual-lane count to
obtain the number of refresh bundles. 

### `RefreshHeader.slots`

 Planner expression for the exclusive end of the refresh scan, one degree-sized block of
slots per bundle. 

### `refresh`

 Plan a refresh scan from cursor zero to the slot count computed from the header. Its eight
public operands are the degree and the seven array pointers. 

### `headerCell`

 Read the machine word at offset `i` from the level header pointed to by the persistent
state. 

### `refreshPublic`

 Read the refresh worker's eight public words from the current header, placing the degree
first and the seven array pointers after it. 

### `refresh_stop_val`

 With the physical slot count in range the word multiplication computes the
natural exclusive stop, including zero vertices, degree or residual lanes. 

### `execute_refresh`

 The accepting planner for the refresh worker constructs the actual eight
public operands directly from the header and supplies the computed segment count. 
