---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTautologyFilterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTautologyFilterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTautologyFilterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual tautological-clause filtering

The outer record loop runs the checked clause-tautology machine on each clause,
emits exactly the clauses that it rejects as tautologies, and restores their
original list order. The Boolean predicates below specify this concrete code;
they are not instructions available to the machine.


### `raw_input_runsIn`

 This starts with the actual raw encoded formula and empty work stacks. 

### `filter_primitive_execution`

 The finite-control execution compiles to an actual primitive tape trace. 
