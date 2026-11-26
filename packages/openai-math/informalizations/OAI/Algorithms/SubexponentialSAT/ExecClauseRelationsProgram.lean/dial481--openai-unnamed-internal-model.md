---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseRelationsProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseRelationsProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseRelationsProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving encoded clause relations

Two invocations of the concrete subset tester compute equivalence and strict
inclusion. The original encoded clauses occupy stacks 8 and 9 throughout;
stacks 0 through 7 are empty workspace at both boundaries. Registers 10 and
11 return equivalence and strict inclusion, respectively.


### `subset_eval`

 The subset routine has an actual trace. Its lifted call preserves the two
original clauses and the caller's two saved Boolean flags. 

### `compare_eval`

 A complete directional comparison restores all workspace, so the same
fixed routine can be invoked with the clause ports interchanged. 

### `program`

 One finite instruction table serves every pair of encoded clauses. 

### `command_eval`

 Every copy, subset test, stack cleanup, and Boolean instruction contributes
to this measured polynomial bound. 

### `command_eval_all`

 The same execution also exposes the reverse-inclusion failure bit, used
to reject a proposed core that is not contained in a candidate clause. 

### `program_relations`

 Extensional clause semantics for the actual computed result flags. 

### `nat_command_eval`

 Direct interface for the canonical unary literal-list representation.
The program is unchanged; injectivity connects its bitwise tests to literals. 
