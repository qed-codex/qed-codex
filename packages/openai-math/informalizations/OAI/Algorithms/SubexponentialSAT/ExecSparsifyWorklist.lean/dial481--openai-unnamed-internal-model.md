---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecSparsifyWorklist.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSparsifyWorklist.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSparsifyWorklist.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable depth-first worklist traversal for sparsification

The traversal manipulates a list of pending inputs explicitly. It never builds
the specification tree while running. A decreasing mass supplies a finite fuel
bound; the fuel loop halts as soon as the worklist is empty. The specification
tree is used only to prove the exact number of visited nodes.


### `Branching`

 A computable binary branching operation with a strict mass decrease in
each child. The decrease proof is erased by execution. 

### `State`

 The explicit traversal state. `leaves` is accumulated in reverse order. 

### `step`

 A single worklist transition. Pushing A before B makes this depth-first. 

### `transition`

 Partial transition semantics: the empty worklist is terminal. This is a
coarse list transition, not a primitive machine step. 

### `runFuel`

 Primitive recursion on a numeric fuel bound, stopping immediately when
the pending list becomes empty. 

### `runFuel_execution`

 The recursive program produces a genuine finite transition trace. Its
length is exactly the increase in the visit counter. 

### `runFuel_pending_nil`

 The fuel bound is derived from the mass decrease, independently of any
claimed sparsification node bound. 

### `run`

 The actual worklist program. The large fuel is represented as an integer;
unused fuel is never iterated after the worklist becomes empty. 

### `tree`

 A specification tree for one input, built by well-founded recursion on
the literal-mass measure. It is not materialized by `run`. 

### `step_node_conservation`

 One explicit worklist transition visits exactly one node of the remaining
specification forest. 

### `run_visits`

 The program's visit counter equals the exact number of processed tree
nodes; it is not an assumed running-time annotation. 

### `Evaluator`

 Measured callbacks return both their actual result and their event count. 

### `stepM`

 Count the displayed list cases, Boolean option case, list constructors,
and visit-counter successor, together with the actual callback events.
Counter bookkeeping is instrumentation; these are not primitive-bit costs. 

### `runM`

 The measured program loops until the worklist is empty. Its termination
measure exists only in the proof and is never stored or computed as fuel. 

### `nodeEvents`

 Exact event cost of a specification node, including the worklist's own
case/constructor events. It is defined from the executed callback counts. 

### `runM_events`

 Exact accumulation over the actual measured traversal. The extra one is
the final empty-worklist inspection. 

### `initial_runM_events_bound`

 Aggregation theorem for measured operations, distinct from primitive bit
complexity. Concrete use must discharge `hbound` with the callback's proofs. 

### `initial_run_visits_le`

 Every existing finite binary-tree bound applies to this actual worklist
visit counter after supplying the tree's path bounds. 

### `RefinesChoices`

 A finite-set semantic refinement of the executable branch operation.
The witness is an actual sunflower choice, not a node-count certificate. 

### `tree_is_decomposition`

 The worklist's specification tree is the shape of a genuine sunflower
decomposition, even when its deterministic enumeration differs from the older
finite-set selector. 

### `initial_run_visits_quantitative`

 The variable-σ node bound applies to the actual worklist visit count once
the executable selector has been refined to concrete sunflower choices. 

### `buildCandidatesM`

 Candidate construction with the actual clause-deduplication loop included. 

### `searchBudget`

 Includes recursive generation, all candidate checks, and composition events. 

### `generationBudget_le_cap`

 Enlarging the base to `m+1` also handles an empty input list. 

### `searchAtM`

 The measured search calls the measured checker on the generated candidates. 

### `scanWidthsM`

 Explicit width loop, charging each width and option inspection. 

### `selectM`

 All widths are inspected by the measured loop; no search is an atomic event. 

### `petalsM`

 Petal lists are built by measured membership filters over every selected clause. 

### `cleanLiterals`

 A list-only pass removing repeated literals from each clause. 

### `choiceOfSelected`

 Reconstruct the finite-set branch witness from the actual executable
selector's successful Boolean checks and minimum-width scan. 

### `children`

 Actual executable children, with only literal deduplication after the
branch. No extra tautology deletion changes the finite-set child identity. 

### `splitFormula`

 The actual executable selector and child constructors used by the loop. 

### `formulaMass`

 The mass is computed by explicit clause/literal deduplication and list
lengths. Its equality with mathematical literal mass is proved separately. 

### `executableBranching`

 The generic engine is now instantiated by the actual list search. 

### `normalizedInput`

 Normalize once at input. The last cleanup is semantically redundant but
makes the raw-width invariant explicit at the worklist interface. 

### `execute`

 Actual finite list-CNF depth-first sparsification. 

### `execute_models`

 Pointwise assignment semantics: the output formulas' disjunction equals
the input formula, before existentially quantifying over assignments. 
