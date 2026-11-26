---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ProgramLogic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramLogic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramLogic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measured verification rules for fixed bit programs

Every execution judgment below contains actual transitions of one fixed step
function. Loop iterations may be controlled by unbounded data; neither the
transition function nor its finite control changes with the iteration count.
No judgment assigns a cost to an unimplemented mathematical function.


### `trace_cut`

 Cut an actual trace at a specified step index. 

### `invariant_trace`

 An inductive configuration invariant holds throughout any actual trace. 

### `frame_trace`

 A frame observation preserved by each actual step is preserved by the run. 

### `Spec`

 A relational, input-dependent measured specification for one fixed program.
Its postcondition may refer to both the initial and final configurations. 

### `instruction`

 A specified actual instruction establishes a one-step specification. 

### `consequence`

 Strengthen the input condition, weaken the relational output condition,
and enlarge a bound already proved for actual executions. 

### `sequence`

 Compose two measured blocks on the same concrete transition function.
The second block's bound is bounded in terms of the original input. 

### `cases`

 Branching on an initial-state predicate combines existing measured proofs;
a concrete guard instruction must be included in the branch specifications. 

### `frame`

 Preserve a frame alongside a proved specification. 

### `countdown`

 Total execution of a countdown loop, with the sum of the actual
per-iteration bounds and a separately charged exit block. The invariant may
relate the natural index to a binary counter in unbounded program storage. 

### `countdown_uniform`

 A uniform body bound yields the usual linear-in-iteration-count budget,
without putting that iteration count in finite control. 

### `while_variant`

 A while-loop variant may decrease by more than one. Each loop traversal
and the final exit must be proved using the same actual step function. 

### `registerWrites`

 Registers possibly modified by this concrete instruction. 

### `stackWrites`

 Stacks possibly modified by this concrete instruction. Peeking is read-only. 

### `RegionTrace`

 Every transition is still a transition of p; region membership records only
the instruction addresses executed before the final boundary is reached. 

### `Block`

 An active block entry and an explicit active-or-halted exit boundary.
The final boundary instruction is not executed by this specification. 

### `countdown`

 A loop body returns to the same concrete header. Its decreasing index is
assertion data, not an additional control label or register type. 

### `while_variant`

 The data-dependent while rule specialized to one concrete program header.
Branch tests and back edges must be included in the supplied measured blocks. 
