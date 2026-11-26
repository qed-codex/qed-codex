---
{
  "module": "OAI/Computability/VPVNP/RankQueryStack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStack.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Continuation stack for scalar coefficient queries

A nonterminal query adds a sequence of products. The machine scans the sequence
in reverse index order and evaluates the two children of each product in turn.
Only one return frame is live per active level. The execution bound counts
push, pop and scalar-update transitions, and bounds the depth at every
intermediate configuration.


### `Program`

 A terminal query supplies a scalar. A composite query supplies the number
of products in its sum and computes the two subqueries from the product index. 

### `Program.describe`

 Return the value of a leaf query or the number of product terms to evaluate for a branch. 

### `Program.left`

 Select the left factor query of the indexed product term. 

### `Program.right`

 Select the right factor query of the indexed product term. 

### `Frame`

 Saved parent query, remaining scan count and partial sum, with the left factor value
retained while the right factor runs. 

### `Control`

 Current evaluator action, entering a query, scanning its sum, or returning a computed
value. 

### `Config`

 Evaluator configuration consisting of the current control and the stack of suspended parent
frames. 

### `step`

 One call, return, or loop transition. At a terminal result the state is fixed. 

### `Runs`

 A run of exactly `t` transitions, with at most `cap` saved frames
throughout. The endpoint also satisfies the cap. 

### `Realizes`

 Scalar recurrence to be realized by the machine. 

### `Descends`

 Both children of every actual call decrease the same depth bound. 

### `ArityLE`

 Every branch described by the program has at most `b` product terms. 

### `run_bounded`

 A clock and a simultaneous space bound for every invocation in any
continuation. The clock charges all control transitions. 
