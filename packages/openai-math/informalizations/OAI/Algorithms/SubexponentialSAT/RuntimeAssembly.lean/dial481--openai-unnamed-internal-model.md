---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RuntimeAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RuntimeAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RuntimeAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From explicit phase budgets to a primitive-machine runtime

The numerical theorems charge initialization, every sparsification node, and
five separate phases of every leaf.  The execution bridge additionally requires
actual traces of one fixed primitive bit machine.  No machine satisfying these
certificates is constructed here.  In particular `ImplementationCertificates`
is an explicit collection of open implementation obligations, not a theorem.


### `LeafWork`

 The five separately charged phases at a sparsification leaf.  `inner`
means symbolic moment computation on a large input and exhaustive search on a
small input.  Arithmetic costs are numbers of primitive-machine transitions. 

### `Work`

 The list `tree` charges all visited nodes, including internal nodes.
`startup` includes parsing/normalization and construction of fixed objects. 

### `ScheduledRun`

 An actual run through a finite sequence of bounded phases.  No transition
of `step` is replaced by a semantic oracle or a unit-cost arithmetic command. 

### `PipelineExecution`

 A genuine primitive-machine execution, split into the charged phases.
The choice of one machine is outside the input quantifier in the final bridge. 

### `ReductionCertificate`

 The semantic obligations are stated at the finite reduction and leaf-test
level, rather than assuming correctness of the whole solver.  The number of
semantic leaves agrees with the number whose work is charged. 

### `polynomial`

 A common polynomial envelope may dominate finitely many different phase
polynomials.  Its coefficient and degree must be fixed before the input. 

### `polynomial_variables_le_input`

 Transfers variable-count polynomial overhead to the explicit input length
using the concrete encoder's proved length bound. 

### `rawSymbolicWork`

 Exact product of the moment-index count, the two coset-enumeration
counts, and a supplied dense arithmetic count.  This is a loop count, not
a primitive-machine runtime assertion. 

### `rawSymbolicWork_le`

 Combines actual retained-monomial cardinality with the coset loop bound.
`denseCost` must be supplied by a proved arithmetic-loop count. 

### `inner_steps_le_of_dense_loops`

 The missing bridge from scalar/index loop steps to primitive bit steps
is stated explicitly in `hsteps`. The polynomial certificate also charges
the number of points, ring operations per iteration, and dense-loop overhead. 

### `denseArithmeticEvents`

 A common event budget for either instrumented dense multiplication or
addition on the actual retained coefficient slots. 

### `instrumented_symbolic_work_le_real`

 No symbolic-arithmetic size bound is assumed here: it is supplied by
the instrumented list recursions in `SymbolicCost` and the retained-slot count. 

### `WorkBounds`

 The numerical obligations, intentionally separated from trace existence.
There is no final `2^(0.9*n)` bound among the assumptions.  The inner bound
allows the explicit factor two in the two separated sums. 

### `symbolic_schedule_bit_bound`

 A local primitive simulation can supply the symbolic bit bound without
assuming a bound on the whole symbolic phase: each listed scalar/index event
has its own primitive trace and bounded cost. The number of those events is
bounded by the finite dense-loop count. 

### `instrumented_symbolic_has_bounded_run`

 Complete local cost bridge using the proved dense-arithmetic event count.
The still-required hypotheses are the actual primitive traces, bounded cost
of each scalar/index/list event, a count of those events, and a polynomial
envelope for the remaining factors. 

### `total_le_eight_polynomial_sq`

 Complete numerical assembly, charging all node work and all five leaf
phases.  The square of the common polynomial pays for the node count and
per-node/per-leaf work; the harmless coefficient eight includes initialization. 

### `total_le_runtimeBound`

 An exponential bound can be substituted only after the phase budgets
have been supplied. This remains a numerical theorem about `Work.total`. 

### `smallFactor`

 Includes sparsifying the bounded-variable input before exhaustive leaf
search, as in the manuscript. Thus no unproved early-bypass optimization is
needed for the small-input case. 

### `ImplementationCertificates`

 Open implementation certificates, with all phase bounds visible.

For every encoded input, an inhabitant must provide (1) traces of the same
primitive machine, (2) a correct output, (3) bounded all-node enumeration,
(4) polynomial node and initialization work, (5) table construction,
(6) layout construction, (7) symbolic arithmetic or exhaustive-search bit
cost, (8) CRT reconstruction, and (9) the final output cost.

In particular this record is not discharged by operation-count/cardinality
theorems, by an abstract cost annotation, or by a semantic SAT function. 

### `decidesWithBound_of_certificates`

 The final bridge is conditional on the explicitly listed primitive-machine
certificates. Neither existence of the machine nor these certificates is
asserted by this module. 
