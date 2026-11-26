---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Computation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Computation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Computation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measured machine execution for the candidate SAT theorem

The definitions here use the transition semantics of mathlib's finite TM2 machines.
A bound is accompanied by an actual execution certificate; no cost is assigned to
an arbitrary mathematical function. TM2 counts executions of finite statements.
Each fixed statement contains finitely many primitive stack operations.


### `Trace`

 An explicit finite trace of successful transitions. 

### `RunsIn`

 A runtime bound means that a transition trace within that bound exists. 

### `iff_evalsToInTime`

 Our trace bounds are equivalent to mathlib's measured execution certificates. 

### `terminal_unique`

 A deterministic transition function cannot produce two different terminal results. 

### `BoundedSimulation`


A local simulation obligation: every source transition has an actual target
execution using at most the given overhead target transitions. This is a proposition
about transition functions, not an asserted cost for a source function.


### `simulate_trace`

 Local measured simulations compose over a whole source trace. 

### `simulate_runsIn`

 The bounded version allows an upper bound on the source trace length. 

### `BoundedSimulation.comp`

 Two measured refinements compose with the product of their constant overheads. 

### `CostedTrace`


A source trace carrying a sum of proposed per-transition costs. This record
alone is not a target-machine runtime proof; that conclusion requires the
measured local simulations in simulate_costedTrace.


### `CostedTrace.exists_trace`

 A costed trace still contains genuine source transitions. 

### `simulate_costedTrace`


State-dependent operation costs give a target runtime bound only when every
source transition is implemented by an actual target trace within that cost.


### `BitMachine`


A finite-control TM2 machine with a binary input/output interface.
We additionally require every work-stack alphabet to be finite.


### `OutputsInTime`


The machine really executes at most the stated number of transitions and halts
with the stated output. The underlying certificate also requires cleared work
stacks and reset finite state, following mathlib's TM2OutputsInTime convention.


### `outputs_unique`

 Successful executions of this deterministic machine have a unique output. 

### `identity`

 A concrete binary identity machine, witnessing that the contract is inhabited. 

### `PrimitiveMachine`


A primitive multitape bit machine. The finite control first selects one tape.
Its transition table reads only that tape's current bit (or blank), then either
halts with one Boolean answer, moves that tape by one cell, or writes one cell.
There are no statement blocks or unbounded arithmetic primitives.


### `Cfg`

 Tape contents are the only unbounded component of a configuration. 

### `step`

 One primitive transition, acting on at most one bit/blank tape cell. 

### `init`

 The actual input word is placed on one tape; every other tape is blank. 

### `OutputsInTime`

 A measured execution ending in the specified accepting/rejecting state. 

### `constantMachine`

 A fully specified finite program returning a fixed bit in one primitive step. 

### `MachineSimulation`


A machine simulation must explain actual local transitions and both input/output
representations. An asserted source running time alone cannot supply this record.


### `MachineSimulation.outputs`

 Constant-overhead simulation transports measured output certificates. 

### `runtimeBound`


The claimed bit-time envelope. The polynomial variable is the length of the
specific explicit encoding, and the exponential variable is the variable count.


### `MacrostepDecidesWithBound`


Correctness and measured running time for every formula of the specified width.
The output is one bit, and both possible outputs are tied to satisfiability.
The encoder is fixed by SubexponentialSAT.Encoding, rather than existentially chosen.


### `MachineSimulation.preserves_bound`


The same exponent is preserved by a proved constant-overhead machine simulation.
The multiplicative constant is charged explicitly.


### `DecidesWithBound`


Correctness and complexity on the primitive bit machine, using the fixed
explicit CNF encoding. No macrostep or arithmetic operation is counted as a
single step in this definition.


### `MacroToPrimitiveSimulation`


The precise refinement required to turn a finite TM2 block program into a
primitive-bit machine. Every transition needs a measured primitive execution;
the constant overhead cannot be supplied by an unsupported cost annotation.


### `MacroToPrimitiveSimulation.outputs`

 A completed low-level refinement transports actual output executions. 

### `MacroToPrimitiveSimulation.preserves_bound`

 The primitive-bit bound charges the refinement's constant explicitly. 

### `MacrostepExponentFeasible`

 The weaker, separately named claim about finite TM2 statement-block steps. 

### `ExponentFeasible`


The machine, constant, and positive integer polynomial degree are fixed before
the number of variables and the formula vary. This is the exact quantifier
order needed by the candidate's uniform saving.


### `exponentFeasible_of_macro_simulation`


A concrete macrostep algorithm yields the primitive-bit target only after a
positive constant-overhead low-level simulation has actually been supplied.


### `exponent_mono`

 Increasing the allowed exponential running time preserves feasibility. 

### `width_antitone`

 An algorithm for wider clauses also handles every smaller width. 

### `CandidateTheorem`


The candidate theorem as a precise, unproved computational proposition.
There is intentionally no declaration claiming an inhabitant of this proposition.

