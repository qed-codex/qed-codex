---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native runtime leaf parameter production, integer guards, and paid setup.
The former composition modules are import-only compatibility shims. 

 A fixed ten-comparison bit guard. All operands are runtime binary words.
This module states their data relation separately from parameter production. 

### `checks`

 The list is fixed syntax; in the final guard it has exactly ten entries. 

### `dispatchCommand`

 Both continuations are real structured commands. The selected branch is
charged after all ten comparisons, including failed fast-path guards. 

### `Instr`

 A finite arithmetic instruction table. All natural-number fields in this
type are code constants or physical port indices. Operand values reside in
Boolean stacks and are read by the concrete routines in `command`. 

### `instruction_eval`

 Uniform exact semantic and physical-cost contract, discharged by the
concrete Boolean-stack routines for every instruction constructor. 

### `program_eval`

 Execute a fixed finite arithmetic circuit. Its returned bound includes
all arithmetic, copying, and every nested loop in the concrete primitives. 

### `result_value_frame`

 Values in ports untouched by the table are preserved exactly. 

### `earlyCode`

 Low eight slots hold ambient n, residual n, original clause count, actual
occurrence bound, maximum arity, full factor count (hash+marked+neutral),
formula width, and total incidences.
The remaining finite table is straight-line syntax, not an input oracle. 

### `command_eval`

 Program-level integration contract. The next theorem discharges its
structural arithmetic readiness from the explicit table. 

### `admissible`

 Every output is fresh and every division denominator is positive for all
inputs. The final safe divisor is max(1,Q); the fast-path guard later implies
Q>=2 and hence identifies it with Q. 

### `preparation`

 Materialize the twenty comparison operands. Public parameter slots and
all eight original metadata words are preserved. Reused private slots are
cleared by real stack programs before each new arithmetic result. 

### `setup_eval`

 A native setup-and-test trace. The operand words are produced by the
numeric program itself before the ten bit comparisons are executed. 

### `dispatch`

 Both branches are finite bit programs. Every input first pays the full
numeric setup and comparison cost, including inputs routed to fallback. 

### `scale`

 Only these numeric values control loops or increase representation length.
The numeric result of a power is deliberately absent. 

### `budget_majorant`

 A single global bound on numeric loop parameters yields a polynomial
bound for every fixed instruction table, regardless of large output values. 

### `iterMajorant_polynomial`

 The deliberately loose degree is a fixed constant once the finite table
is fixed. It establishes a genuine ordinary-polynomial setup bound. 

### `scaleBound`

 The only input values entering loop costs are precisely the four small
operands bounded in CrudeBounds. All power outputs affect later work through
binary word lengths alone. 

### `guarded_budget_ordinary`

 Ordinary-polynomial bit work, uniformly over all padded input words.
The constants depend only on the fixed table, never on an input parameter. 

### `runtime_ordinary`

 The complete physical parameter setup, including all guards and halt,
has a fixed ordinary-polynomial bound in input counts and padded bit lengths. 

### `EncodesParameters`

 Public output ABI for a successful fast-path parameter setup. Other
entries are paid working values and need not be interpreted by callers. 

### `setup_output`

 Native end-to-end parameter production and guard testing. On a successful
fast path every public output word encodes its exact specified parameter. 

### `code`

 Input t is at33 and qE at35. The two derived metadata words are
qE−2 at44 and B=2t at45. No other numeric table entry changes. 
