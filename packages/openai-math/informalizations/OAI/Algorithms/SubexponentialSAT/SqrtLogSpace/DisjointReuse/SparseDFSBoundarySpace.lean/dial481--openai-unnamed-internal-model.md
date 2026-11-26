---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSBoundarySpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSBoundarySpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSBoundarySpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical storage at the depth-first controller boundary.

Only framed formula bodies occur on the pending stack. The mathematical depth
is a proof index and is not serialized. Both children, the current formula,
the declared-variable word, and the two count words are charged simultaneously.
These bounds apply to the actual fixed frontier and accumulator routines after
injective port relocation. The final DFS must still establish its boundary
invariant and bounds for the concrete selector, splitter, and leaf commands.


### `clearProgram_stack_length_le`

 Actual cleanup never increases any stack, at any prefix. No bound on
elapsed time is needed: its finite table contains only pop, branch and halt. 

### `frontier_length_le`

 The delimiter and every escaped body bit are included. 

### `boundaryStacks`

 The finite DFS port view. Scratch and all other selector ports are empty
at this boundary; `rootEmbedding` puts persistent words above the leaf bank. 

### `boundary_space`

 Count words are canonical, so cancellation or redundant zero padding
cannot invalidate this actual byte-length bound. The two framed children may
coexist with the original formula and the complete pending frontier. 

### `popStack`

 Local current, saved-n, pending and scratch ports. 

### `pairStack`

 Local pending, saved-n, framed children and scratch ports. 

### `countStack`

 Local running total, current leaf count and scratch ports. 

### `rootEmbedding`

 DFS bookkeeping retains its original ports inside the frozen 1220-stack ABI.
Current formula, threshold, frontier, header and counts lie above its low scratch bank.
View port zero remains scratch, while view port thirteen is the formula. 

### `rootStacks`

 Full root boundary stacks, including retained raw input and the two
binary setup parameters. Every unassigned stack is empty. 

### `root_boundary_space`

 All 1220 stacks are bounded, including raw input and setup data outside
the finite DFS view. The reserved high bank is empty in this exact state. 

### `pop_lifted_space`

 The pop's actual transient scratch is bounded independently of how many
earlier DFS iterations have run. Unmapped caller stacks retain their bound. 

### `pair_lifted_space`

 Both framed children are present at entry. The existing concrete pair
copy consumes each child; its prefix bound includes both copies and scratch. 

### `count_lifted_execution`

 One concrete accumulator call returns the canonical new total and clears
both temporary ports. Its prefix bound is uniform across all visited leaves. 
