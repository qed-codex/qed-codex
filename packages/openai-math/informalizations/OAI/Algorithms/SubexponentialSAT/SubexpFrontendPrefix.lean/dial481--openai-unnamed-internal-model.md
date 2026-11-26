---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFrontendPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFrontendPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFrontendPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A raw-input program for the growing parameters

The program has fixed control and six Boolean stacks. It parses the existing
canonical input, retains the declared count, computes both binary logarithms,
and divides their result by sixteen. The body remains on stack 0, while stacks
2, 4, and 5 hold n, s(n), and u(n). Stacks 1 and 3 are cleared work space.

This implementation uses the declared variable universe. The canonical unary
header already proves n <= input length, and the executable sparsifier performs
its own normalization. The separate dense-renaming semantics remain available
in SubexpFrontend; no unproved remapping program is called here.


### `bound`

 Includes the outer halt and both preserving copies. 

### `run_raw`

 One fixed program computes all three retained integer words directly
from the raw unary-header input and preserves the entire formula body. 

### `run_formula`

 The actual canonical CNF input is accepted directly, with a fixed
quadratic source-step bound in its encoded length. 

### `run_formula_primitive`

 The compiler turns this raw-input prefix into an actual primitive-tape
run. The multiplier is fixed by the single finite program, before n or F. 
